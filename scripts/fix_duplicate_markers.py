#!/usr/bin/env python3
"""
Script to fix duplicate page markers in chapter files.
Removes old markers and keeps only the correct sequential ones.
"""

import re
import os

# Define chapters with their page ranges
CHAPTERS = [
    ("00_front_matter.md", "i", "ii"),
    ("00_introduction.md", "iii", "iv"),
    ("01_enlightenment_roots_full.md", 1, 11),
    ("02_classical_liberalism.md", 12, 23),
    ("03_build_houses_full.md", 24, 30),
    ("04_Pt1_mental_health_full.md", 31, 38),
    ("04_Pt2_Reclaiming_Healthcare.md", 39, 48),
    ("05_capitalism_conscience.md", 49, 56),
    ("06_every_vote_counts.md", 57, 63),
    ("07_europe_complicated.md", 64, 69),
    ("08_immigration_conversations.md", 70, 83),
    ("09_green_growth.md", 84, 91),
    ("10_technology_good.md", 92, 107),
    ("11_right_education.md", 108, 113),
    ("12_your_rights_choices.md", 114, 121),
    ("13_rights_modern_age.md", 122, 129),
    ("14_tomorrows_tyranny.md", 130, 136),
    ("15_guest_voices.md", 137, 144),
    ("16_cooption_language.md", 145, 154),
    ("17_reclaiming_liberalism.md", 155, 163),
    ("18_liberal_lemonade.md", 164, 177),
]

def roman_to_int(roman):
    """Convert roman numeral to integer"""
    roman_dict = {'i': 1, 'ii': 2, 'iii': 3, 'iv': 4, 'v': 5}
    return roman_dict.get(roman.lower(), 0)

def is_valid_page(page_str, start_page, end_page):
    """Check if page number is valid for this chapter"""
    # Handle roman numerals
    if isinstance(start_page, str):
        start_num = roman_to_int(start_page)
        end_num = roman_to_int(end_page)
        page_num = roman_to_int(page_str)
        return start_num <= page_num <= end_num

    # Handle regular numbers
    try:
        page_num = int(page_str)
        return start_page <= page_num <= end_page
    except ValueError:
        return False

def clean_markers(content, start_page, end_page):
    """Remove invalid markers and duplicates, keep only valid sequential ones"""
    lines = content.split('\n')

    # Find all markers with their line numbers
    markers = []
    marker_pattern = r'→\s*([^←]+)\s*←'

    for i, line in enumerate(lines):
        match = re.search(marker_pattern, line)
        if match:
            page_str = match.group(1).strip()
            is_valid = is_valid_page(page_str, start_page, end_page)
            markers.append((i, page_str, is_valid))

    # Remove invalid markers
    lines_to_remove = set()
    for line_num, page_str, is_valid in markers:
        if not is_valid:
            lines_to_remove.add(line_num)
            # Also remove the following line if it's a separator
            if line_num + 1 < len(lines) and lines[line_num + 1].strip() == '':
                lines_to_remove.add(line_num + 1)
            if line_num + 2 < len(lines) and lines[line_num + 2].strip() == '---':
                lines_to_remove.add(line_num + 2)

    # Remove duplicate consecutive markers
    seen_pages = set()
    for i in range(len(markers) - 1):
        line_num1, page1, valid1 = markers[i]
        line_num2, page2, valid2 = markers[i + 1]

        # If two consecutive markers have the same page number, remove the first
        if page1 == page2 and valid1 and valid2:
            lines_to_remove.add(line_num1)
            if line_num1 + 1 < len(lines) and lines[line_num1 + 1].strip() == '':
                lines_to_remove.add(line_num1 + 1)
            if line_num1 + 2 < len(lines) and lines[line_num1 + 2].strip() == '---':
                lines_to_remove.add(line_num1 + 2)

    # Rebuild content without removed lines
    new_lines = [line for i, line in enumerate(lines) if i not in lines_to_remove]

    return '\n'.join(new_lines)

def process_file(filename, start_page, end_page):
    """Process a single file"""
    if not os.path.exists(filename):
        print(f"  ⚠️  File not found: {filename}")
        return False

    print(f"Processing {filename}...")

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ❌ Error reading file: {e}")
        return False

    # Count markers before
    before_count = len(re.findall(r'→\s*([^←]+)\s*←', content))

    # Clean markers
    new_content = clean_markers(content, start_page, end_page)

    # Count markers after
    after_count = len(re.findall(r'→\s*([^←]+)\s*←', new_content))

    removed = before_count - after_count

    if removed > 0:
        # Write back
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  ✅ Removed {removed} duplicate/invalid markers ({before_count} → {after_count})")
            return True
        except Exception as e:
            print(f"  ❌ Error writing file: {e}")
            return False
    else:
        print(f"  ℹ️  No changes needed ({after_count} markers)")
        return True

def main():
    print("=" * 70)
    print("FIXING DUPLICATE PAGE MARKERS")
    print("=" * 70)
    print()

    success_count = 0
    for filename, start_page, end_page in CHAPTERS:
        if process_file(filename, start_page, end_page):
            success_count += 1

    print()
    print("=" * 70)
    print(f"✅ Successfully processed {success_count}/{len(CHAPTERS)} files")
    print("=" * 70)

if __name__ == "__main__":
    main()
