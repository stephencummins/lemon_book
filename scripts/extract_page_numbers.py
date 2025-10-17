#!/usr/bin/env python3
"""Extract page numbers for chapters and sections from clean_book.md"""

import re

with open('clean_book.md', 'r') as f:
    content = f.read()

# Split into lines for processing
lines = content.split('\n')

# Track current page number and find headings
current_page = 0
chapter_pages = {}

for i, line in enumerate(lines):
    # Update current page number when we find a page marker
    page_match = re.search(r'<div align="right"><sub>(\d+)</sub></div>', line)
    if page_match:
        current_page = int(page_match.group(1))
    
    # Find chapter headings (# Chapter or ## heading)
    if line.startswith('# Chapter') or line.startswith('## Chapter'):
        # Get next few lines to find the title
        title = line.replace('#', '').strip()
        if i+1 < len(lines) and lines[i+1].strip():
            chapter_pages[title] = current_page
    
    # Find major section headings
    if line.startswith('### ') or line.startswith('## Part '):
        title = line.replace('#', '').strip()
        chapter_pages[title] = current_page

# Print the mapping
print("Chapter/Section Page Numbers:")
print("=" * 60)
for title, page in sorted(chapter_pages.items(), key=lambda x: x[1]):
    print(f"Page {page:3d}: {title}")

