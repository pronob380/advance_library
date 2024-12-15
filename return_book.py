import json
from save_book import save_book


def return_book(all_books):
    try:
        with open("lend_books.json", "r") as fp:
            lend_books = json.load(fp)
    except FileNotFoundError:
        lend_books = []

    book_title = input("Enter Book Title to Return: ")

    for lend in lend_books:
        if lend["book_title"].lower() == book_title.lower():
            for book in all_books:
                if book["title"].lower() == book_title.lower():
                    book["quatity"] = str(int(book["quatity"]) + 1)
                    save_book(all_books)
                    lend_books.remove(lend)
                    with open("lend_books.json", "w") as fp:
                        json.dump(lend_books, fp, indent=4)

                    print(f"Book '{book_title}' has been returned successfully.")
                    return

    print(f"No lending record found for '{book_title}'.")
