/*
 * Glossary Hovercards (HTMX + Tippy.js, no manual wiring)
 * - Finds first occurrence of each glossary term (by slug) and wraps it.
 * - Creates exactly 1 trigger + 1 tooltip template per slug (keeps DOM clean).
 * - Uses HTMX to fetch /glossary/{slug}/partial into the tooltip on first show.
 * - Re-scans on HTMX swaps.
 */
(() => {
  const DEFAULTS = {
    glossaryUrl: "/glossary.json",
    root: document,
    placement: "bottom-start",
    distance: 12,                 // pixels; applied via Popper offset
    themeClass: "my-4 text-lg",
    // "bg-black rounded-xl border-2 border-pink-500 overflow-hidden text-white",
    triggerClass:
      "bg-pink-500 text-white px-1 rounded cursor-pointer",
    maxWidth: null,               // null = no limit (tippy 'maxWidth: "none"')
    preload: false,               // if true, load partial at init (not just on show)
  };

  const triggerIdFor = (slug) => `${slug}-gloss-item`;
  const templateIdFor = (slug) => `${slug}-gloss-template`;

  let _glossaryCache = null; // Map(termLower -> slug)
  const _instances = new Map(); // slug -> tippy instance

  const toTitle = (s) => s.replace(/\w\S*/g, w => w[0].toUpperCase() + w.slice(1));

  function termRegex(term) {
    const escaped = term.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    // avoid matching inside words
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
      return el; // only first occurrence
    }
    return null;
  }

  function ensureTemplate(slug, opts) {
    // Create a hidden container used as the tooltip content source
    const existing = document.getElementById(templateIdFor(slug));
    if (existing) return existing;

    const tpl = document.createElement("div");
    tpl.id = templateIdFor(slug);
    tpl.className = "hidden";
    tpl.innerHTML = `
      <div class="${opts.themeClass}">
        <p class="p-4 text-gray-400 text-xs">
            <span class="font-bold font-yellow-500">${toTitle(slug)}</span>
          glossary
        </p>
        <div class="w-80 max-h-64 sm:w-96 sm:max-h-96 overflow-y-auto">
          <div
            class="flex items-center justify-center text-gray-400 text-xs p-4"
            hx-get="/glossary/${slug}/partial/"
            hx-trigger="every 0.1s"
            hx-target="this"
            hx-swap="outerHTML">
            loading...
          </div>
        </div>
      </div>
    `.trim();

    document.body.appendChild(tpl);
    return tpl;
  }

  function createTippyFor(trigger, slug, opts) {
    if (_instances.has(slug)) return _instances.get(slug);

    const tpl = ensureTemplate(slug, opts);

    const instance = tippy(trigger, {
      theme: 'waylon',
      allowHTML: true,
      arrow: false,
      placement: opts.placement,
      interactive: true,
      maxWidth: opts.maxWidth === null ? 'none' : opts.maxWidth,
      animation: 'scale', // subtle default; can remove
      appendTo: () => document.body,
      offset: [0, opts.distance],
      // Lazy set content on show so the HTMX 'revealed' trigger can fire
      onShow(inst) {
        const html = tpl.innerHTML;
        inst.setContent(html);
        // If we aren't preloading, force HTMX to process the injected nodes so
        // the 'revealed' trigger will load the partial.
        if (!opts.preload && window.htmx) {
          // Process just the popper content area
          const tip = inst.popper.querySelector('.tippy-content');
          if (tip) window.htmx.process(tip);
        }
      },
    });

    _instances.set(slug, instance);
    return instance;
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
        Object.entries(json).forEach(([k, v]) =>
          m.set(String(k).toLowerCase().trim(), String(v).trim())
        );
        _glossaryCache = m;
      } catch (e) {
        console.warn('[glossary-hovercards] Failed to fetch glossary JSON:', e);
        return;
      }
    }

    // Avoid duplicate triggers per slug that already exist on the page
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
          span.className = opts.triggerClass;
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

      // Initialize Tippy for this trigger
      createTippyFor(insertedEl, slug, opts);
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


