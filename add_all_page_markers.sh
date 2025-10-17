#!/bin/bash

# Script to add page markers to all remaining chapter files
# Uses Markdown format: → X ←

echo "Adding page markers to all remaining chapters..."
echo "================================================"

# Function to add opening page marker to a file
add_opening_marker() {
    local file="$1"
    local page="$2"

    # Add marker at beginning if not already present
    if ! head -1 "$file" | grep -q "→"; then
        echo "→ $page ←

---
" | cat - "$file" > temp && mv temp "$file"
        echo "✓ Added opening marker (page $page) to $file"
    else
        echo "  Opening marker already exists in $file"
    fi
}

# Chapters 3-18 with their starting pages
# We'll add the opening marker, then you can add internal markers manually or with another pass

# Part II
add_opening_marker "03_build_houses_full.md" "24"
add_opening_marker "04_Pt1_mental_health_full.md" "31"
add_opening_marker "04_Pt2_Reclaiming_Healthcare.md" "39"
add_opening_marker "05_capitalism_conscience.md" "49"
add_opening_marker "06_every_vote_counts.md" "57"
add_opening_marker "07_europe_complicated.md" "64"
add_opening_marker "08_immigration_conversations.md" "70"
add_opening_marker "09_green_growth.md" "84"

# Part III
add_opening_marker "10_technology_good.md" "92"
add_opening_marker "11_right_education.md" "108"
add_opening_marker "12_your_rights_choices.md" "114"
add_opening_marker "13_rights_modern_age.md" "122"
add_opening_marker "14_tomorrows_tyranny.md" "130"

# Part IV
add_opening_marker "15_guest_voices.md" "137"
add_opening_marker "16_cooption_language.md" "145"
add_opening_marker "17_reclaiming_liberalism.md" "155"
add_opening_marker "18_liberal_lemonade.md" "164"

echo ""
echo "================================================"
echo "Opening page markers added to all chapters!"
echo "Now need to add internal page markers based on"
echo "natural section breaks (~275 words per page)"
echo "================================================"
