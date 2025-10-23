import re
import sys

def check_index_pages(index_content, max_page):
    pattern = r'\b(\d+)(?:-(\d+))?\b'
    errors = []
    matches = re.finditer(pattern, index_content)
    for match in matches:
        start_page = int(match.group(1))
        if start_page == 0:
            errors.append(f"Page number 0 is not valid: {match.group(0)}")
        if start_page > max_page:
            errors.append(f"Page number {start_page} is greater than the total number of pages ({max_page}): {match.group(0)}")
        if match.group(2):
            end_page = int(match.group(2))
            if end_page > max_page:
                errors.append(f"Page number {end_page} is greater than the total number of pages ({max_page}): {match.group(0)}")
            if start_page > end_page:
                errors.append(f"Invalid page range, start page is greater than end page: {match.group(0)}")

    if not errors:
        print("All page numbers in the index are within the valid range (1-164).")
    else:
        print("Found the following issues with the page numbers in the index:")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

if __name__ == "__main__":
    with open("book_index_with_pages.md", "r") as f:
        index_content = f.read()
    check_index_pages(index_content, 164)
