---
title: '💭 Lazy self-installing Python scripts with uv'
date: 2024-12-24T03:20:33
templateKey: link
link: https://treyhunner.com/2024/12/lazy-self-installing-python-scripts-with-uv/
tags:
  - python
  - uv
published: true

---

> I really like Trey's steps to making an executable python script with uv

his old process seems to be the same with a new shebang

> 1. Add an appropriate shebang line above the first line in the file (e.g. #!/usr/bin/env python3)
> 2. Aet an executable bit on the file (chmod a+x my_script.py)
> 3. Place the script in a directory that’s in my shell’s PATH variable (e.g. cp my_script.py ~/bin/my_script)


And here is the new format the the shebang followed by the metadata comment block defined in PEP 723.

``` bash
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "ffmpeg-normalize",
# ]
# ///
```


[Original thought](https://treyhunner.com/2024/12/lazy-self-installing-python-scripts-with-uv/)
