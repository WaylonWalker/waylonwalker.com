#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["typer>=0.16", "pyyaml>=6", "pydantic>=2"]
# ///
"""Track post reviews and commit attributed edits without unrelated changes."""
from __future__ import annotations

import hashlib
import json
import os
import shlex
import subprocess
import tempfile
import uuid
from datetime import datetime, timezone
from functools import cache
from pathlib import Path
from typing import Annotated, Literal
from urllib.parse import quote

import typer
import yaml
from pydantic import BaseModel, ConfigDict

app = typer.Typer(no_args_is_help=True, help=__doc__)
Role = Literal["copy-editor", "internal-link-editor"]
EXCLUDED = {"authors", "editorial_history"}


class Record(BaseModel):
    model_config = ConfigDict(extra="forbid")
    schema_version: int = 1
    event_id: str
    author: str
    role: Role
    action: Literal["edited", "reviewed"]
    recorded_by: str
    recorded_at: str
    base_commit: str
    commit: str
    path: str
    content_digest: str
    digest_version: str = "editorial-v1"
    file_url: str
    diff_url: str
    summary: str


def git(*args: str, env: dict[str, str] | None = None) -> str:
    result = subprocess.run(["git", *args], capture_output=True, env=env)
    if result.returncode:
        raise ValueError(result.stderr.decode().strip())
    return result.stdout.decode().strip()


@cache
def root() -> Path:
    return Path(git("rev-parse", "--show-toplevel"))


def split(text: str) -> tuple[str, str, dict]:
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        raise ValueError("Post must have YAML frontmatter")
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        raise ValueError("Unclosed frontmatter")
    front = "".join(lines[1:end])
    data = yaml.safe_load(front) or {}
    if not isinstance(data, dict):
        raise ValueError("Frontmatter must be a mapping")
    node = yaml.compose(front)
    keys = [key.value for key, _ in node.value] if node else []
    if len(keys) != len(set(keys)):
        raise ValueError("Duplicate frontmatter keys")
    return front, "".join(lines[end + 1:]), data


def digest(text: str) -> str:
    _, body, data = split(text)
    relevant = {key: value for key, value in data.items() if key not in EXCLUDED}
    serialized = json.dumps(relevant, sort_keys=True, ensure_ascii=False, default=str)
    return "sha256:" + hashlib.sha256((serialized + "\n" + body).encode()).hexdigest()


def replace_fields(text: str, fields: dict) -> str:
    """Replace only named top-level fields; retain prose and other YAML bytes."""
    front, body, _ = split(text)
    node = yaml.compose(front)
    spans = []
    pairs = node.value if node else []
    for i, (key, _) in enumerate(pairs):
        if key.value in fields:
            end = pairs[i + 1][0].start_mark.index if i + 1 < len(pairs) else len(front)
            spans.append((key.start_mark.index, end))
    for start, end in reversed(spans):
        front = front[:start] + front[end:]
    additions = yaml.safe_dump(fields, sort_keys=False, allow_unicode=True, width=78)
    return "---\n" + front.rstrip("\n") + "\n" + additions + "---\n" + body


def post_path(value: Path) -> str:
    path = value.resolve()
    base = root()
    relative = path.relative_to(base).as_posix()
    if not relative.startswith("pages/") or path.suffix != ".md" or path.is_symlink():
        raise ValueError(f"Expected a Markdown post under pages/: {value}")
    git("ls-files", "--error-unmatch", "--", relative)
    return relative


def clean(paths: list[str]) -> None:
    if git("status", "--porcelain", "--", *paths):
        raise ValueError("Selected posts must be clean. Commit their owned changes first.")


def session_dir() -> Path:
    return Path(git("rev-parse", "--absolute-git-dir")) / "editorial"


def save(session: dict) -> None:
    directory = session_dir()
    directory.mkdir(exist_ok=True)
    destination = directory / f"{session['id']}.json"
    temporary = destination.with_suffix(".tmp")
    temporary.write_text(json.dumps(session, indent=2) + "\n")
    temporary.replace(destination)


def load(session_id: str) -> dict:
    uuid.UUID(session_id)
    return json.loads((session_dir() / f"{session_id}.json").read_text())


def begin(paths: list[str], author: str, role: Role) -> dict:
    if not author.strip():
        raise ValueError("Author must be a stable, nonempty ID")
    clean(paths)
    session = {
        "id": str(uuid.uuid4()), "author": author, "role": role,
        "base_commit": git("rev-parse", "HEAD"), "phase": "started",
        "posts": {p: {"before": (root() / p).read_text(), "digest": digest((root() / p).read_text())} for p in paths},
        "commits": [],
    }
    save(session)
    return session


def commit_paths(paths: list[str], message: str, author: str) -> str:
    """Use an isolated index, then refresh only the selected real index entries."""
    if git("diff", "--cached", "--name-only", "--", *paths):
        raise ValueError("Selected files have staged changes; unstage them first")
    base = git("rev-parse", "HEAD")
    with tempfile.TemporaryDirectory(prefix="editorial-index-") as directory:
        env = os.environ.copy()
        env["GIT_INDEX_FILE"] = str(Path(directory) / "index")
        git("read-tree", base, env=env)
        git("add", "--", *paths, env=env)
        changed = set(git("diff", "--cached", "--name-only", env=env).splitlines())
        if not changed or not changed.issubset(paths):
            raise ValueError("Commit must contain changes only in selected files")
        git("commit", "-m", message + f"\n\nEditorial-Author: {author}", env=env)
    sha = git("rev-parse", "HEAD")
    actual = set(git("diff-tree", "--no-commit-id", "--name-only", "-r", sha).splitlines())
    if actual != changed:
        raise ValueError(f"Commit {sha} changed unexpected files; inspect before continuing")
    git("reset", "-q", "HEAD", "--", *paths)
    return sha


def repo_url() -> str:
    url = git("remote", "get-url", "origin")
    if url.startswith("git@github.com:"):
        url = "https://github.com/" + url.removeprefix("git@github.com:")
    if not url.startswith("https://github.com/"):
        raise ValueError("origin must be a GitHub repository URL for file diff links")
    return url.removesuffix(".git").rstrip("/")


def entry(session: dict, path: str, sha: str, action: str, summary: str, recorded_by: str) -> dict:
    url = repo_url()
    anchor = hashlib.sha256(path.encode()).hexdigest()
    return Record(
        event_id=f"{session['id']}:{path}", author=session["author"],
        role=session["role"], action=action, recorded_by=recorded_by,
        recorded_at=datetime.now(timezone.utc).isoformat(),
        base_commit=session["base_commit"], commit=sha, path=path,
        content_digest=digest((root() / path).read_text()),
        file_url=f"{url}/blob/{sha}/{quote(path, safe='/')}",
        diff_url=f"{url}/commit/{sha}#diff-{anchor}", summary=summary,
    ).model_dump()


def credit(text: str, author: str, role: str) -> str:
    _, _, data = split(text)
    authors = data.get("authors")
    if authors is None:
        authors = [data.get("author", "waylon")]
    if not isinstance(authors, list):
        raise ValueError("authors must be a list")
    authors = list(authors)
    if any(isinstance(a, dict) and a.get("id") == author and a.get("role", "").replace(" ", "-") == role for a in authors):
        return text
    authors.append({"id": author, "role": role.replace("-", " ")})
    return replace_fields(text, {"authors": authors})


def complete(session: dict, summary: str, recorded_by: str | None = None) -> dict:
    paths = list(session["posts"])
    if session["phase"] == "done":
        return session
    if not summary.strip():
        raise ValueError("Pass a nonempty --summary")
    repo_url()  # Validate links before creating a commit.
    if session["phase"] == "started":
        if git("rev-parse", "HEAD") != session["base_commit"]:
            raise ValueError("HEAD changed during the session; inspect and start a new session")
        actions = {}
        for path in paths:
            current = (root() / path).read_text()
            _, _, before = split(session["posts"][path]["before"])
            _, _, after = split(current)
            if before.get("editorial_history") != after.get("editorial_history"):
                raise ValueError(f"Session must preserve prior editorial history: {path}")
            action = "edited" if digest(current) != session["posts"][path]["digest"] else "reviewed"
            actions[path] = action
        for path in paths:
            destination = root() / path
            destination.write_text(credit(destination.read_text(), session["author"], session["role"]))
        if git("diff", "--name-only", "--", *paths):
            sha = commit_paths(paths, f"editorial: {session['role']} by {session['author']}", session["author"])
            session["commits"].append(sha)
        else:
            sha = session["base_commit"]
        session.update(phase="content_committed", content_commit=sha, actions=actions, summary=summary)
        save(session)
    if session["phase"] == "content_committed":
        clean(paths)
        pending = {}
        for path in paths:
            text = (root() / path).read_text()
            _, _, data = split(text)
            history = data.get("editorial_history", [])
            if not isinstance(history, list):
                raise ValueError(f"editorial_history must be a list: {path}")
            record = entry(session, path, session["content_commit"], session["actions"][path], session["summary"], recorded_by or session["author"])
            pending[path] = replace_fields(text, {"editorial_history": [*history, record]})
        session.update(phase="metadata_pending", pending=pending)
        save(session)
        for path, text in pending.items():
            (root() / path).write_text(text)
    if session["phase"] == "metadata_pending":
        for path, expected in session["pending"].items():
            if (root() / path).read_text() != expected:
                raise ValueError(f"Attribution interrupted or post changed: {path}. Restore the session's pending text before retrying")
        sha = commit_paths(paths, f"editorial: record {session['role']} revision links", recorded_by or session["author"])
        session["commits"].append(sha)
        session["phase"] = "done"
        save(session)
    return session


def emit(session: dict) -> None:
    typer.echo(json.dumps({"session": session["id"], "phase": session["phase"], "commits": session["commits"]}, indent=2))


@app.callback()
def main(version: Annotated[bool, typer.Option("--version", is_eager=True)] = False) -> None:
    if version:
        typer.echo("editorial 1.0.0")
        raise typer.Exit()
    os.chdir(root())


@app.command()
def start(
    posts: Annotated[list[Path], typer.Argument(help="Clean tracked posts to review or edit.")],
    author: Annotated[str, typer.Option(help="Actual agent/model ID, or human author ID.")],
    role: Annotated[Role, typer.Option()],
) -> None:
    """Capture a clean baseline. Save the printed session ID for finish."""
    emit(begin(list(dict.fromkeys(post_path(p) for p in posts)), author, role))


@app.command()
def finish(
    session: Annotated[str, typer.Option(help="Session ID printed by start.")],
    summary: Annotated[str, typer.Option(help="Describe the changes or unchanged review.")],
) -> None:
    """Commit selected edits, record exact revision links, and print all commits."""
    emit(complete(load(session), summary))


def candidates(role: Role) -> list[dict]:
    result = []
    for path in sorted((root() / "pages").rglob("*.md")):
        try:
            text = path.read_text()
            _, _, data = split(text)
            history = data.get("editorial_history", [])
            last = next((r for r in reversed(history) if r.get("role") == role), None)
            current = digest(text)
            status = "unreviewed" if last is None else "current" if last.get("digest_version") == "editorial-v1" and last.get("content_digest") == current else "stale"
            result.append({"path": path.relative_to(root()).as_posix(), "status": status, "last_commit": last.get("commit") if last else None})
        except (ValueError, yaml.YAMLError, AttributeError, TypeError) as error:
            typer.echo(f"Skipping {path}: {error}", err=True)
    return result


@app.command()
def queue(
    role: Annotated[Role, typer.Option()],
    json_output: Annotated[bool, typer.Option("--json")] = False,
    include_current: Annotated[bool, typer.Option("--include-current")] = False,
    limit: Annotated[int, typer.Option(min=1)] = 20,
) -> None:
    """List unreviewed and changed posts for one role."""
    rows = [r for r in candidates(role) if include_current or r["status"] != "current"][:limit]
    if json_output:
        typer.echo(json.dumps(rows, indent=2))
    else:
        for row in rows:
            typer.echo(f"{row['status']}\t{row['path']}")


@app.command()
def review(
    author: Annotated[str, typer.Option()],
    role: Annotated[Role, typer.Option()],
    agent_command: Annotated[str | None, typer.Option(help="Executable and arguments; review prompt is appended as one argument.")] = None,
    limit: Annotated[int, typer.Option(min=1)] = 1,
    no_input: Annotated[bool, typer.Option("--no-input")] = False,
) -> None:
    """Work through the queue with an agent command or an interactive review."""
    if agent_command is None and (no_input or not os.isatty(0)):
        raise ValueError("Pass --agent-command for noninteractive review, or use start/finish")
    rows = [r for r in candidates(role) if r["status"] != "current"]
    reviewed = 0
    for row in rows:
        path = row["path"]
        if git("status", "--porcelain", "--", path):
            typer.echo(f"Skipping dirty post: {path}", err=True)
            continue
        if reviewed >= limit:
            break
        if not agent_command:
            typer.echo((root() / path).read_text(), err=True)
            choice = typer.prompt("[r] record review, [e] open editor, [s] skip, [q] quit", err=True)
            if choice == "q":
                break
            if choice == "s":
                continue
            if choice not in {"r", "e"}:
                raise ValueError("Choose r, e, s, or q")
        session = begin([path], author, role)
        emit(session)
        if agent_command:
            prompt = (
                f"Read AGENTS.md and docs/editorial-workflow.md. Act as {role} on {path}. "
                f"Your author ID is {author}. Preserve the author's voice and prior history. "
                "Modify only this post. For internal links use existing relevant site posts. "
                "The calling script owns commits and attribution: leave your edits uncommitted. "
                f"Session: {session['id']}."
            )
            result = subprocess.run([*shlex.split(agent_command), prompt])
        elif choice == "e":
            result = subprocess.run([*shlex.split(os.environ.get("EDITOR", "vi")), path])
        else:
            result = None
        if result is not None and result.returncode:
            raise ValueError(f"Worker exited with {result.returncode}; inspect session {session['id']} before finish")
        summary = f"{role} review" if agent_command else typer.prompt("Review summary", err=True)
        emit(complete(session, summary))
        reviewed += 1


@app.command("record-commit")
def record_commit(
    posts: Annotated[list[Path], typer.Argument()],
    commit: Annotated[str, typer.Option(help="Existing edit commit touching these posts.")],
    author: Annotated[str, typer.Option()],
    role: Annotated[Role, typer.Option()],
    recorded_by: Annotated[str, typer.Option(help="Who is importing the existing attribution.")],
    summary: Annotated[str, typer.Option()],
) -> None:
    """Import an existing owned edit commit; selected posts must match that revision."""
    paths = list(dict.fromkeys(post_path(p) for p in posts))
    clean(paths)
    sha = git("rev-parse", f"{commit}^{{commit}}")
    changed = set(git("diff-tree", "--no-commit-id", "--name-only", "-r", sha).splitlines())
    if not set(paths).issubset(changed):
        raise ValueError("Each selected post must be changed by the supplied commit")
    for path in paths:
        committed = subprocess.run(["git", "show", f"{sha}:{path}"], capture_output=True, check=True).stdout.decode()
        if committed != (root() / path).read_text():
            raise ValueError(f"Post differs from supplied commit: {path}")
        _, _, data = split(committed)
        if not any(isinstance(a, dict) and a.get("id") == author for a in data.get("authors", [])):
            raise ValueError(f"Post must already credit {author}: {path}")
    session = begin(paths, author, role)
    session.update(phase="content_committed", base_commit=git("rev-parse", f"{sha}^"), content_commit=sha,
                   actions={p: "edited" for p in paths}, summary=summary, commits=[sha])
    save(session)
    emit(complete(session, summary, recorded_by))


if __name__ == "__main__":
    try:
        app()
    except (ValueError, OSError, yaml.YAMLError, subprocess.CalledProcessError) as error:
        typer.echo(f"Error: {error}", err=True)
        raise SystemExit(1)
