#!/bin/bash
# Generate PDF of The Lemon Book using Pandoc

echo "======================================================================"
echo "GENERATING PDF: THE LEMON BOOK"
echo "======================================================================"
echo ""

pandoc \
  00_front_matter.md \
  00_introduction.md \
  table_of_contents.md \
  01_enlightenment_roots.md \
  02_classical_liberalism.md \
  03_build_houses_full.md \
  04_Pt1_mental_health_full.md \
  04_Pt2_Reclaiming_Healthcare.md \
  05_capitalism_conscience.md \
  06_every_vote_counts.md \
  07_europe_complicated.md \
  08_immigration_conversations.md \
  09_green_growth.md \
  10_technology_good.md \
  11_right_education.md \
  12_your_rights_choices.md \
  13_rights_modern_age.md \
  14_tomorrows_tyranny.md \
  15_guest_voices.md \
  16_cooption_language.md \
  17_reclaiming_liberalism.md \
  18_liberal_lemonade.md \
  book_index_with_pages.md \
  bibliography.md \
  colophon.md \
  -o "The_Lemon_Book.pdf" \
  --pdf-engine=xelatex \
  -V geometry:margin=1in \
  -V fontsize=11pt \
  -V documentclass=book \
  -V papersize=a4 \
  -V linestretch=1.4 \
  --metadata title="The Lemon Book: Refreshing Liberalism for the 21st Century" \
  --metadata author="Stephen Cummins" \
  --metadata date="2025" \
  --number-sections \
  --highlight-style=tango

if [ $? -eq 0 ]; then
    echo ""
    echo "======================================================================"
    echo "✅ PDF GENERATED SUCCESSFULLY"
    echo "======================================================================"
    echo "Output: The_Lemon_Book.pdf"
    ls -lh The_Lemon_Book.pdf
else
    echo ""
    echo "======================================================================"
    echo "❌ PDF GENERATION FAILED"
    echo "======================================================================"
    exit 1
fi
