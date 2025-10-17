#!/usr/bin/env python3
"""
Script to add page markers with proper sequential numbering.
Places one marker per page at natural content breaks.
"""

import re
import os

# Define chapters with their page ranges
CHAPTERS = [
    ("00_front_matter.md", ["i", "ii"]),
    ("00_introduction.md", ["iii", "iv"]),
    ("01_enlightenment_roots_full.md", list(range(1, 12))),  # 1-11
    ("02_classical_liberalism.md", list(range(12, 24))),  # 12-23
    ("03_build_houses_full.md", list(range(24, 31))),  # 24-30
    ("04_Pt1_mental_health_full.md", list(range(31, 39))),  # 31-38
    ("04_Pt2_Reclaiming_Healthcare.md", list(range(39, 49))),  # 39-48
    ("05_capitalism_conscience.md", list(range(49, 57))),  # 49-56
    ("06_every_vote_counts.md", list(range(57, 64))),  # 57-63
    ("07_europe_complicated.md", list(range(64, 70))),  # 64-69
    ("08_immigration_conversations.md", list(range(70, 84))),  # 70-83
    ("09_green_growth.md", list(range(84, 92))),  # 84-91
    ("10_technology_good.md", list(range(92, 108))),  # 92-107
    ("11_right_education.md", list(range(108, 114))),  # 108-113
    ("12_your_rights_choices.md", list(range(114, 122))),  # 114-121
    ("13_rights_modern_age.md", list(range(122, 130))),  # 122-129
    ("14_tomorrows_tyranny.md", list(range(130, 137))),  # 130-136
    ("15_guest_voices.md", list(range(137, 145))),  # 137-144
    ("16_cooption_language.md", list(range(145, 155))),  # 145-154
    ("17_reclaiming_liberalism.md", list(range(155, 164))),  # 155-163
    ("18_liberal_lemonade.md", list(range(164, 178))),  # 164-177
]

def count_words(text):
    """Count words in text"""
    return len(text.split())

def add_page_marker(page_num):
    """Generate page marker in arrow format"""
    return f'→ {page_num} ←\n\n---\n\n'

def process_file(filename, page_numbers):
    """Add page markers to a file"""
    if not os.path.exists(filename):
        print(f"  ⚠️  File not found: {filename}")
        return False

    print(f"Processing {filename}...")
    print(f"  Pages: {page_numbers[0]} to {page_numbers[-1]} ({len(page_numbers)} pages)")

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ❌ Error reading file: {e}")
        return False

    # Calculate words per page
    total_words = count_words(content)
    words_per_page = total_words / len(page_numbers) if len(page_numbers) > 0 else 275

    print(f"  Total words: {total_words}, Target words/page: {words_per_page:.0f}")

    # Split into lines
    lines = content.split('\n')

    # Find section headers (lines starting with # or ##)
    headers = []
    for i, line in enumerate(lines):
        if line.strip().startswith('#') and not line.strip().startswith('###'):
            headers.append(i)

    print(f"  Found {len(headers)} section headers")

    # Calculate where pages should break
    page_breaks = []

    # Always add first page at start
    page_breaks.append((0, page_numbers[0]))

    # Calculate subsequent pages based on word count
    cumulative_words = 0
    page_index = 1  # Start from second page

    for i, line in enumerate(lines):
        cumulative_words += count_words(line)

        # Check if we've reached the next page threshold and we're at a header
        if page_index < len(page_numbers) and i in headers:
            target_words = page_index * words_per_page
            # If we're within 20% of target, place marker here
            if abs(cumulative_words - target_words) / target_words < 0.2:
                page_breaks.append((i, page_numbers[page_index]))
                page_index += 1

    print(f"  Will add {len(page_breaks)} page markers")

    # Add page markers (in reverse to preserve line numbers)
    for line_num, page_num in reversed(page_breaks[1:]):  # Skip first
        marker = add_page_marker(page_num)
        lines.insert(line_num, marker.rstrip())

    # Add first page marker
    marker = add_page_marker(page_breaks[0][1])
    if not lines[0].strip().startswith('→'):
        lines.insert(0, marker.rstrip())

    # Write back
    new_content = '\n'.join(lines)

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  ✅ Complete!")
        return True
    except Exception as e:
        print(f"  ❌ Error writing file: {e}")
        return False

def main():
    print("=" * 70)
    print("ADDING PAGE MARKERS TO ALL CHAPTERS")
    print("=" * 70)
    print()

    success_count = 0
    for filename, page_numbers in CHAPTERS:
        if process_file(filename, page_numbers):
            success_count += 1

    print()
    print("=" * 70)
    print(f"✅ Successfully processed {success_count}/{len(CHAPTERS)} files")
    print("=" * 70)

if __name__ == "__main__":
    main()
