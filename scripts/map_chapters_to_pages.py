#!/usr/bin/env python3
"""Map chapters to their page numbers in clean_book.md"""

import re

with open('clean_book.md', 'r') as f:
    lines = f.readlines()

# First pass: record all page numbers and their line numbers
page_markers = {}
for i, line in enumerate(lines):
    match = re.search(r'<div align="right"><sub>(\d+)</sub></div>', line)
    if match:
        page_markers[i] = int(match.group(1))

# Second pass: find chapters and map to most recent page
chapter_mapping = {}
current_page = 1

for i, line in enumerate(lines):
    # Update current page if we passed a page marker
    for marker_line, page_num in page_markers.items():
        if marker_line < i:
            current_page = max(current_page, page_num)
    
    # Look for chapter headings
    if line.startswith('# Chapter '):
        chapter_mapping[i] = (line.strip(), current_page)

# Print mapping
print("Chapter to Page Mapping:")
print("=" * 70)
for line_num in sorted(chapter_mapping.keys()):
    chapter_title, page = chapter_mapping[line_num]
    print(f"Page {page:3d}: {chapter_title}")

