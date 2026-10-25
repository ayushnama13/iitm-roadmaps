#!/usr/bin/env python3
import sys
import os
import subprocess
import tempfile
import re
import html
import markdown

def main():
    if len(sys.argv) != 3:
        print(f"Usage: python3 {sys.argv[0]} INPUT.md OUTPUT.pdf", file=sys.stderr)
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Check input file existence
    if not os.path.isfile(input_path):
        print(f"Error: Input file '{input_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    # Check chrome existence
    chrome_path = "/usr/bin/google-chrome"
    if not os.path.isfile(chrome_path):
        print(f"Error: Google Chrome not found at '{chrome_path}'.", file=sys.stderr)
        sys.exit(1)

    # Read markdown input
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            md_content = f.read()
        # local links to other .md files point at their PDF versions
        md_content = re.sub(r"\[([^\]]*?)\.md\]\((?!https?://)([^)\s]+)\.md\)", r"[\1.pdf](\2.pdf)", md_content)
        md_content = re.sub(r"\]\((?!https?://)([^)\s]+)\.md\)", r"](\1.pdf)", md_content)
    except Exception as e:
        print(f"Error reading input file: {e}", file=sys.stderr)
        sys.exit(1)

    # Process <details> blocks to force open and parse inner markdown
    def process_details(match):
        content = match.group(1)
        summary_match = re.search(r"(<summary>.*?</summary>)", content, re.IGNORECASE | re.DOTALL)
        summary = summary_match.group(1) if summary_match else ""
        body = content.replace(summary, "").strip()
        body_html = markdown.markdown(body, extensions=["tables", "fenced_code", "sane_lists", "md_in_html"])
        return f"<details open>\n{summary}\n{body_html}\n</details>"

    processed_md = re.sub(r"<details>(.*?)</details>", process_details, md_content, flags=re.DOTALL | re.IGNORECASE)

    # Convert Markdown to HTML body
    body_html = markdown.markdown(
        processed_md,
        extensions=["tables", "fenced_code", "sane_lists", "md_in_html"]
    )

    m = re.search(r"^# (.+)$", md_content, re.M)
    title = html.escape(m.group(1) if m else os.path.basename(output_path))

    # Wrap in standalone HTML template with embedded CSS
    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>
  @page {{
    size: A4;
    margin: 16mm;
  }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 10.5pt;
    line-height: 1.45;
    color: #212529;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
  }}
  h1, h2, h3, h4, h5, h6 {{
    color: #212529;
    margin-top: 1.2em;
    margin-bottom: 0.5em;
    font-weight: 600;
  }}
  h1 {{
    font-size: 1.8em;
    border-bottom: 2px solid #343a40;
    padding-bottom: 6px;
    margin-top: 0;
  }}
  h2 {{
    font-size: 1.4em;
    page-break-after: avoid;
    break-after: avoid;
  }}
  h3 {{
    font-size: 1.2em;
    page-break-after: avoid;
    break-after: avoid;
  }}
  p {{
    margin: 0 0 1em 0;
  }}
  a {{
    color: #0366d6;
    text-decoration: none;
    overflow-wrap: anywhere;
    word-break: break-word;
  }}
  table {{
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 1em;
  }}
  /* tables with an all-empty header row (key/value tables) */
  thead:not(:has(th:not(:empty))) {{
    display: none;
  }}
  th, td {{
    border-bottom: 1px solid #dee2e6;
    padding: 6px 10px;
    text-align: left;
    vertical-align: top;
    overflow-wrap: break-word;
  }}
  /* short first column (Week, key) only in narrow tables of <= 3 columns */
  th:first-child:nth-last-child(-n+3), td:first-child:nth-last-child(-n+3) {{
    white-space: nowrap;
  }}
  th {{
    background-color: #f1f3f5;
    font-weight: 600;
    border-bottom: 2px solid #adb5bd;
  }}
  tr:nth-child(even) {{
    background-color: #f8f9fa;
  }}
  blockquote {{
    border-left: 4px solid #ced4da;
    padding-left: 1em;
    margin: 1em 0;
    color: #495057;
    page-break-inside: avoid;
    break-inside: avoid;
  }}
  pre, code {{
    font-family: SFMono-Regular, Consolas, "Liberation Mono", Menlo, Courier, monospace;
    font-size: 0.95em;
  }}
  pre {{
    background-color: #f8f9fa;
    padding: 10px;
    border: 1px solid #e9ecef;
    border-radius: 4px;
    white-space: pre-wrap;
    page-break-inside: avoid;
    break-inside: avoid;
  }}
  code {{
    background-color: rgba(27, 31, 35, 0.05);
    padding: 2px 4px;
    border-radius: 3px;
  }}
  pre code {{
    background-color: transparent;
    padding: 0;
  }}
  details {{
    margin-bottom: 1em;
  }}
  summary {{
    font-weight: 600;
    cursor: pointer;
    margin-bottom: 0.5em;
  }}
  ul, ol {{
    margin-top: 0;
    margin-bottom: 1em;
    padding-left: 2em;
  }}
  li {{
    margin-bottom: 0.3em;
  }}
  tr {{
    page-break-inside: avoid;
    break-inside: avoid;
  }}
  figure {{
    page-break-inside: avoid;
    break-inside: avoid;
  }}
</style>
</head>
<body>
{body_html}
</body>
</html>
"""

    # Use a temp dir that is cleaned up
    with tempfile.TemporaryDirectory() as tmpdir:
        tmppath = os.path.join(tmpdir, "input.html")
        try:
            with open(tmppath, "w", encoding="utf-8") as f:
                f.write(html_doc)
        except Exception as e:
            print(f"Error writing temporary HTML file: {e}", file=sys.stderr)
            sys.exit(1)

        # Run headless Chrome to print to PDF
        cmd = [
            chrome_path,
            "--headless=new",
            "--no-pdf-header-footer",
            f"--print-to-pdf={os.path.abspath(output_path)}",
            f"file://{os.path.abspath(tmppath)}"
        ]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            if result.returncode != 0:
                print(f"Error: Chrome exited with non-zero code {result.returncode}", file=sys.stderr)
                if result.stderr:
                    print(result.stderr, file=sys.stderr)
                sys.exit(1)
        except subprocess.TimeoutExpired:
            print("Error: Chrome PDF generation timed out.", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Error running Chrome: {e}", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    main()
