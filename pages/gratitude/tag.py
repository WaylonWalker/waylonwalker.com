from pathlib import Path

files = Path(__file__).parent.glob("*.md")

for file in files:
    text = file.read_text()
    lines = text.splitlines()

    # find line that starts with title:  and append newline after it
    for i, line in enumerate(lines):
        if line.startswith("title:"):
            lines.insert(i, "tags:\n  - gratitude\n")
            break
    lines.append("")

    file.write_text("\n".join(lines))
