---
date: 2025-01-12 11:18:25
templateKey: blog-post
title: one-shot-s3-cleanup
tags:
  - python
  - python
  - python
published: True

---

So I made a mistake in an app I am working on and ended up creating thumbnails
of thumbnails, and thumbnails of thumbnails of thumbnails... etc. I was able to
delete them all, but I wanted to make a one-shot script to do it.

![screenshot-2025-01-31T21-20-56-934Z.png](https://dropper.waylonwalker.com/api/file/e804dd2c-e3d9-4a83-83fa-95a720cdc92b.png)

## One Shot App

I got the idea of the one shot app from [Simon
Willison](https://simonwillison.net/2024/Dec/19/one-shot-python-tools/) and
replicated his setup in a chatgpt project

![screenshot-2025-01-12T18-16-57-443Z.png](https://dropper.waylonwalker.com/api/file/78d6eea9-29a2-43ed-b09e-1585762c991c.webp)

## Initial Prompt

``` txt
a mistake was made in my s3 bucket and I've created a bunch of extra files
write a script that deletes all files that contain _thumb_thumb

⬢ [devtainer] ❯ aws s3 ls s3://dropper
2024-12-29 14:32:32      16158 02271f4c-be18-4bea-b23e-d00f9fe42b9f.webp
2025-01-11 14:20:49       2878 02271f4c-be18-4bea-b23e-d00f9fe42b9f_thumb.webp
2025-01-11 14:21:17       2858 02271f4c-be18-4bea-b23e-d00f9fe42b9f_thumb_thumb.webp
2025-01-11 14:21:44       2856 02271f4c-be18-4bea-b23e-d00f9fe42b9f_thumb_thumb_thumb.webp
2025-01-11 14:21:44       2856 02271f4c-be18-4bea-b23e-d00f9fe42b9f_thumb_thumb_thumb_thumb.webp
2024-12-27 10:25:36       2812 06422c09-d0da-44ec-9339-786864ebccf2.webp
2025-01-11 14:20:49       2710 06422c09-d0da-44ec-9339-786864ebccf2_thumb.webp
2025-01-11 14:21:17       2652 06422c09-d0da-44ec-9339-786864ebccf2_thumb_thumb.webp
2025-01-11 14:21:45       2632 06422c09-d0da-44ec-9339-786864ebccf2_thumb_thumb_thumb.webp
2025-01-11 14:21:45       2632 06422c09-d0da-44ec-9339-786864ebccf2_thumb_thumb_thumb_thumb.webp
2024-12-29 20:44:14     146060 074edddb-8b46-4d94-9b55-d70a7bb74366.webp
2025-01-11 14:20:50      12476 074edddb-8b46-4d94-9b55-d70a7bb74366_thumb.webp
2025-01-11 14:21:17      12400 074edddb-8b46-4d94-9b55-d70a7bb74366_thumb_thumb.webp

create a typer application to do this job
include a --dry-run flag
make the search for _thumb_thumb editable
```

## s3_cleanup

Here is the result of the s3_cleanup script.  It ended up being 5 or 6 passes
to get everything I wanted with soft-delete enabled. Nice preview outputs in
the dry run.  This was 90% created by chatgpt 4o, with some slight hand edits
by me along the way.

``` python
#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "boto3",
#     "typer",
#     "rich"
# ]
# ///

import boto3
from datetime import datetime, timezone
from rich.console import Console
from rich.table import Table
import traceback
import typer

app = typer.Typer()
console = Console()

DEFAULT_SOFT_DELETE_DIR = "soft-delete/"


def human_readable_size(size: int) -> str:
    """Convert bytes to a human-readable format."""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} PB"


def calculate_file_age(last_modified: datetime) -> str:
    """Calculate the age of the file from the current time."""
    now = datetime.now(timezone.utc)
    age = now - last_modified
    days = age.days
    if days > 0:
        return f"{days} days"
    hours, remainder = divmod(age.seconds, 3600)
    minutes = remainder // 60
    if hours > 0:
        return f"{hours} hours"
    return f"{minutes} minutes"


@app.command()
def clean(
    bucket_name: str = typer.Argument(..., help="The name of the S3 bucket."),
    substring: str = typer.Argument(
        ..., help="The substring to search for in file names."
    ),
    dry_run: bool = typer.Option(
        False, help="If set, no files will be deleted; only listed."
    ),
    soft_delete: bool = typer.Option(
        False,
        help="If set, files will be moved to a soft delete directory instead of permanently deleted.",
    ),
    soft_delete_dir: str = typer.Option(
        DEFAULT_SOFT_DELETE_DIR, help="The directory to move soft-deleted files to."
    ),
    max_age: int = typer.Option(None, help="Maximum age of files to include, in days."),
    min_age: int = typer.Option(None, help="Minimum age of files to include, in days."),
):
    """Delete or soft-delete files in an S3 bucket that contain a specific substring in their names."""
    s3 = boto3.client("s3")

    try:
        # List all objects in the bucket
        response = s3.list_objects_v2(Bucket=bucket_name)

        if "Contents" not in response:
            console.print("[bold yellow]No files found in the bucket.[/bold yellow]")
            return

        now = datetime.now(timezone.utc)

        def file_within_age_range(obj):
            file_age = (now - obj["LastModified"]).days
            if max_age is not None and file_age > max_age:
                return False
            if min_age is not None and file_age < min_age:
                return False
            return True

        files_to_process = [
            obj
            for obj in response["Contents"]
            if substring in obj["Key"] and file_within_age_range(obj)
        ]

        if not files_to_process:
            console.print(
                "[bold yellow]No files matching criteria found in the bucket.[/bold yellow]"
            )
            return

        if dry_run:
            console.print(
                "[bold blue]Dry run mode: The following files would be processed:[/bold blue]"
            )
            table = Table(title="Files to be Processed")
            table.add_column("File Name", style="cyan", no_wrap=True)
            table.add_column("Size", style="magenta", justify="right")
            table.add_column("Age", style="green", justify="right")
            table.add_column("Action", style="yellow", no_wrap=True)

            total_size = 0
            for obj in files_to_process:
                human_size = human_readable_size(obj["Size"])
                file_age = calculate_file_age(obj["LastModified"])
                action = (
                    f"[bold yellow]-> {soft_delete_dir}{obj['Key']}[/bold yellow]"
                    if soft_delete
                    else "[bold red]DELETE[/bold red]"
                )
                table.add_row(obj["Key"], human_size, file_age, action)
                total_size += obj["Size"]

            console.print(table)
            console.print(
                f"\n[bold green]Summary:[/bold green] {len(files_to_process)} files, Total Size: {human_readable_size(total_size)}, Operation: {'Soft Delete' if soft_delete else 'Delete'}"
            )

        else:
            for obj in files_to_process:
                file_key = obj["Key"]
                if soft_delete:
                    copy_source = {"Bucket": bucket_name, "Key": file_key}
                    new_key = f"{soft_delete_dir}{file_key}"
                    s3.copy_object(
                        CopySource=copy_source, Bucket=bucket_name, Key=new_key
                    )
                    s3.delete_object(Bucket=bucket_name, Key=file_key)
                    console.print(
                        f"[bold yellow]Moved to soft-delete:[/bold yellow] {file_key} -> {new_key}"
                    )
                else:
                    s3.delete_object(Bucket=bucket_name, Key=file_key)
                    console.print(f"[bold red]Deleted:[/bold red] {file_key}")

            console.print(
                f"[bold green]Operation completed. {len(files_to_process)} files processed. Operation: {'Soft Delete' if soft_delete else 'Delete'}[/bold green]"
            )

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}", style="red")


@app.command()
def clear_soft_delete(
    bucket_name: str = typer.Argument(..., help="The name of the S3 bucket."),
    soft_delete_dir: str = typer.Option(
        DEFAULT_SOFT_DELETE_DIR, help="The soft delete directory to clear."
    ),
    dry_run: bool = typer.Option(
        False, help="If set, no files will be deleted; only listed."
    ),
):
    """Remove all files in the soft delete directory."""
    s3 = boto3.client("s3")

    try:
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=soft_delete_dir)

        if "Contents" not in response:
            console.print(
                f"[bold yellow]No files found in the soft delete directory '{soft_delete_dir}'.[/bold yellow]"
            )
            return

        files_to_delete = [obj for obj in response["Contents"]]

        if dry_run:
            console.print(
                "[bold blue]Dry run mode: The following files would be deleted from the soft delete directory:[/bold blue]"
            )
            table = Table(title="Files to be Deleted")
            table.add_column("File Name", style="cyan", no_wrap=True)
            table.add_column("Size", style="magenta", justify="right")
            total_size = 0

            for obj in files_to_delete:
                human_size = human_readable_size(obj["Size"])
                table.add_row(obj["Key"], human_size)
                total_size += obj["Size"]

            console.print(table)
            console.print(
                f"\n[bold green]Summary:[/bold green] {len(files_to_delete)} files, Total Size: {human_readable_size(total_size)}"
            )
        else:
            for file_key in files_to_delete:
                file_key = file_key["Key"]
                s3.delete_object(Bucket=bucket_name, Key=file_key)
                console.print(
                    f"[bold red]Deleted from soft-delete:[/bold red] {file_key}"
                )

            console.print(
                f"[bold green]Soft delete directory '{soft_delete_dir}' cleared. {len(files_to_delete)} files removed.[/bold green]"
            )

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}", style="red")
        console.print("[bold red]Operation failed.[/bold red]")

        console.print(traceback.format_exc())


@app.command()
def undo_soft_delete(
    bucket_name: str = typer.Argument(..., help="The name of the S3 bucket."),
    soft_delete_dir: str = typer.Option(
        DEFAULT_SOFT_DELETE_DIR, help="The soft delete directory to restore from."
    ),
    dry_run: bool = typer.Option(
        False, help="If set, no files will be restored; only listed."
    ),
):
    """Restore all files from the soft delete directory to their original locations."""
    s3 = boto3.client("s3")

    try:
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=soft_delete_dir)

        if "Contents" not in response:
            console.print(
                f"[bold yellow]No files found in the soft delete directory '{soft_delete_dir}'.[/bold yellow]"
            )
            return

        files_to_restore = [obj for obj in response["Contents"]]

        if dry_run:
            console.print(
                "[bold blue]Dry run mode: The following files would be restored:[/bold blue]"
            )
            table = Table(title="Files to be Restored")
            table.add_column("File Name", style="cyan", no_wrap=True)
            table.add_column("Size", style="magenta", justify="right")
            table.add_column("Original Location", style="green", no_wrap=True)
            total_size = 0

            for obj in files_to_restore:
                human_size = human_readable_size(obj["Size"])
                original_key = obj["Key"][len(soft_delete_dir) :]
                table.add_row(obj["Key"], human_size, original_key)
                total_size += obj["Size"]

            console.print(table)
            console.print(
                f"\n[bold green]Summary:[/bold green] {len(files_to_restore)} files, Total Size: {human_readable_size(total_size)}"
            )
        else:
            for obj in files_to_restore:
                file_key = obj["Key"]
                original_key = file_key[
                    len(soft_delete_dir) :
                ]  # Remove the soft delete prefix
                copy_source = {"Bucket": bucket_name, "Key": file_key}
                s3.copy_object(
                    CopySource=copy_source, Bucket=bucket_name, Key=original_key
                )
                s3.delete_object(Bucket=bucket_name, Key=file_key)
                console.print(
                    f"[bold green]Restored:[/bold green] {file_key} -> {original_key}"
                )

            console.print(
                f"[bold green]Restoration completed. {len(files_to_restore)} files restored.[/bold green]"
            )

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}", style="red")


if __name__ == "__main__":
    app()
```

## full help text output

Here is the help text for all of the commands in the script.

``` bash
dropper on  main [!?] is 📦 v1.0.0 via  v22.13.0  v3.11.10 on  (us-east-1)  NO PYTHON VENV SET took 7s
⬢ [devtainer] ❯ ./scripts/s3_cleanup.py --help

 Usage: s3_cleanup.py [OPTIONS] COMMAND [ARGS]...

╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                         │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.  │
│ --help                        Show this message and exit.                                                       │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ clean               Delete or soft-delete files in an S3 bucket that contain a specific substring in their      │
│                     names.                                                                                      │
│ clear-soft-delete   Remove all files in the soft delete directory.                                              │
│ undo-soft-delete    Restore all files from the soft delete directory to their original locations.               │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

⬢ [devtainer] ❯ ./scripts/s3_cleanup.py clean --help

 Usage: s3_cleanup.py clean [OPTIONS] BUCKET_NAME SUBSTRING

 Delete or soft-delete files in an S3 bucket that contain a specific substring in their names.

╭─ Arguments ─────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    bucket_name      TEXT  The name of the S3 bucket. [default: None] [required]                               │
│ *    substring        TEXT  The substring to search for in file names. [default: None] [required]               │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --dry-run            --no-dry-run                 If set, no files will be deleted; only listed.                │
│                                                   [default: no-dry-run]                                         │
│ --soft-delete        --no-soft-delete             If set, files will be moved to a soft delete directory        │
│                                                   instead of permanently deleted.                               │
│                                                   [default: no-soft-delete]                                     │
│ --soft-delete-dir                        TEXT     The directory to move soft-deleted files to.                  │
│                                                   [default: soft-delete/]                                       │
│ --max-age                                INTEGER  Maximum age of files to include, in days. [default: None]     │
│ --min-age                                INTEGER  Minimum age of files to include, in days. [default: None]     │
│ --help                                            Show this message and exit.                                   │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

⬢ [devtainer] ❯ ./scripts/s3_cleanup.py clear-soft-delete --help

 Usage: s3_cleanup.py clear-soft-delete [OPTIONS] BUCKET_NAME

 Remove all files in the soft delete directory.

╭─ Arguments ─────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    bucket_name      TEXT  The name of the S3 bucket. [default: None] [required]                               │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --soft-delete-dir                    TEXT  The soft delete directory to clear. [default: soft-delete/]          │
│ --dry-run            --no-dry-run          If set, no files will be deleted; only listed. [default: no-dry-run] │
│ --help                                     Show this message and exit.                                          │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

⬢ [devtainer] ❯ ./scripts/s3_cleanup.py undo-soft-delete --help

 Usage: s3_cleanup.py undo-soft-delete [OPTIONS] BUCKET_NAME

 Restore all files from the soft delete directory to their original locations.

╭─ Arguments ─────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    bucket_name      TEXT  The name of the S3 bucket. [default: None] [required]                               │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --soft-delete-dir                    TEXT  The soft delete directory to restore from. [default: soft-delete/]   │
│ --dry-run            --no-dry-run          If set, no files will be restored; only listed.                      │
│                                            [default: no-dry-run]                                                │
│ --help                                     Show this message and exit.                                          │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```
