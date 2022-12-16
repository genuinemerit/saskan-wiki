#!python

import sys
import markdownify

from pathlib import Path
from pprint import pprint as pp  # noqa: F401


def get_dir_html(p_path: str) -> tuple:
    """Read a directory and return names of files that
       end with ".html".

    Args:
        p_path (str): Legit path to directory location.
    Return
        (Tuple): (Status (bool), Message (text or None),
                    Directory content (List or None))
    """
    html_files = None
    try:
        if Path(p_path).exists() and Path(p_path).is_dir():
            html_files =\
                [f for f in Path(p_path).iterdir() if f.suffix == ".html"]
            return (True, None, html_files)
        else:
            return (False, f"<{p_path}> not found", None)
    except Exception as err:
        return (False, err, None)


# Main
# ----
if len(sys.argv) != 2:
    raise ValueError("Provide path to directory containing" +
                     "HTML file to be converted.")

html_dir = sys.argv[1]
print(f"Converting HTML files in directory <{html_dir}> to markdown...")
ok, msg, html_files = get_dir_html(html_dir)
if not ok:
    print(msg)
else:
    if html_files in (None, []):
        print("No HTML files found in directory.")
    else:
        for html_file in html_files:
            with open(html_file, "r") as f:
                html = f.read()
            md = markdownify.markdownify(html, heading_style="ATX")
            md_file = str(html_file).replace(".html", ".md")
            with open(md_file, "w") as f:
                f.write(md)
            print("Converted: " + str(html_file) + " to " + md_file)
