# PDF Build Order - The Lemon Book

## Complete File Order for PDF Assembly

### Front Matter (Pages i-iv)
1. **00_front_matter.md** - Pages i-ii
   - Title page
   - Dedication
   - About the Author
   - Acknowledgements

2. **00_introduction.md** - Pages iii-iv
   - Introduction: When Life Gives You Lemons

3. **table_of_contents.md** - After page iv (unnumbered or pages v-vi)
   - Complete table of contents with page numbers

---

### Part I: The Liberal Tradition (Pages 1-23)

4. **01_enlightenment_roots.md** - Pages 1-11
   - Chapter 1: The Enlightenment Roots of Liberalism

5. **02_classical_liberalism.md** - Pages 12-23
   - Chapter 2: Classical Liberalism and its Evolution

---

### Part II: Contemporary Challenges (Pages 24-91)

6. **03_build_houses_full.md** - Pages 24-30
   - Chapter 3: Actually, We Can Build Houses

7. **04_Pt1_mental_health_full.md** - Pages 31-38
   - Chapter 4 Part I: Your Mental Health Matters

8. **04_Pt2_Reclaiming_Healthcare.md** - Pages 39-48
   - Chapter 4 Part II: Reclaiming Healthcare

9. **05_capitalism_conscience.md** - Pages 49-56
   - Chapter 5: Capitalism with a Conscience

10. **06_every_vote_counts.md** - Pages 57-63
    - Chapter 6: Every Vote Should Count

11. **07_europe_complicated.md** - Pages 64-69
    - Chapter 7: Europe: It's Complicated

12. **08_immigration_conversations.md** - Pages 70-83
    - Chapter 8: Immigration: Honest Conversations

13. **09_green_growth.md** - Pages 84-91
    - Chapter 9: The Lime Chapter: Green Growth, Not Green Grief

---

### Part III: Digital Age Liberalism (Pages 92-136)

14. **10_technology_good.md** - Pages 92-107
    - Chapter 10: Technology for Good

15. **11_right_education.md** - Pages 108-113
    - Chapter 11: The Right to Education

16. **12_your_rights_choices.md** - Pages 114-121
    - Chapter 12: Your Rights, Your Choices

17. **13_rights_modern_age.md** - Pages 122-129
    - Chapter 13: Rights in the Modern Age

18. **14_tomorrows_tyranny.md** - Pages 130-136
    - Chapter 14: Tomorrow's Tyranny

---

### Part IV: The Path Forward (Pages 137-177)

19. **15_guest_voices.md** - Pages 137-144
    - Chapter 15: Guest Voices

20. **16_cooption_language.md** - Pages 145-154
    - Chapter 16: The Power of Words

21. **17_reclaiming_liberalism.md** - Pages 155-163
    - Chapter 17: Reclaiming Authentic Liberalism

22. **18_liberal_lemonade.md** - Pages 164-177
    - Chapter 18: Liberal Lemonade

---

### Back Matter (Pages 178+)

23. **book_index_with_pages.md** - Starting page 178
    - Comprehensive index

24. **Bibliography** (to be created) - TBD
    - References and sources

25. **Colophon** (to be created) - TBD
    - Publishing information
    - Typeface and design notes
    - Creation process

---

## Total Files: 25

### Current Status:
- ✅ Files 1-22: Complete with page numbers
- ⏳ File 23: Index complete with page numbers
- ❌ File 24: Bibliography needs to be created
- ❌ File 25: Colophon needs to be created

---

## PDF Assembly Options

### Option 1: Pandoc
```bash
pandoc 00_front_matter.md 00_introduction.md table_of_contents.md \
  01_enlightenment_roots.md 02_classical_liberalism.md \
  03_build_houses_full.md 04_Pt1_mental_health_full.md \
  04_Pt2_Reclaiming_Healthcare.md 05_capitalism_conscience.md \
  06_every_vote_counts.md 07_europe_complicated.md \
  08_immigration_conversations.md 09_green_growth.md \
  10_technology_good.md 11_right_education.md \
  12_your_rights_choices.md 13_rights_modern_age.md \
  14_tomorrows_tyranny.md 15_guest_voices.md \
  16_cooption_language.md 17_reclaiming_liberalism.md \
  18_liberal_lemonade.md book_index_with_pages.md \
  -o "The_Lemon_Book.pdf" \
  --pdf-engine=xelatex \
  --toc --toc-depth=2 \
  -V geometry:margin=1in \
  -V fontsize=11pt \
  -V documentclass=book
```

### Option 2: Concatenate First, Then Convert
```bash
cat 00_front_matter.md 00_introduction.md ... > complete_book.md
pandoc complete_book.md -o The_Lemon_Book.pdf --pdf-engine=xelatex
```

### Option 3: LaTeX with Custom Formatting
For professional book layout with:
- Custom headers/footers
- Page number positioning
- Chapter styling
- Professional typography

---

## Notes

1. **Page Numbers**: The HTML page markers will need special handling in PDF conversion
2. **Images**: All images in `images/` directory need to be embedded
3. **Page Breaks**: May need to add explicit page breaks between chapters
4. **Formatting**: Consider whether to keep HTML page markers or remove them for PDF

---

## Recommended Next Steps

1. Create bibliography.md
2. Create colophon.md
3. Test PDF generation with one chapter
4. Create full PDF assembly script
5. Review and adjust formatting
6. Generate final PDF

<div style="page-break-after: always;"></div>
