"""Inline the sample RFP into the app so index.html works offline and on GitHub Pages.

    python build.py   ->  index.html
"""
from pathlib import Path

root = Path(__file__).parent
sample = (root / "samples" / "sample-rfp-northwind.txt").read_text(encoding="utf-8")
sample = sample.replace("</script", "<\\/script")
html = (root / "src" / "app.html").read_text(encoding="utf-8").replace("__SAMPLE_RFP__", sample)
(root / "index.html").write_text(html, encoding="utf-8")
print("wrote index.html", len(html), "bytes")
