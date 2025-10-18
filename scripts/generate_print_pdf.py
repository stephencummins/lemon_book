#!/usr/bin/env python3
"""
Generate print-ready PDF from markdown files with 300 DPI resolution.
This script uses WeasyPrint for proper print-quality PDF generation.
"""

import os
import sys
from pathlib import Path
import subprocess
import tempfile

# Check for required libraries
try:
    from weasyprint import HTML, CSS
    WEASYPRINT_AVAILABLE = True
except ImportError:
    WEASYPRINT_AVAILABLE = False
    print("⚠️  WeasyPrint not installed. Install with: pip install weasyprint")

try:
    import markdown
    MARKDOWN_AVAILABLE = True
except ImportError:
    MARKDOWN_AVAILABLE = False
    print("⚠️  markdown not installed. Install with: pip install markdown")

# Configuration
BOOK_DIR = Path(__file__).parent.parent
CHAPTERS = [
    "00_front_matter.md",
    "00_introduction.md",
    "01_enlightenment_roots.md",
    "02_classical_liberalism.md",
    "03_build_houses_full.md",
    "04_Pt1_mental_health_full.md",
    "04_Pt2_Reclaiming_Healthcare.md",
    "05_capitalism_conscience.md",
    "06_every_vote_counts.md",
    "07_europe_complicated.md",
    "08_immigration_conversations.md",
    "09_green_growth.md",
    "10_technology_good.md",
    "11_right_education.md",
    "12_your_rights_choices.md",
    "13_rights_modern_age.md",
    "14_tomorrows_tyranny.md",
    "15_guest_voices.md",
    "16_cooption_language.md",
    "17_reclaiming_liberalism.md",
    "18_Conclusion.md",
    "book_index_with_pages.md",
]

# Print-quality CSS for 6"x9" book at 300 DPI
PRINT_CSS = """
@page {
    size: 6in 9in;
    margin: 0.75in 0.5in;

    @bottom-center {
        content: counter(page);
        font-size: 10pt;
    }
}

body {
    font-family: 'Georgia', 'Times New Roman', serif;
    font-size: 11pt;
    line-height: 1.5;
    color: #000;
    hyphens: auto;
}

h1 {
    font-size: 24pt;
    font-weight: bold;
    margin-top: 0;
    margin-bottom: 0.5in;
    page-break-before: always;
}

h2 {
    font-size: 18pt;
    font-weight: bold;
    margin-top: 0.3in;
    margin-bottom: 0.15in;
}

h3 {
    font-size: 14pt;
    font-weight: bold;
    margin-top: 0.2in;
    margin-bottom: 0.1in;
}

p {
    margin-bottom: 0.1in;
    text-align: justify;
    orphans: 2;
    widows: 2;
}

img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 0.2in auto;
    /* Force high-quality image rendering */
    image-rendering: high-quality;
    image-rendering: -webkit-optimize-contrast;
}

blockquote {
    margin: 0.15in 0.5in;
    font-style: italic;
    border-left: 3px solid #ccc;
    padding-left: 0.2in;
}

code {
    font-family: 'Courier New', monospace;
    background-color: #f5f5f5;
    padding: 0.05in;
    font-size: 9pt;
}

pre {
    background-color: #f5f5f5;
    padding: 0.1in;
    margin: 0.15in 0;
    overflow-x: auto;
    font-size: 9pt;
}

ul, ol {
    margin-left: 0.3in;
    margin-bottom: 0.1in;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 0.15in 0;
}

th, td {
    border: 1px solid #000;
    padding: 0.05in;
    text-align: left;
}

th {
    background-color: #f0f0f0;
    font-weight: bold;
}

/* Page breaks */
.page-break {
    page-break-after: always;
}

/* Prevent page breaks inside these elements */
h1, h2, h3, h4, h5, h6 {
    page-break-after: avoid;
}

figure, img {
    page-break-inside: avoid;
}
"""


def convert_markdown_to_html(markdown_files, output_html):
    """Convert markdown files to a single HTML file."""
    if not MARKDOWN_AVAILABLE:
        print("❌ markdown library not available")
        return False

    print(f"📝 Converting {len(markdown_files)} markdown files to HTML...")

    md = markdown.Markdown(extensions=[
        'extra',  # Tables, footnotes, etc.
        'codehilite',  # Code highlighting
        'toc',  # Table of contents
        'sane_lists',  # Better list handling
    ])

    html_parts = ['<!DOCTYPE html>', '<html>', '<head>',
                  '<meta charset="utf-8">',
                  '<title>The Lemon Book: Refreshing Liberalism</title>',
                  '</head>', '<body>']

    for md_file in markdown_files:
        md_path = BOOK_DIR / md_file
        if not md_path.exists():
            print(f"⚠️  File not found: {md_file}")
            continue

        print(f"   Converting: {md_file}")
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()

        html_parts.append(md.convert(content))
        md.reset()

    html_parts.extend(['</body>', '</html>'])

    with open(output_html, 'w', encoding='utf-8') as f:
        f.write('\n'.join(html_parts))

    print(f"✅ HTML created: {output_html}")
    return True


def generate_pdf_weasyprint(html_file, pdf_file, dpi=300):
    """Generate PDF using WeasyPrint with specified DPI."""
    if not WEASYPRINT_AVAILABLE:
        print("❌ WeasyPrint not available")
        return False

    print(f"📄 Generating PDF with {dpi} DPI...")

    # Create CSS with DPI setting
    css = CSS(string=PRINT_CSS)

    # Generate PDF
    html = HTML(filename=str(html_file), base_url=str(BOOK_DIR))
    html.write_pdf(
        pdf_file,
        stylesheets=[css],
        resolution=dpi,  # Set output resolution to 300 DPI
        optimize_images=False,  # Don't compress images (keep quality)
    )

    print(f"✅ PDF created: {pdf_file}")
    return True


def generate_pdf_pandoc(output_pdf):
    """Fallback: Generate PDF using pandoc (requires LaTeX)."""
    print("📄 Generating PDF using pandoc...")

    cmd = [
        "pandoc",
        *CHAPTERS,
        "-o", str(output_pdf),
        "--metadata-file=scripts/metadata.yaml",
        "--from=markdown+smart+raw_tex",
        "--resource-path=.:images",
        "--template=scripts/custom-template.latex",
        "--pdf-engine=xelatex",
        "--dpi=300",  # Set DPI for images
    ]

    try:
        subprocess.run(cmd, cwd=BOOK_DIR, check=True, capture_output=True, text=True)
        print(f"✅ PDF created: {output_pdf}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Pandoc failed: {e.stderr}")
        return False
    except FileNotFoundError:
        print("❌ Pandoc not found")
        return False


def main():
    print("=" * 80)
    print("🍋 LEMON BOOK - PRINT-READY PDF GENERATOR (300 DPI)")
    print("=" * 80)
    print()

    output_pdf = BOOK_DIR / "The_Lemon_Book_Print.pdf"

    # Method 1: Try WeasyPrint (best for print quality)
    if WEASYPRINT_AVAILABLE and MARKDOWN_AVAILABLE:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as tmp:
            temp_html = tmp.name

        try:
            if convert_markdown_to_html(CHAPTERS, temp_html):
                if generate_pdf_weasyprint(temp_html, output_pdf, dpi=300):
                    print()
                    print("=" * 80)
                    print("✨ Success!")
                    print(f"📖 Print-ready PDF: {output_pdf}")
                    print(f"🎯 Resolution: 300 DPI (Lulu standard)")
                    print(f"📏 Page size: 6\" x 9\"")
                    print()
                    print("💡 Next steps:")
                    print("   1. Review the PDF")
                    print("   2. Upload to Lulu preflight checker")
                    print("   3. Create print job via Lulu API")
                    return 0
        finally:
            if os.path.exists(temp_html):
                os.unlink(temp_html)

    # Method 2: Fallback to pandoc
    print("\n🔄 Trying pandoc fallback...")
    if generate_pdf_pandoc(output_pdf):
        print()
        print("=" * 80)
        print("✨ Success!")
        print(f"📖 Print-ready PDF: {output_pdf}")
        print(f"🎯 Target: 300 DPI")
        return 0

    # Both methods failed
    print()
    print("=" * 80)
    print("❌ Could not generate PDF")
    print()
    print("Please install one of the following:")
    print("  1. WeasyPrint: pip install weasyprint markdown")
    print("  2. Pandoc + XeLaTeX: brew install pandoc && brew install --cask mactex")
    print()
    return 1


if __name__ == "__main__":
    sys.exit(main())
