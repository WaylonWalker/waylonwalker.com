"""Contract tests for the production Lighthouse matrix aggregation."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import lighthouse_analysis as audit  # noqa: E402


class LighthouseMatrixTests(unittest.TestCase):
    def test_nine_baseline_page_types_are_enabled(self):
        self.assertEqual(len(audit.DEFAULT_PAGE_KEYS.split(",")), 9)
        keys = {page.key for page in audit.PAGES}
        self.assertTrue(set(audit.DEFAULT_PAGE_KEYS.split(",")).issubset(keys))

    def test_mobile_medians_handle_noise_and_none_metrics(self):
        def sample(performance, lcp, ttfb):
            return {
                "scores": {name: performance for name in audit.CATEGORIES},
                "metrics": {"lcp_ms": lcp, "ttfb_ms": ttfb, "cls": 0.0},
                "failed_audits": [],
            }

        result = audit.median_samples([
            sample(53, 7800, None),
            sample(91, 3300, 210),
            sample(92, 3100, 220),
        ])
        self.assertEqual(result["scores"]["performance"], 91)
        self.assertEqual(result["metrics"]["lcp_ms"], 3300)
        self.assertEqual(result["metrics"]["ttfb_ms"], 215)
        self.assertEqual(result["metrics"]["cls"], 0.0)

    def test_report_lists_mobile_and_desktop_separately(self):
        page = {
            "key": "archive", "label": "Archive", "url": "https://waylonwalker.com/archive/",
            "scores": {name: 91 for name in audit.CATEGORIES},
            "desktop_scores": {name: 100 for name in audit.CATEGORIES},
            "mobile_runs": 3, "desktop_runs": 1,
            "metrics": {"fcp_ms": 1500, "lcp_ms": 3300, "ttfb_ms": 220,
                        "tbt_ms": 0, "cls": 0, "si_ms": 2500},
            "failed_audits": [],
        }
        summary = {"base_url": "https://waylonwalker.com", "run_id": "test",
                   "pages": [page], "averages": page["scores"]}
        markdown = audit.render_markdown(summary, None)
        self.assertIn("Mobile scores (median of 3)", markdown)
        self.assertIn("Desktop scores (1 run)", markdown)
        self.assertIn("LCP 3.30s", markdown)


if __name__ == "__main__":
    unittest.main()
