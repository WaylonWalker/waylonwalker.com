// Production-only visual acceptance for the winding road in site history.
// No edits, logins, or deploys; screenshots and geometry are retained as CI artifacts.
import { chromium } from "playwright";
import { mkdir, writeFile, appendFile } from "node:fs/promises";

const url = "https://waylonwalker.com/a-little-site-history/";
const widths = [320, 360, 390, 768, 1440];
const outputDir = "artifacts/road-layout";
await mkdir(outputDir, { recursive: true });
const browser = await chromium.launch({ headless: true });
const results = [];

try {
  for (const width of widths) {
    const page = await browser.newPage({
      viewport: { width, height: 900 },
      deviceScaleFactor: 1,
      reducedMotion: "reduce",
      colorScheme: width === 390 ? "dark" : "light",
    });
    const result = { width, url, errors: [] };
    try {
      const response = await page.goto(url, { waitUntil: "domcontentloaded", timeout: 45000 });
      result.httpStatus = response?.status() ?? null;
      if (!response?.ok()) throw new Error(`HTTP ${result.httpStatus} loading production page`);
      await page.evaluate(() => document.fonts?.ready);
      await page.waitForFunction(
        () => document.querySelectorAll('.road[data-road-ready] .road-card').length > 0,
        undefined,
        { timeout: 25000 },
      );
      await page.waitForTimeout(350);
      const geometry = await page.evaluate(() => {
        const roots = [...document.querySelectorAll('.road[data-road-ready]')];
        const round = (value) => Math.round(value * 10) / 10;
        const rect = (el) => {
          const box = el.getBoundingClientRect();
          return { left: round(box.left), top: round(box.top), right: round(box.right), bottom: round(box.bottom) };
        };
        return roots.map((root) => {
          const cards = [...root.querySelectorAll(".road-card")].map(rect);
          const anchors = [...root.querySelectorAll(".road-point")];
          const inner = root.querySelector(".road-inner");
          let following = root.nextElementSibling;
          while (following && (["SCRIPT", "STYLE"].includes(following.tagName) || !following.getClientRects().length)) {
            following = following.nextElementSibling;
          }
          const violations = [];
          if (!inner || cards.length === 0) violations.push("road has no rendered cards");
          if (!following) violations.push("cannot identify following article content");
          for (let i = 0; i < cards.length; i++) {
            const a = cards[i];
            if (a.left < -2 || a.right > innerWidth + 2) {
              violations.push(`card ${i} extends outside viewport`);
            }
            if (following && a.bottom > following.getBoundingClientRect().top - 1) {
              violations.push(`card ${i} overlaps following ${following.tagName}`);
            }
            for (let j = i + 1; j < cards.length; j++) {
              const b = cards[j];
              const overlapW = Math.min(a.right, b.right) - Math.max(a.left, b.left);
              const overlapH = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top);
              if (overlapW > 2 && overlapH > 2) {
                violations.push(`cards ${i} and ${j} overlap by ${round(overlapW)}x${round(overlapH)}px`);
              }
            }
          }
          anchors.forEach((anchor, i) => {
            if (getComputedStyle(anchor).position !== "absolute") {
              violations.push(`milestone anchor ${i} participates in document flow`);
            }
          });
          return {
            style: root.dataset.road,
            cardCount: cards.length,
            root: rect(root),
            inner: inner ? rect(inner) : null,
            followingTag: following?.tagName ?? null,
            following: following ? rect(following) : null,
            cards,
            violations,
          };
        });
      });
      result.roads = geometry;
      if (!geometry.length) result.errors.push("no initialized road found");
      for (const road of geometry) result.errors.push(...road.violations);
    } catch (error) {
      result.errors.push(String(error?.message || error));
    }
    try {
      await page.screenshot({ path: `${outputDir}/road-${width}.png`, fullPage: true, timeout: 30000 });
    } catch (error) {
      result.errors.push(`screenshot: ${String(error?.message || error)}`);
    }
    results.push(result);
    console.log(JSON.stringify({ width, status: result.httpStatus, roads: result.roads?.length || 0, errors: result.errors }));
    await page.close();
  }
} finally {
  await browser.close();
}

await writeFile(`${outputDir}/geometry.json`, JSON.stringify(results, null, 2) + "\n");
const failed = results.filter((r) => r.errors.length);
const summary = [
  "## Production road geometry (not deployment verification)",
  "",
  "| Viewport | HTTP | Road cards | Result |",
  "| --- | --- | ---: | --- |",
  ...results.map((r) => `| ${r.width}px | ${r.httpStatus ?? "—"} | ${r.roads?.[0]?.cardCount ?? 0} | ${r.errors.length ? r.errors.join("; ") : "PASS"} |`),
  "",
  "Screenshots and measured card/following-content bounds are in the road-layout artifact.",
  "",
].join("\n");
console.log(summary);
if (process.env.GITHUB_STEP_SUMMARY) await appendFile(process.env.GITHUB_STEP_SUMMARY, summary);
if (failed.length) process.exitCode = 1;
