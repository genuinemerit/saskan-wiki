#python

import sys
import markdownify

if len(sys.argv) != 2:
    raise ValueError("Please provide path to HTML file to be converted to markdown.")

html_file = sys.argv[1]
print(f"Converting {html_file} to markdown...")
with open(html_file, "r") as f:
    html = f.read()
md = markdownify.markdownify(html, heading_style="ATX")
md_file = html_file.replace(".html", ".md")
with open(md_file, "w") as f:
	f.write(md)


