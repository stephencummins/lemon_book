# Automated Book Building and Publishing

This repository is configured to automatically build and publish book files to Cloudflare R2 whenever you commit changes to git.

## How it works

A post-commit git hook (`.git/hooks/post-commit`) automatically runs after every commit. This hook:

1. Generates all book formats (PDF, EPUB, DOCX, HTML, RTF, ODT)
2. Uploads them to Cloudflare R2 bucket `lemon-book/book/`

## Generated Files

Each commit generates the following files:
- **lemon_book.pdf** (95M) - Print-quality PDF with uncompressed images
- **lemon_book.epub** (51M) - E-book format for e-readers
- **lemon_book.docx** (51M) - Microsoft Word format
- **lemon_book.odt** (51M) - OpenDocument format
- **lemon_book.rtf** (101M) - Rich Text Format
- **lemon_book.html** (392K) - HTML web version

## Important Notes

- Large generated files (PDF, DOCX, EPUB, etc.) are **excluded from git** via `.gitignore`
- Only markdown source files are tracked in git
- Book files are stored in Cloudflare R2 for distribution
- Build process takes several minutes due to file sizes

## Manual Build

To manually build and upload without committing:

```bash
UPLOAD_TO_R2=true bash scripts/build_book.sh
```

To build without uploading:

```bash
bash scripts/build_book.sh
```

## Cloudflare R2 Location

All files are uploaded to:
- Bucket: `lemon-book`
- Path: `book/`

## Troubleshooting

If the post-commit hook isn't running:
1. Check it exists: `.git/hooks/post-commit`
2. Ensure it's executable: `chmod +x .git/hooks/post-commit`
3. Check wrangler is installed: `wrangler --version`

## Requirements

- pandoc (for document generation)
- MacTeX/XeLaTeX (for PDF generation)
- wrangler CLI (for Cloudflare R2 uploads)
