"""
Markata Plugin: Chart.js Renderer

This plugin converts Chart.js code blocks in Markdown files into rendered Chart.js charts.

# Installation

Ensure Chart.js is available in your site. If serving locally, add the script to your template:

```html
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("pre.chartjs").forEach((block, idx) => {
    try {
      const config = JSON.parse(block.textContent);
      const canvas = document.createElement("canvas");
      const wrapper = document.createElement("div");
      wrapper.className = "chartjs-wrapper";
      wrapper.appendChild(canvas);
      block.replaceWith(wrapper);
      new Chart(canvas.getContext("2d"), config);
    } catch (err) {
      console.error("Failed to render Chart.js chart", err);
    }
  });
});    </script>
```

# Configuration

Enable the plugin in `markata.toml`:

```toml
[markata]
hooks = ["markata.plugins.chartjs"]
```

# Usage

Use Chart.js code blocks in your Markdown content:

```markdown
``` chartjs
{
  "type": "bar",
  "data": {
    "labels": ["Red", "Blue"],
    "datasets": [{ "label": "Votes", "data": [12, 19] }]
  },
  "options": {
    "responsive": true
  }
}
```
```

# Notes

- Requires the Markata markdown-it-py backend with the `html` option enabled.
"""

from markata.hookspec import hook_impl
import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from markata import Markata

CHARTJS_BLOCK_RE = re.compile(r"```[\s]*chartjs\n(.*?)\n```", re.DOTALL)


@hook_impl
def pre_render(markata: "Markata") -> None:
    for article in markata.iter_articles("processing chartjs blocks"):
        if "chartjs" in article.content:
            article.content = CHARTJS_BLOCK_RE.sub(
                replace_chartjs_block, article.content
            )


def replace_chartjs_block(match: re.Match) -> str:
    chartjs_code = match.group(1).strip()
    chartjs_block = f'<pre class="chartjs">{chartjs_code}</pre>'
    return chartjs_block
