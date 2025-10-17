#!/usr/bin/env python3
"""
Script to remove ALL page markers from chapters so we can start fresh.
"""

import re
import os

CHAPTERS = [
    "00_front_matter.md",
    "00_introduction.md",
    "01_enlightenment_roots_full.md",
    "02_classical_liberalism.md",
    "03_build_houses_full.md",
    "04_Pt1_mental_health_full.md",
    "04_Pt2_Reclaiming_Healthcare.md",
    "05_capitalism_conscience.md",
    "06_every_vote_counts.md",
    "07_europe_complicated.md",
    "08_immigration_conversations.md",
    "09_green_growth.md",
    "10_technology_good.md",
    "11_right_education.md",
    "12_your_rights_choices.md",
    "13_rights_modern_age.md",
    "14_tomorrows_tyranny.md",
    "15_guest_voices.md",
    "16_cooption_language.md",
    "17_reclaiming_liberalism.md",
    "18_liberal_lemonade.md",
]

def remove_all_markers(content):
    """Remove all page markers and their surrounding separators"""
    lines = content.split('\n')
    new_lines = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check if this line is a page marker
        if re.search(r'→\s*[^←]+\s*←', line):
            # Skip this line
            # Also skip following blank line and --- if they exist
            if i + 1 < len(lines) and lines[i + 1].strip() == '':
                i += 1  # Skip blank line
            if i + 1 < len(lines) and lines[i + 1].strip() == '---':
                i += 1  # Skip separator
            if i + 1 < len(lines) and lines[i + 1].strip() == '':
                i += 1  # Skip blank line after separator
            i += 1
            continue

        new_lines.append(line)
        i += 1

    return '\n'.join(new_lines)

def process_file(filename):
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
    before_count = len(re.findall(r'→\s*[^←]+\s*←', content))

    if before_count == 0:
        print(f"  ℹ️  No markers found")
        return True

    # Remove all markers
    new_content = remove_all_markers(content)

    # Count markers after (should be 0)
    after_count = len(re.findall(r'→\s*[^←]+\s*←', new_content))

    # Write back
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  ✅ Removed {before_count} markers")
        return True
    except Exception as e:
        print(f"  ❌ Error writing file: {e}")
        return False

def main():
    print("=" * 70)
    print("REMOVING ALL PAGE MARKERS")
    print("=" * 70)
    print()

    success_count = 0
    for filename in CHAPTERS:
        if process_file(filename):
            success_count += 1

    print()
    print("=" * 70)
    print(f"✅ Successfully processed {success_count}/{len(CHAPTERS)} files")
    print("=" * 70)

if __name__ == "__main__":
    main()
