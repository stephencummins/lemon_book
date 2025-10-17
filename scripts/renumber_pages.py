#!/usr/bin/env python3
"""Renumber pages sequentially in clean_book.md"""

import re

# Read the backup file
with open('clean_book.md.bak', 'r') as f:
    content = f.read()

# Find all page number markers
pattern = r'<div align="right"><sub>(\d+)</sub></div>'
matches = list(re.finditer(pattern, content))

print(f"Found {len(matches)} page markers")
print(f"Current range: {matches[0].group(1)} to {matches[-1].group(1)}")

# Replace with sequential numbering starting from 1
new_content = content
page_num = 1

for match in matches:
    old_marker = match.group(0)
    new_marker = f'<div align="right"><sub>{page_num}</sub></div>'
    # Replace only the first occurrence to avoid issues
    new_content = new_content.replace(old_marker, new_marker, 1)
    page_num += 1

# Write the updated content
with open('clean_book.md', 'w') as f:
    f.write(new_content)

print(f"✓ Renumbered pages 1 to {page_num - 1}")
