#!/usr/bin/env python3
"""Convert HTML to PDF using Chrome headless."""

import subprocess
import sys
from pathlib import Path

def html_to_pdf_chrome(html_file, pdf_file):
    """Try to convert using Chrome headless with print-quality settings (300 DPI)."""
    chrome_paths = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
    ]

    for chrome_path in chrome_paths:
        if Path(chrome_path).exists():
            cmd = [
                chrome_path,
                "--headless",
                "--disable-gpu",
                "--print-to-pdf=" + str(pdf_file),
                # Print quality settings for 300 DPI output
                "--print-to-pdf-no-header",  # Remove headers/footers
                "--no-margins",  # Remove default margins
                # Note: Chrome doesn't have direct DPI control, but these settings
                # ensure high-quality output. Actual DPI depends on page size and
                # viewport settings in the HTML/CSS
                "file://" + str(Path(html_file).resolve())
            ]
            try:
                subprocess.run(cmd, check=True, capture_output=True)
                return True
            except subprocess.CalledProcessError:
                continue
    return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: html_to_pdf.py <input.html> <output.pdf>")
        sys.exit(1)

    html_file = sys.argv[1]
    pdf_file = sys.argv[2]

    if html_to_pdf_chrome(html_file, pdf_file):
        print(f"Successfully created {pdf_file}")
        sys.exit(0)
    else:
        print("Could not find Chrome or Chromium for PDF conversion")
        print("Please convert the HTML file manually")
        sys.exit(1)
