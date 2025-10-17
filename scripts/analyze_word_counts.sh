#!/bin/bash

# Word Count Analysis Script for The Lemon Book
# Analyzes each chapter file and calculates editing requirements

echo "========================================="
echo "THE LEMON BOOK - WORD COUNT ANALYSIS"
echo "========================================="
echo ""

# Target words per page
WORDS_PER_PAGE=275

# Array of chapter files with their page allocations
declare -A chapters=(
    ["00_front_matter.md"]="4"
    ["00_introduction.md"]="1"
    ["01_enlightenment_roots_full.md"]="13"
    ["02_classical_liberalism.md"]="12"
    ["03_build_houses_full.md"]="7"
    ["04_Pt1_mental_health_full.md"]="8"
    ["04_Pt2_Reclaiming_Healthcare.md"]="10"
    ["05_capitalism_conscience.md"]="8"
    ["06_every_vote_counts.md"]="7"
    ["07_europe_complicated.md"]="6"
    ["08_immigration_conversations.md"]="14"
    ["09_green_growth.md"]="8"
    ["10_technology_good.md"]="16"
    ["11_right_education.md"]="6"
    ["12_your_rights_choices.md"]="8"
    ["13_rights_modern_age.md"]="8"
    ["14_tomorrows_tyranny.md"]="7"
    ["15_guest_voices.md"]="8"
    ["16_cooption_language.md"]="10"
    ["17_reclaiming_liberalism.md"]="9"
    ["18_liberal_lemonade.md"]="14"
)

# Function to count words in a file
count_words() {
    wc -w < "$1" | tr -d ' '
}

# Total stats
total_current=0
total_target=0
total_pages=0

echo "FILE ANALYSIS"
echo "========================================="
printf "%-40s %8s %8s %8s %8s\n" "File" "Pages" "Current" "Target" "Cut %"
echo "-----------------------------------------"

# Analyze each file
for file in "${!chapters[@]}"; do
    if [ -f "../$file" ]; then
        pages=${chapters[$file]}
        current=$(count_words "../$file")
        target=$((pages * WORDS_PER_PAGE))

        # Calculate percentage to cut
        if [ $current -gt 0 ]; then
            cut_percent=$(( (current - target) * 100 / current ))
        else
            cut_percent=0
        fi

        # Update totals
        total_current=$((total_current + current))
        total_target=$((total_target + target))
        total_pages=$((total_pages + pages))

        # Color code based on cut percentage
        if [ $cut_percent -gt 45 ]; then
            status="🔴 HEAVY"
        elif [ $cut_percent -gt 35 ]; then
            status="🟡 MODERATE"
        elif [ $cut_percent -gt 20 ]; then
            status="🟢 LIGHT"
        elif [ $cut_percent -lt 0 ]; then
            status="⚠️  SHORT"
            cut_percent=$((cut_percent * -1))
        else
            status="✅ OK"
        fi

        printf "%-40s %8s %8s %8s %7s%% %s\n" "$file" "$pages" "$current" "$target" "$cut_percent" "$status"
    else
        printf "%-40s %8s %8s %8s %s\n" "$file" "$pages" "MISSING" "N/A" "❌ NOT FOUND"
    fi
done

echo "========================================="
printf "%-40s %8s %8s %8s\n" "TOTALS" "$total_pages" "$total_current" "$total_target"

# Calculate overall cut percentage
if [ $total_current -gt 0 ]; then
    overall_cut=$(( (total_current - total_target) * 100 / total_current ))
else
    overall_cut=0
fi

echo ""
echo "SUMMARY"
echo "========================================="
echo "Total pages allocated: $total_pages"
echo "Current total words: $total_current"
echo "Target total words: $total_target"
echo "Overall reduction needed: ${overall_cut}%"
echo "Words to cut: $((total_current - target))"
echo ""

# Priority files for editing
echo "EDITING PRIORITIES"
echo "========================================="
echo ""
echo "🔴 HEAVY EDITING NEEDED (>45% reduction):"
for file in "${!chapters[@]}"; do
    if [ -f "../$file" ]; then
        pages=${chapters[$file]}
        current=$(count_words "../$file")
        target=$((pages * WORDS_PER_PAGE))
        cut_percent=$(( (current - target) * 100 / current ))

        if [ $cut_percent -gt 45 ]; then
            echo "  - $file ($cut_percent% reduction needed)"
        fi
    fi
done

echo ""
echo "🟡 MODERATE EDITING (35-45% reduction):"
for file in "${!chapters[@]}"; do
    if [ -f "../$file" ]; then
        pages=${chapters[$file]}
        current=$(count_words "../$file")
        target=$((pages * WORDS_PER_PAGE))
        cut_percent=$(( (current - target) * 100 / current ))

        if [ $cut_percent -ge 35 ] && [ $cut_percent -le 45 ]; then
            echo "  - $file ($cut_percent% reduction needed)"
        fi
    fi
done

echo ""
echo "🟢 LIGHT EDITING (20-35% reduction):"
for file in "${!chapters[@]}"; do
    if [ -f "../$file" ]; then
        pages=${chapters[$file]}
        current=$(count_words "../$file")
        target=$((pages * WORDS_PER_PAGE))
        cut_percent=$(( (current - target) * 100 / current ))

        if [ $cut_percent -ge 20 ] && [ $cut_percent -lt 35 ]; then
            echo "  - $file ($cut_percent% reduction needed)"
        fi
    fi
done

echo ""
echo "✅ MINIMAL OR NO EDITING (<20% reduction):"
for file in "${!chapters[@]}"; do
    if [ -f "../$file" ]; then
        pages=${chapters[$file]}
        current=$(count_words "../$file")
        target=$((pages * WORDS_PER_PAGE))
        cut_percent=$(( (current - target) * 100 / current ))

        if [ $cut_percent -ge 0 ] && [ $cut_percent -lt 20 ]; then
            echo "  - $file ($cut_percent% reduction needed)"
        fi
    fi
done

echo ""
echo "========================================="
echo "Analysis complete!"
echo ""
