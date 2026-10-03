# GSC fixes

This batch fixes verified site configuration and migration issues from the
October 3 GSC review.  The changes are staged for review, without a commit or
deployment.

## Engine issues

- [#1507](https://github.com/WaylonWalker/markata-go/issues/1507): external URL
  embeds are consumed by attachment parsing and rewritten under `/static/`.
- [#1508](https://github.com/WaylonWalker/markata-go/issues/1508): redirect
  sources can overwrite generated articles and point to missing destinations.
- [#1509](https://github.com/WaylonWalker/markata-go/issues/1509): sitemaps
  advertise noindex generated pages and duplicate locations.
- [#1510](https://github.com/WaylonWalker/markata-go/issues/1510): sitemap index
  dates include excluded future posts, even for empty child sitemaps.
- [#1511](https://github.com/WaylonWalker/markata-go/issues/1511): lint does not
  detect likely bare-domain Markdown destinations such as `(pype.dev)`.
- [#1512](https://github.com/WaylonWalker/markata-go/issues/1512): config
  diagnostics should identify misplaced feed-format keys.
- [#1514](https://github.com/WaylonWalker/markata-go/issues/1514): explicit false
  format overrides are lost when the table has no enabled format.  This was
  reproduced while validating the site fixes.

Each issue includes reproduction steps, observed behavior, and verification
criteria.  Existing native redirect issue #1039 is now closed.  The alias rules
below use exact routes supported by HTML fallback and native redirect output.

## Canonical pages

Nine content files now have explicit hyphenated slugs matching existing
redirect destinations:

- `locked-diskcache`
- `kedro172-replit`
- `stories-10-10-2020-10-21-2020`
- `auto-conda-env`
- `bit-01`
- `dunder-rich`
- `copier-endops`
- `ansible-install-fonts`
- `ansible-install-if-not-callable`

Previously, the source filename generated an underscore route, then an old
redirect overwrote its article with a redirect to a nonexistent hyphen route.
The hyphen routes now contain the actual article output.  Existing underscore
redirects have valid destinations.

Publication, draft, private, and skip flags were preserved.  Three of these
posts are published; the other six retain their existing unpublished shadow
page behavior.  This batch does not publish those posts into public feeds.

## Migration aliases

Added 147 exact rules to `static/_redirects`:

| Alias type | Rules |
| --- | ---: |
| Old root tag routes | 92 |
| Legacy thought IDs 1000 through 1027 | 28 |
| Nested article, shot, and glossary routes | 17 |
| Tag synonyms and legacy tag prefix | 7 |
| Renamed TIL feed variants | 3 |

The destinations were checked against generated output.  Existing article
routes, configured feeds, and generated utility routes were excluded from
candidate root tag aliases.  In particular, `/steam` remains the Steam feed.

These rules restore paths such as `/blog/eight-years-cat/`,
`/thoughts-1016/`, and `/pygame/`, without relying on the ignored `/blog/*`
wildcard.  Tag aliases keep the existing noindex policy at their destination.
Out-of-range pagination and unverified cross-service URLs remain outside this
batch.

## Links and sitemaps

The thought-666 link now uses `https://pype.dev`, rather than the relative
destination `pype.dev` that produced `/thought-666/pype.dev`.

Moved seven misplaced sitemap exclusions into feed format tables and excluded
the redundant noindex `all` and `published` child sitemaps.  The nine affected
feeds are `all`, `steam`, `draft`, `family-shots`, `published`, `scheduled`,
`slashes`, `stars`, and `today`.

Every retained output format is explicit in those tables.  A table containing
only `sitemap=false` currently triggers default-format inheritance and enables
the sitemap again.  This workaround preserves HTML, simple HTML, RSS, Atom,
JSON, Markdown, and text output while the false-value bug is tracked in #1514.

The engine still lists noindex landing pages in `sitemap-pages.xml`, emits
future sitemap index modification dates, and produces malformed external
embed URLs.  Those remain tracked upstream rather than patched through local
output rewriting.

## Validation

- Config validation passed.
- Lint passed for all ten edited Markdown files.
- Full build passed with `v0.13.0-1-g3663c5d8`, using a temporary `just` recipe
  based on the repository build command and a fresh output directory.
- Validation disabled Searchcraft ingestion and external thoughts import.
  Existing local content was built with normal rendering and publishing.
- All 147 new aliases had generated redirect HTML and existing destinations;
  all returned HTTP 200 in a temporary local static-server check.
- All nine canonical pages contained article output and the expected absolute
  canonical URL, rather than redirect HTML.
- Source and built content-index publication flags matched the baseline.
- All nine excluded child sitemaps were absent from fresh output and from the
  root sitemap index.
- The corrected thought-666 external href appeared in generated HTML.
- The full build reported two unrelated tags-type warnings:
  `pages/link/bastardica.md` and `pages/post/bloatware-is-dying.md`.

Build artifacts, logs, alias inventory, issue bodies, and the validation
summary are under `/tmp/gsc-site-fixes-2026-10-03/`.  The original GSC exports,
review, and categorized inventory remain in the locally ignored `gsc/` folder.

The staged config patch excludes the pre-existing calendar-feed addition.
Pre-existing `.gitignore`, `pages/sample.md`, and other workspace changes were
left outside this staged batch.
