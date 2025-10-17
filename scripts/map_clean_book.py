#!/usr/bin/env python3
"""Map all content in clean_book.md to page numbers"""

import re

with open('clean_book.md', 'r') as f:
    lines = f.readlines()

# First pass: record all page numbers and their line numbers
page_at_line = {}
for i, line in enumerate(lines):
    match = re.search(r'<div align="right"><sub>(\d+)</sub></div>', line)
    if match:
        page_at_line[i] = int(match.group(1))

# Function to find the page number for a given line
def get_page_for_line(line_num):
    # Find the most recent page marker before this line
    page = 1  # Default to page 1
    for marker_line, page_num in sorted(page_at_line.items()):
        if marker_line <= line_num:
            page = page_num
        else:
            break
    return page

# Second pass: find all headings and map to pages
content_map = []

for i, line in enumerate(lines):
    stripped = line.strip()
    
    # Skip empty lines and page markers
    if not stripped or 'page-break' in stripped or '<div align="right">' in stripped:
        continue
    
    # Capture major sections
    if stripped.startswith('# Chapter'):
        page = get_page_for_line(i)
        content_map.append((page, 'CHAPTER', stripped))
    elif stripped.startswith('## ') and not stripped.startswith('## Table'):
        page = get_page_for_line(i)
        content_map.append((page, 'SECTION', stripped.replace('##', '').strip()))
    elif stripped.startswith('### '):
        page = get_page_for_line(i)
        content_map.append((page, 'SUBSECTION', stripped.replace('###', '').strip()))
    elif stripped.startswith('**Chapter'):
        page = get_page_for_line(i)
        content_map.append((page, 'TOC_ENTRY', stripped.replace('**', '').strip()))

# Print the mapping
print("CONTENT MAP FOR clean_book.md")
print("=" * 80)
print()

for page, content_type, title in content_map:
    if content_type == 'CHAPTER':
        print(f"\n{'='*80}")
        print(f"Page {page:3d}: {title}")
        print(f"{'='*80}")
    elif content_type == 'SECTION':
        print(f"Page {page:3d}:   {title}")
    elif content_type == 'TOC_ENTRY':
        print(f"Page {page:3d}:     [TOC] {title}")

print(f"\n\nTotal Pages: {max(page_at_line.values())}")

