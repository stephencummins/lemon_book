#!/usr/bin/env python3
"""
Update index page numbers to match actual chapter page numbers.
The old index was based on outdated ToC page numbers.
"""

import re

# Mapping of old page ranges to new page ranges
# Based on the comparison between old ToC and actual pages
PAGE_ADJUSTMENTS = {
    # Front matter and Part I
    (3, 15): (1, 11),      # Chapter 1
    (16, 27): (12, 23),    # Chapter 2

    # Part II
    (28, 34): (24, 30),    # Chapter 3
    (35, 42): (31, 38),    # Chapter 4 Part I
    (43, 52): (39, 48),    # Chapter 4 Part II
    (53, 60): (49, 56),    # Chapter 5
    (61, 67): (57, 63),    # Chapter 6
    (68, 73): (64, 69),    # Chapter 7
    (74, 87): (70, 83),    # Chapter 8
    (88, 95): (84, 91),    # Chapter 9

    # Part III
    (96, 111): (92, 107),  # Chapter 10
    (112, 117): (108, 113), # Chapter 11
    (118, 125): (114, 121), # Chapter 12
    (126, 133): (122, 129), # Chapter 13
    (134, 140): (130, 136), # Chapter 14

    # Part IV
    (141, 148): (137, 144), # Chapter 15
    (149, 158): (145, 154), # Chapter 16
    (159, 167): (155, 163), # Chapter 17
    (168, 181): (164, 177), # Chapter 18
}

def adjust_page_number(old_page):
    """Adjust a single page number from old to new"""
    for (old_start, old_end), (new_start, new_end) in PAGE_ADJUSTMENTS.items():
        if old_start <= old_page <= old_end:
            # Calculate offset within range
            offset = old_page - old_start
            return new_start + offset
    # If not in any range, return as-is (might be back matter)
    return old_page

def adjust_page_range(match):
    """Adjust page range in format XX-YY or XX"""
    text = match.group(0)

    # Handle single page numbers
    if '-' not in text:
        page = int(text)
        new_page = adjust_page_number(page)
        return str(new_page)

    # Handle page ranges XX-YY
    parts = text.split('-')
    start = int(parts[0])
    end = int(parts[1])

    new_start = adjust_page_number(start)
    new_end = adjust_page_number(end)

    return f"{new_start}-{new_end}"

def update_index(content):
    """Update all page numbers in the index"""
    # Pattern to match page numbers: either single numbers or ranges
    # Must be followed by specific punctuation or end of line
    pattern = r'\b(\d+(?:-\d+)?)\b(?=[,;\s]|$)'

    new_content = re.sub(pattern, adjust_page_range, content)
    return new_content

def main():
    input_file = "book_index_with_pages.md"

    print("=" * 70)
    print("UPDATING INDEX PAGE NUMBERS")
    print("=" * 70)
    print()

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"✓ Read {input_file}")
    except Exception as e:
        print(f"✗ Error reading file: {e}")
        return False

    # Update page numbers
    new_content = update_index(content)

    # Count changes
    old_numbers = re.findall(r'\b\d+(?:-\d+)?\b', content)
    new_numbers = re.findall(r'\b\d+(?:-\d+)?\b', new_content)

    print(f"✓ Updated {len(old_numbers)} page references")

    # Write back
    try:
        with open(input_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✓ Wrote updated index to {input_file}")
    except Exception as e:
        print(f"✗ Error writing file: {e}")
        return False

    print()
    print("=" * 70)
    print("✅ INDEX UPDATE COMPLETE")
    print("=" * 70)

    return True

if __name__ == "__main__":
    main()
