#!/usr/bin/env python3
"""
Smart page marker placement - places markers at natural breaks:
1. Section headers (##)
2. Bold subsections (**)
3. Paragraph breaks

Places one marker per page based on ~275 words per page.
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

def is_break_point(line, next_line=None):
    """Check if this line is a potential break point"""
    line_stripped = line.strip()

    # Section header (##)
    if line_stripped.startswith('##') and not line_stripped.startswith('###'):
        return True

    # Bold subsection at start of line
    if line_stripped.startswith('**') and '**' in line_stripped[2:]:
        return True

    # Paragraph break (empty line followed by text)
    if line_stripped == '' and next_line and next_line.strip() and not next_line.strip().startswith('→'):
        return True

    return False

def process_file(filename, page_numbers):
    """Add page markers to a file"""
    if not os.path.exists(filename):
        print(f"  ⚠️  File not found: {filename}")
        return False

    print(f"\nProcessing {filename}...")
    print(f"  Pages: {page_numbers[0]} to {page_numbers[-1]} ({len(page_numbers)} pages)")

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ❌ Error reading file: {e}")
        return False

    # Calculate target words per page
    total_words = count_words(content)
    words_per_page = total_words / len(page_numbers)

    print(f"  Total words: {total_words}, Words per page: {words_per_page:.1f}")

    # Split into lines
    lines = content.split('\n')

    # Find all potential break points
    break_points = []
    for i in range(len(lines)):
        next_line = lines[i + 1] if i + 1 < len(lines) else None
        if is_break_point(lines[i], next_line):
            break_points.append(i)

    print(f"  Found {len(break_points)} potential break points")

    # Place markers at break points closest to target word counts
    page_placements = []

    # First page always at line 0
    page_placements.append((0, page_numbers[0]))

    # For remaining pages, find best break point
    cumulative_words = 0

    for page_idx in range(1, len(page_numbers)):
        target_words = page_idx * words_per_page

        # Find break point closest to target
        best_line = None
        best_diff = float('inf')

        # Count words up to each break point
        for break_line in break_points:
            if break_line <= page_placements[-1][0]:  # Skip if before last marker
                continue

            # Count words from start to this line
            words_to_here = sum(count_words(lines[i]) for i in range(break_line))
            diff = abs(words_to_here - target_words)

            if diff < best_diff:
                best_diff = diff
                best_line = break_line

        if best_line is not None:
            page_placements.append((best_line, page_numbers[page_idx]))

    print(f"  Placing {len(page_placements)} page markers")

    # Insert markers (in reverse to preserve line numbers)
    for line_num, page_num in reversed(page_placements):
        # Skip if already has a marker
        if lines[line_num].strip().startswith('→'):
            continue

        marker = f'→ {page_num} ←\n\n---\n'

        # If this is a blank line (paragraph break), insert after it
        if lines[line_num].strip() == '':
            lines.insert(line_num + 1, marker)
        else:
            # Otherwise insert before (for headers and bold text)
            lines.insert(line_num, marker)

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
    print("ADDING PAGE MARKERS WITH SMART PLACEMENT")
    print("=" * 70)

    success_count = 0
    for filename, page_numbers in CHAPTERS:
        if process_file(filename, page_numbers):
            success_count += 1

    print("\n" + "=" * 70)
    print(f"✅ Successfully processed {success_count}/{len(CHAPTERS)} files")
    print("=" * 70)

if __name__ == "__main__":
    main()
