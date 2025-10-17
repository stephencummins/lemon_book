#!/bin/bash

# Simple word count analysis for The Lemon Book chapters

echo "========================================="
echo "THE LEMON BOOK - WORD COUNT ANALYSIS"
echo "========================================="
echo ""

WORDS_PER_PAGE=275

echo "FILE ANALYSIS"
echo "================================================================================================================"
printf "%-45s %8s %10s %10s %10s %s\n" "File" "Pages" "Current" "Target" "Diff" "Status"
echo "----------------------------------------------------------------------------------------------------------------"

# Front Matter
FILE="00_front_matter.md"
PAGES=4
if [ -f "$FILE" ]; then
    CURRENT=$(wc -w < "$FILE" | tr -d ' ')
    TARGET=$((PAGES * WORDS_PER_PAGE))
    DIFF=$((CURRENT - TARGET))
    PCT=$(( DIFF * 100 / CURRENT ))
    printf "%-45s %8d %10d %10d %+10d %s\n" "$FILE" "$PAGES" "$CURRENT" "$TARGET" "$DIFF" "($PCT%)"
fi

FILE="00_introduction.md"
PAGES=1
if [ -f "$FILE" ]; then
    CURRENT=$(wc -w < "$FILE" | tr -d ' ')
    TARGET=$((PAGES * WORDS_PER_PAGE))
    DIFF=$((CURRENT - TARGET))
    PCT=$(( DIFF * 100 / CURRENT ))
    printf "%-45s %8d %10d %10d %+10d %s\n" "$FILE" "$PAGES" "$CURRENT" "$TARGET" "$DIFF" "($PCT%)"
fi

FILE="01_enlightenment_roots_full.md"
PAGES=13
if [ -f "$FILE" ]; then
    CURRENT=$(wc -w < "$FILE" | tr -d ' ')
    TARGET=$((PAGES * WORDS_PER_PAGE))
    DIFF=$((CURRENT - TARGET))
    PCT=$(( DIFF * 100 / CURRENT ))
    printf "%-45s %8d %10d %10d %+10d %s\n" "$FILE" "$PAGES" "$CURRENT" "$TARGET" "$DIFF" "($PCT%)"
fi

FILE="02_classical_liberalism.md"
PAGES=12
if [ -f "$FILE" ]; then
    CURRENT=$(wc -w < "$FILE" | tr -d ' ')
    TARGET=$((PAGES * WORDS_PER_PAGE))
    DIFF=$((CURRENT - TARGET))
    PCT=$(( DIFF * 100 / CURRENT ))
    printf "%-45s %8d %10d %10d %+10d %s\n" "$FILE" "$PAGES" "$CURRENT" "$TARGET" "$DIFF" "($PCT%)"
fi

FILE="03_build_houses_full.md"
PAGES=7
if [ -f "$FILE" ]; then
    CURRENT=$(wc -w < "$FILE" | tr -d ' ')
    TARGET=$((PAGES * WORDS_PER_PAGE))
    DIFF=$((CURRENT - TARGET))
    PCT=$(( DIFF * 100 / CURRENT ))
    printf "%-45s %8d %10d %10d %+10d %s\n" "$FILE" "$PAGES" "$CURRENT" "$TARGET" "$DIFF" "($PCT%)"
fi

FILE="04_Pt1_mental_health_full.md"
PAGES=8
if [ -f "$FILE" ]; then
    CURRENT=$(wc -w < "$FILE" | tr -d ' ')
    TARGET=$((PAGES * WORDS_PER_PAGE))
    DIFF=$((CURRENT - TARGET))
    PCT=$(( DIFF * 100 / CURRENT ))
    printf "%-45s %8d %10d %10d %+10d %s\n" "$FILE" "$PAGES" "$CURRENT" "$TARGET" "$DIFF" "($PCT%)"
fi

FILE="04_Pt2_Reclaiming_Healthcare.md"
PAGES=10
if [ -f "$FILE" ]; then
    CURRENT=$(wc -w < "$FILE" | tr -d ' ')
    TARGET=$((PAGES * WORDS_PER_PAGE))
    DIFF=$((CURRENT - TARGET))
    PCT=$(( DIFF * 100 / CURRENT ))
    printf "%-45s %8d %10d %10d %+10d %s\n" "$FILE" "$PAGES" "$CURRENT" "$TARGET" "$DIFF" "($PCT%)"
fi

FILE="05_capitalism_conscience.md"
PAGES=8
if [ -f "$FILE" ]; then
    CURRENT=$(wc -w < "$FILE" | tr -d ' ')
    TARGET=$((PAGES * WORDS_PER_PAGE))
    DIFF=$((CURRENT - TARGET))
    PCT=$(( DIFF * 100 / CURRENT ))
    printf "%-45s %8d %10d %10d %+10d %s\n" "$FILE" "$PAGES" "$CURRENT" "$TARGET" "$DIFF" "($PCT%)"
fi

FILE="06_every_vote_counts.md"
PAGES=7
if [ -f "$FILE" ]; then
    CURRENT=$(wc -w < "$FILE" | tr -d ' ')
    TARGET=$((PAGES * WORDS_PER_PAGE))
    DIFF=$((CURRENT - TARGET))
    PCT=$(( DIFF * 100 / CURRENT ))
    printf "%-45s %8d %10d %10d %+10d %s\n" "$FILE" "$PAGES" "$CURRENT" "$TARGET" "$DIFF" "($PCT%)"
fi

FILE="07_europe_complicated.md"
PAGES=6
if [ -f "$FILE" ]; then
    CURRENT=$(wc -w < "$FILE" | tr -d ' ')
    TARGET=$((PAGES * WORDS_PER_PAGE))
    DIFF=$((CURRENT - TARGET))
    PCT=$(( DIFF * 100 / CURRENT ))
    printf "%-45s %8d %10d %10d %+10d %s\n" "$FILE" "$PAGES" "$CURRENT" "$TARGET" "$DIFF" "($PCT%)"
fi

FILE="08_immigration_conversations.md"
PAGES=14
if [ -f "$FILE" ]; then
    CURRENT=$(wc -w < "$FILE" | tr -d ' ')
    TARGET=$((PAGES * WORDS_PER_PAGE))
    DIFF=$((CURRENT - TARGET))
    PCT=$(( DIFF * 100 / CURRENT ))
    printf "%-45s %8d %10d %10d %+10d %s\n" "$FILE" "$PAGES" "$CURRENT" "$TARGET" "$DIFF" "($PCT%)"
fi

FILE="09_green_growth.md"
PAGES=8
if [ -f "$FILE" ]; then
    CURRENT=$(wc -w < "$FILE" | tr -d ' ')
    TARGET=$((PAGES * WORDS_PER_PAGE))
    DIFF=$((CURRENT - TARGET))
    PCT=$(( DIFF * 100 / CURRENT ))
    printf "%-45s %8d %10d %10d %+10d %s\n" "$FILE" "$PAGES" "$CURRENT" "$TARGET" "$DIFF" "($PCT%)"
fi

FILE="10_technology_good.md"
PAGES=16
if [ -f "$FILE" ]; then
    CURRENT=$(wc -w < "$FILE" | tr -d ' ')
    TARGET=$((PAGES * WORDS_PER_PAGE))
    DIFF=$((CURRENT - TARGET))
    PCT=$(( DIFF * 100 / CURRENT ))
    printf "%-45s %8d %10d %10d %+10d %s\n" "$FILE" "$PAGES" "$CURRENT" "$TARGET" "$DIFF" "($PCT%)"
fi

FILE="11_right_education.md"
PAGES=6
if [ -f "$FILE" ]; then
    CURRENT=$(wc -w < "$FILE" | tr -d ' ')
    TARGET=$((PAGES * WORDS_PER_PAGE))
    DIFF=$((CURRENT - TARGET))
    PCT=$(( DIFF * 100 / CURRENT ))
    printf "%-45s %8d %10d %10d %+10d %s\n" "$FILE" "$PAGES" "$CURRENT" "$TARGET" "$DIFF" "($PCT%)"
fi

FILE="12_your_rights_choices.md"
PAGES=8
if [ -f "$FILE" ]; then
    CURRENT=$(wc -w < "$FILE" | tr -d ' ')
    TARGET=$((PAGES * WORDS_PER_PAGE))
    DIFF=$((CURRENT - TARGET))
    PCT=$(( DIFF * 100 / CURRENT ))
    printf "%-45s %8d %10d %10d %+10d %s\n" "$FILE" "$PAGES" "$CURRENT" "$TARGET" "$DIFF" "($PCT%)"
fi

FILE="13_rights_modern_age.md"
PAGES=8
if [ -f "$FILE" ]; then
    CURRENT=$(wc -w < "$FILE" | tr -d ' ')
    TARGET=$((PAGES * WORDS_PER_PAGE))
    DIFF=$((CURRENT - TARGET))
    PCT=$(( DIFF * 100 / CURRENT ))
    printf "%-45s %8d %10d %10d %+10d %s\n" "$FILE" "$PAGES" "$CURRENT" "$TARGET" "$DIFF" "($PCT%)"
fi

FILE="14_tomorrows_tyranny.md"
PAGES=7
if [ -f "$FILE" ]; then
    CURRENT=$(wc -w < "$FILE" | tr -d ' ')
    TARGET=$((PAGES * WORDS_PER_PAGE))
    DIFF=$((CURRENT - TARGET))
    PCT=$(( DIFF * 100 / CURRENT ))
    printf "%-45s %8d %10d %10d %+10d %s\n" "$FILE" "$PAGES" "$CURRENT" "$TARGET" "$DIFF" "($PCT%)"
fi

FILE="15_guest_voices.md"
PAGES=8
if [ -f "$FILE" ]; then
    CURRENT=$(wc -w < "$FILE" | tr -d ' ')
    TARGET=$((PAGES * WORDS_PER_PAGE))
    DIFF=$((CURRENT - TARGET))
    PCT=$(( DIFF * 100 / CURRENT ))
    printf "%-45s %8d %10d %10d %+10d %s\n" "$FILE" "$PAGES" "$CURRENT" "$TARGET" "$DIFF" "($PCT%)"
fi

FILE="16_cooption_language.md"
PAGES=10
if [ -f "$FILE" ]; then
    CURRENT=$(wc -w < "$FILE" | tr -d ' ')
    TARGET=$((PAGES * WORDS_PER_PAGE))
    DIFF=$((CURRENT - TARGET))
    PCT=$(( DIFF * 100 / CURRENT ))
    printf "%-45s %8d %10d %10d %+10d %s\n" "$FILE" "$PAGES" "$CURRENT" "$TARGET" "$DIFF" "($PCT%)"
fi

FILE="17_reclaiming_liberalism.md"
PAGES=9
if [ -f "$FILE" ]; then
    CURRENT=$(wc -w < "$FILE" | tr -d ' ')
    TARGET=$((PAGES * WORDS_PER_PAGE))
    DIFF=$((CURRENT - TARGET))
    PCT=$(( DIFF * 100 / CURRENT ))
    printf "%-45s %8d %10d %10d %+10d %s\n" "$FILE" "$PAGES" "$CURRENT" "$TARGET" "$DIFF" "($PCT%)"
fi

FILE="18_liberal_lemonade.md"
PAGES=14
if [ -f "$FILE" ]; then
    CURRENT=$(wc -w < "$FILE" | tr -d ' ')
    TARGET=$((PAGES * WORDS_PER_PAGE))
    DIFF=$((CURRENT - TARGET))
    PCT=$(( DIFF * 100 / CURRENT ))
    printf "%-45s %8d %10d %10d %+10d %s\n" "$FILE" "$PAGES" "$CURRENT" "$TARGET" "$DIFF" "($PCT%)"
fi

echo "================================================================================================================"
echo ""
echo "Report generated: $(date)"
