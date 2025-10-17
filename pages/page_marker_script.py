#!/usr/bin/env python3
"""
Script to add page markers to all chapter files based on natural content breaks.
Places markers every ~275 words at section boundaries.
"""

import re
import sys

# Define chapters with their starting page numbers and target page counts
CHAPTERS = [
    # (filename, start_page, page_count, use_roman)
    ("00_front_matter.md", "i", 2, True),
    ("00_introduction.md", "iii", 2, True),
    ("01_enlightenment_roots_full.md", 1, 11, False),
    ("02_classical_liberalism.md", 12, 12, False),
    ("03_build_houses_full.md", 24, 7, False),
    ("04_Pt1_mental_health_full.md", 31, 8, False),
    ("04_Pt2_Reclaiming_Healthcare.md", 39, 10, False),
    ("05_capitalism_conscience.md", 49, 8, False),
    ("06_every_vote_counts.md", 57, 7, False),
    ("07_europe_complicated.md", 64, 6, False),
    ("08_immigration_conversations.md", 70, 14, False),
    ("09_green_growth.md", 84, 8, False),
    ("10_technology_good.md", 92, 16, False),
    ("11_right_education.md", 108, 6, False),
    ("12_your_rights_choices.md", 114, 8, False),
    ("13_rights_modern_age.md", 122, 8, False),
    ("14_tomorrows_tyranny.md", 130, 7, False),
    ("15_guest_voices.md", 137, 8, False),
    ("16_cooption_language.md", 145, 10, False),
    ("17_reclaiming_liberalism.md", 155, 9, False),
    ("18_liberal_lemonade.md", 164, 14, False),
]

def count_words(text):
    """Count words in text"""
    return len(text.split())

def add_page_marker(page_num, is_roman=False):
    """Generate page marker in arrow format"""
    return f'→ {page_num} ←\n\n---\n\n'

def process_file(filename, start_page, page_count, use_roman):
    """Add page markers to a file"""
    print(f"\nProcessing {filename}...")
    print(f"  Start page: {start_page}, Pages: {page_count}")

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"  ERROR: File not found!")
        return False

    # Calculate words per page
    total_words = count_words(content)
    words_per_page = total_words / page_count if page_count > 0 else 275

    print(f"  Total words: {total_words}, Target words/page: {words_per_page:.0f}")

    # Split into lines
    lines = content.split('\n')

    # Find section headers (lines starting with # or ##)
    headers = []
    for i, line in enumerate(lines):
        if line.strip().startswith('#') and not line.strip().startswith('###'):
            headers.append(i)

    print(f"  Found {len(headers)} section headers")

    # Calculate where pages should break (roughly every words_per_page words)
    # Place markers at headers closest to target word counts
    page_breaks = []
    current_page = start_page if isinstance(start_page, int) else 1

    # First page marker at start
    if not content.strip().startswith('→'):
        page_breaks.append((0, start_page))
        if isinstance(start_page, int):
            current_page = start_page + 1
        else:
            current_page = 1

    # Calculate subsequent pages
    target_words = words_per_page
    cumulative_words = 0

    for i, line in enumerate(lines):
        cumulative_words += count_words(line)

        # Check if we've hit target and if this is a good break point
        if cumulative_words >= target_words and i in headers:
            page_breaks.append((i, current_page))
            current_page += 1
            target_words += words_per_page

    print(f"  Will add {len(page_breaks)} page markers")

    # Add page markers (in reverse to preserve line numbers)
    for line_num, page_num in reversed(page_breaks[1:]):  # Skip first if already exists
        marker = add_page_marker(page_num, use_roman)
        lines.insert(line_num, marker.rstrip())

    # Add first page marker if needed
    if page_breaks and page_breaks[0][0] == 0:
        marker = add_page_marker(page_breaks[0][1], use_roman)
        if not lines[0].strip().startswith('→'):
            lines.insert(0, marker.rstrip())

    # Write back
    new_content = '\n'.join(lines)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"  ✓ Complete!")
    return True

def main():
    print("=" * 60)
    print("ADDING PAGE MARKERS TO ALL CHAPTERS")
    print("=" * 60)

    success_count = 0
    for filename, start_page, page_count, use_roman in CHAPTERS:
        if process_file(filename, start_page, page_count, use_roman):
            success_count += 1

    print("\n" + "=" * 60)
    print(f"Complete! Processed {success_count}/{len(CHAPTERS)} files")
    print("=" * 60)

if __name__ == "__main__":
    main()
