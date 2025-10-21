// Template vars
const populate_search_input = false
const search_hotkey = '/'
const didyoumean_url = '/didyoumean.json'

// Elements
const searchInput = document.getElementById('search');
const resultsEl = document.getElementById('didyoumean_results');

// Optional: prefill with current path, but DO NOT fetch results yet
let currentPath = '';
if (populate_search_input) {
  currentPath = window.location.pathname.replace(/^\/|\/$/g, '');
  searchInput.value = currentPath;
}

// State
let pages = null;                 // will hold JSON once loaded
let loaded = false;               // one-time loader guard
let debounceTimeout = null;

// Light placeholder
const showEmpty = () => {
  resultsEl.innerHTML = '<li class="text-gray-500 col-span-full text-center py-8">Start typing to search…</li>';
};
const showLoading = () => {
  resultsEl.innerHTML = '<li class="text-gray-400 col-span-full text-center py-8 animate-pulse">Loading suggestions…</li>';
};
const showError = (msg = 'Could not load suggestions.') => {
  resultsEl.innerHTML = `<li class="text-red-400 col-span-full text-center py-8">${msg}</li>`;
};

// Initial placeholder
showEmpty();

// Lazy loader (runs once)
async function ensureLoaded() {
  if (loaded) return;
  loaded = true;
  try {
    showLoading();
    const resp = await fetch(didyoumean_url, { credentials: 'same-origin', cache: 'force-cache' });
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    pages = await resp.json();
    // If we prefilled with currentPath, only render after first interaction;
    // but if the input already contains non-empty text (e.g., hotkey put focus and user typed),
    // we render immediately from the input handler below.
    // To avoid a blank state after load (before the first input arrives), keep placeholder:
    showEmpty();
  } catch (err) {
    console.error('didyoumean load failed:', err);
    showError();
  }
}

// Scoring/search (unchanged logic, wrapped so it only exists after load)
function searchObject(needle, obj) {
  needle = needle.toLowerCase();
  let score = 0;

  const searchField = (value) => {
    if (!value) return 0;
    value = String(value).toLowerCase();

    if (value === needle) return 15;
    if (value.match(new RegExp(`\\b${needle}\\b`))) return 10;
    if (value.includes(needle)) return 8;

    const needleParts = needle.split(/\W+/).filter(p => p.length > 2);
    const valueParts = value.split(/\W+/).filter(p => p.length > 2);
    if (needleParts.length === 0) return 0;

    let matchCount = 0;
    for (const part of needleParts) {
      for (const valuePart of valueParts) {
        if (valuePart.includes(part) || part.includes(valuePart)) { matchCount++; break; }
      }
    }
    const matchRatio = matchCount / needleParts.length;
    if (matchRatio >= 0.75) return matchRatio * 6;
    return 0;
  };

  const slugScore = searchField(obj.slug) * 3;
  const titleScore = searchField(obj.title) * 2;
  const descScore = searchField(obj.description) * 1;
  const tagScore = (obj.tags || []).reduce((sum, tag) => sum + searchField(tag), 0);

  score = slugScore + titleScore + descScore + tagScore;

  if (score > 0 && obj.slug) {
    const inputParts = needle.split('/').filter(p => p.length > 0);
    const slugParts = obj.slug.toLowerCase().split('/');
    for (let i = 0; i < inputParts.length && i < slugParts.length; i++) {
      if (slugParts[i].includes(inputParts[i])) score += 5;
    }
  }
  return score;
}

function findSimilar(input) {
  if (!pages || !input || input.length < 2) return [];
  const normalizedInput = input.toLowerCase().trim();
  const scored = pages.map(page => ({ ...page, score: searchObject(normalizedInput, page) }));
  return scored
    .sort((a, b) => b.score - a.score)
    .slice(0, 12)
    .filter(item => item.score > 15);
}

function updateResults(results) {
  if (!results || results.length === 0) {
    resultsEl.innerHTML = '<p class="text-gray-500 col-span-full text-center py-8">No similar pages found.</p>';
    return;
  }
  const html = results.map(page => `
      <li class="p-4 bg-gray-800 rounded-lg hover:shadow-lg transition-shadow first:mt-4">
        <a href="/${page.slug}" class="block">
          <h3 class="text-lg font-semibold text-pink-400 hover:text-pink-300 mb-2">
            ${page.title || page.slug}
          </h3>
          ${page.description ? `
            <p class="text-sm text-gray-300 mb-3 line-clamp-2">
              ${page.description}
            </p>` : ''}
          ${page.tags && page.tags.length ? `
            <div class="mt-3 flex flex-wrap gap-2">
              ${page.tags.map(tag => `<span class="px-2 py-1 bg-gray-700 rounded text-xs">${tag}</span>`).join('')}
            </div>` : ''}
        </a>
      </li>
    `).join('');
  resultsEl.innerHTML = html;
}

// Debounced input handler (loads on demand)
function handleInputNow(val) {
  if (!pages) { showLoading(); return; }
  const results = findSimilar(val);
  updateResults(results);
}
function onInput(e) {
  clearTimeout(debounceTimeout);
  const val = e.target.value;
  debounceTimeout = setTimeout(() => handleInputNow(val), 120);
}

// One-time bootstrap on first interaction with the input
function primeAndMaybeSearch(e) {
  ensureLoaded().then(() => {
    // If we prefilled and user is now interacting, show initial results for the current path
    if (populate_search_input && searchInput.value && !resultsEl.dataset.initialized) {
      resultsEl.dataset.initialized = '1';
      handleInputNow(searchInput.value);
    }
  });
}

// Hook interactions that should trigger the lazy load
['focus', 'click', 'keydown'].forEach(ev =>
  searchInput.addEventListener(ev, primeAndMaybeSearch, { once: true })
);

// Regular input updates (after load, this will render; before load, it will show "loading")
searchInput.addEventListener('input', (e) => {
  // If the user starts typing before we loaded, kick off load immediately
  if (!loaded) ensureLoaded();
  onInput(e);
});

// Hotkey support (focuses input; also triggers lazy load)
if (search_hotkey) {
  document.addEventListener('keydown', (e) => {
    // ignore when typing in inputs/textareas
    const t = e.target;
    if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.isContentEditable)) return;

    if (e.key === search_hotkey) {
      e.preventDefault();
      searchInput.focus();
      searchInput.select();
      ensureLoaded();
    }
  });
}

