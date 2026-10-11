# Editorial workflow

Each post credits contributors in `authors` and records their work in
`editorial_history`.  Use `copy-editor` for spelling, grammar, and clarity.
Use `internal-link-editor` for relevant links between existing posts.

## Agent sessions

Start with clean selected posts.  Identify the actual model or person with a
stable author ID.  Work exclusively on the selected posts during the session.
The session manifest lives in `.git/editorial/`, outside published content.

```bash
uv run scripts/editorial.py queue --role copy-editor --json
uv run scripts/editorial.py start pages/blog/example.md \
  --author gpt-6-luna --role copy-editor
# Review or edit the post, then use the session UUID printed above.
uv run scripts/editorial.py finish --session SESSION_UUID \
  --summary 'Corrected spelling and grammar.'
```

`finish` preserves prior history, adds contributor credit, commits the selected
files, then appends history with the edit commit's full SHA and file links.
It prints a JSON report containing every resulting commit.  An unchanged
review is recorded as `reviewed`; a changed content digest is `edited`.
Git's committer remains the configured operator.  The `Editorial-Author`
commit trailer and frontmatter identify the contributor explicitly.

A commit cannot contain its own final SHA.  The attribution commit points to
the preceding content commit.  Report both commits to the user.  For a review
that already has contributor credit, only the attribution commit is needed.

The script uses a temporary index to commit selected files.  Unrelated staged
and unstaged changes stay outside its commits.  Selected staged files are
rejected.  Starting on a dirty selected post is rejected because the script
cannot infer who owns individual changes.  Keep other writers away from the
selected files until the session finishes.  Existing repository hooks run.

## Review queue

Start an interactive review with:

```bash
uv run scripts/editorial.py review --author waylon --role copy-editor --limit 5
```

The script displays each post and offers review, edit with `$EDITOR`, skip,
or quit.  Dirty posts are skipped.  The default limit is one post.

To use an agent, pass its executable and arguments with `--agent-command`.
The script appends a review prompt as one final argument.  Use a command
that accepts a prompt in that position, for example:

```bash
uv run scripts/editorial.py review --author ACTUAL_MODEL_ID \
  --role internal-link-editor --agent-command 'codex exec' --limit 5 --no-input
```

Select the model in the worker's own CLI configuration and make the author ID
match it.  The script supplies the role, post, and session to the worker.
The worker leaves edits uncommitted; the calling script owns both commits.
A successful worker exit is its declaration that the review is complete,
even when it made no changes.  A failed worker leaves a session for inspection.
The script does not verify editorial judgment or the worker's actual model.

For agents operating directly in this repository, use `start` and `finish`.
Read the post, perform the assigned role, then finish and report all SHAs.
Copy editors preserve voice, meaning, technical claims, and personal details.
Internal link editors add useful links to existing posts, using established
site link syntax.  Both roles preserve previous authors and history.

## Revision data

Each history entry has this versioned shape:

```yaml
editorial_history:
  - schema_version: 1
    event_id: '<session UUID>:pages/blog/example.md'
    author: gpt-6-luna
    role: copy-editor
    action: edited
    recorded_by: gpt-6-luna
    recorded_at: '2026-10-11T15:00:00+00:00'
    base_commit: '<full pre-edit commit SHA>'
    commit: '<full content commit SHA>'
    path: pages/blog/example.md
    content_digest: 'sha256:<hex digest>'
    digest_version: editorial-v1
    file_url: 'https://github.com/OWNER/REPO/blob/SHA/pages/blog/example.md'
    diff_url: 'https://github.com/OWNER/REPO/commit/SHA#diff-<path hash>'
    summary: Corrected spelling and grammar.
```

`file_url` targets the exact file at that revision.  `diff_url` targets that
file's diff in the edit commit.  GitHub's file diff anchor is the SHA-256 of
the UTF-8 repository-relative path.  Paths in blob URLs are percent encoded.
These links work remotely once the commits have been pushed.

`recorded_at` is the attribution timestamp, not an invented edit timestamp.
`recorded_by` distinguishes the contributor from an agent importing old work.
`base_commit` and `commit`, together with `path`, also allow a future renderer
to retrieve the before and after versions directly from Git.  Multiple posts
may share an edit commit; each record targets its own file.  History retains
separate events for repeated work by the same contributor.

For `editorial-v1`, parse YAML frontmatter, remove only `authors` and
`editorial_history`, serialize the remaining mapping using Python's
`json.dumps(sort_keys=True, ensure_ascii=False, default=str)` with its default
separators, append a newline, then append the Markdown body after the closing
frontmatter delimiter.  Hash those UTF-8 bytes with SHA-256.  Python date and
datetime values use their `str()` representations.  Files are read with
Python's universal newline handling.  YAML formatting changes alone do not
invalidate a review; body whitespace and ordinary metadata changes do.
A future markata-go implementation must match this normalization or introduce
a new digest version.

The latest event for each role determines freshness.  A matching digest means
`current`; a different or unknown digest version means `stale`; no matching
role means `unreviewed`.  Attribution alone does not make a review stale.
A change later reverted to the reviewed content becomes current again.
Malformed posts are skipped with a diagnostic during queue discovery.

## Import existing edits

First establish ownership of the selected diffs with the user, then commit
only those owned changes.  Import the existing edit commit with:

```bash
uv run scripts/editorial.py record-commit pages/blog/example.md \
  --commit EDIT_SHA --author gpt-6-luna --role copy-editor \
  --recorded-by ACTUAL_IMPORTER_ID --summary 'Imported existing copy edits.'
```

Selected posts must be clean, already credit the contributor, and match the
supplied commit exactly.  The command creates an attribution commit and
reports both the supplied edit commit and the new commit.

## Interrupted sessions

`finish` saves phases and pending attribution text under `.git/editorial/`.
If a commit hook fails, fix the cause and retry the same session.  Inspect
Git history first if the process was killed while Git was committing: an
abrupt interruption between a Git commit and manifest save requires manual
reconciliation.  The manifest contains the baseline, content commit, pending
text, and commit report.  Preserve it until the session is reconciled.

The tool refuses changed pending attribution text rather than overwriting it.
There is no automatic rollback of completed commits.  Treat sessions as
exclusive operations in one checkout; use separate worktrees for concurrent
editorial work.  Frontmatter is an audit trail backed by Git, not a tamper
proof signature.  Rendering author-specific changes belongs in markata-go
later.
