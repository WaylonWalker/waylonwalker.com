/*
 * Glossary Hovercards (Web Awesome, no manual wiring)
 * - Finds first occurrence of each glossary term (by slug) and wraps it.
 * - Appends a <wa-tooltip> per slug with hover/focus/click triggers.
 * - Keeps DOM clean: 1 trigger + 1 tooltip per slug, even with HTMX swaps.
 */
(() => {
  const DEFAULTS = {
    glossaryUrl: "/glossary.json",
    root: document,
    placement: "bottom-start",
    distance: 12,
  };

  const triggerIdFor = (slug) => `${slug}-gloss-item`;
  const tooltipIdFor = (slug) => `${slug}-gloss-popover`;
  const toTitle = (s) => s.replace(/\w\S*/g, w => w[0].toUpperCase() + w.slice(1));

  let _glossaryCache = null; // Map(termLower -> slug)

  function termRegex(term) {
    const escaped = term.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    return new RegExp(`(?<![A-Za-z0-9])(${escaped})(?![A-Za-z0-9])`, "i");
  }

  function wrapFirstMatchInElement(root, rx, makeEl) {
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode(node) {
        if (!node.nodeValue || !node.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
        const p = node.parentElement;
        if (!p) return NodeFilter.FILTER_REJECT;
        if (p.closest("a, code, pre, kbd, samp, button, textarea, .no-glossary, [contenteditable='true']")) {
          return NodeFilter.FILTER_REJECT;
        }
        return NodeFilter.FILTER_ACCEPT;
      }
    });

    let textNode;
    while ((textNode = walker.nextNode())) {
      const m = rx.exec(textNode.nodeValue);
      if (!m) continue;

      const before = textNode.nodeValue.slice(0, m.index);
      const match = textNode.nodeValue.slice(m.index, m.index + m[0].length);
      const after = textNode.nodeValue.slice(m.index + m[0].length);

      const frag = document.createDocumentFragment();
      if (before) frag.appendChild(document.createTextNode(before));

      const el = makeEl(match);
      frag.appendChild(el);

      if (after) frag.appendChild(document.createTextNode(after));

      textNode.parentNode.replaceChild(frag, textNode);
      return el; // one occurrence only
    }
    return null;
  }

  function buildtooltip(slug, opts) {
    const el = document.createElement('wa-tooltip');
    el.setAttribute('for', triggerIdFor(slug));
    el.setAttribute('id', tooltipIdFor(slug));
    el.setAttribute('placement', opts.placement);
    el.setAttribute('distance', String(opts.distance));
    el.setAttribute('trigger', 'hover focus'); // desktop + keyboard + mobile
    el.setAttribute('style', '--max-width:none;');

    el.innerHTML = `
      <div class="bg-black rounded-xl border-2 border-pink-500 overflow-hidden">
        <p class="p-3 text-gray-400 text-xs">glossary</p>
        <wa-include
          class="w-80 max-h-64 sm:w-96 sm:max-h-96 overflow-y-hidden text-white"
          src="/glossary/${slug}/partial">
        </wa-include>
      </div>
    `.trim();
    return el;
  }

  async function init(options = {}) {
    const opts = { ...DEFAULTS, ...options };
    const root = opts.root || document;

    if (!_glossaryCache) {
      try {
        const res = await fetch(opts.glossaryUrl, { credentials: 'same-origin' });
        const json = await res.json();
        const m = new Map();
        // normalize to Map(termLower -> slug)
        Object.entries(json).forEach(([k, v]) => m.set(String(k).toLowerCase().trim(), String(v).trim()));
        _glossaryCache = m;
      } catch (e) {
        console.warn('[glossary-hovercards] Failed to fetch glossary JSON:', e);
        return;
      }
    }

    // Avoid duplicating tooltips per slug
    const existingSlugs = new Set(
      Array.from(document.querySelectorAll('[id$="-gloss-item"]'))
        .map(el => el.id.replace(/-gloss-item$/, ''))
    );

    const TARGET_SELECTOR = 'p, blockquote, li, h1, h2, h3, h4, h5, h6';
    const blocks = Array.from(root.querySelectorAll(TARGET_SELECTOR));

    for (const [termLower, slug] of _glossaryCache.entries()) {
      if (existingSlugs.has(slug)) continue;

      const rx = termRegex(termLower);
      let insertedEl = null;

      for (const block of blocks) {
        insertedEl = wrapFirstMatchInElement(block, rx, (matchedText) => {
          const span = document.createElement('span');
          span.className = 'bg-pink-500 text-white px-1 rounded cursor-pointer';
          span.id = triggerIdFor(slug);
          span.textContent = matchedText; // preserve original casing
          span.tabIndex = 0;
          span.setAttribute('role', 'button');
          span.setAttribute('aria-haspopup', 'dialog');
          return span;
        });
        if (insertedEl) break;
      }

      if (!insertedEl) continue;

      // Append tooltip and move on
      document.body.appendChild(buildtooltip(slug, opts));
      existingSlugs.add(slug);
    }
  }

  // Public API
  window.GlossaryHovercards = { init };

  // Auto-init on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => init());
  } else {
    init();
  }

  // Re-scan swapped regions with HTMX (if present)
  document.addEventListener('htmx:afterSwap', (e) => {
    window.GlossaryHovercards.init({ root: e.target });
  });
})();
