#!/usr/bin/env python3
"""
Convert HTML to PDF using WeasyPrint
"""
import weasyprint
import sys
from pathlib import Path

def html_to_pdf(html_file, pdf_file):
    """Convert HTML file to PDF"""
    try:
        # Read the HTML content
        html_content = Path(html_file).read_text(encoding='utf-8')
        
        # Create PDF
        html = weasyprint.HTML(string=html_content, base_url='.')
        css = weasyprint.CSS(string='''
            @page {
                margin: 1in;
                size: A4;
            }
            body {
                font-family: "Times New Roman", serif;
                font-size: 11pt;
                line-height: 1.4;
            }
            h1, h2, h3 {
                color: #333;
                page-break-after: avoid;
            }
            h1 {
                font-size: 18pt;
                margin-top: 24pt;
            }
            h2 {
                font-size: 14pt;
                margin-top: 18pt;
            }
            .toc {
                page-break-after: always;
            }
        ''')
        
        html.write_pdf(pdf_file, stylesheets=[css])
        print(f"✅ Successfully created PDF: {pdf_file}")
        return True
        
    except Exception as e:
        print(f"❌ Error creating PDF: {e}")
        return False

if __name__ == "__main__":
    html_file = "Complete_Lemon_Book.html"
    pdf_file = "The_Lemon_Book.pdf"
    
    if html_to_pdf(html_file, pdf_file):
        print(f"PDF generation completed: {pdf_file}")
    else:
        sys.exit(1)