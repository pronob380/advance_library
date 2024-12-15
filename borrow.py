

from datetime import datetime, timedelta
import json
from save_book import save_book

def lend_book(all_books):
    try:
        with open("all_books.json", "r") as fp:
            lend_books = json.load(fp)
    except FileNotFoundError:
        lend_books = []

    book_title = input("Enter Book Title to Lend: ")
    borrower_name = input("Enter Borrower's Name: ")
    borrower_phone = input("Enter Borrower's Phone Number: ")


    for book in all_books:
        if book['title'].lower() == book_title.lower():
            if int(book["quatity"]) > 0:
                borrow_date = datetime.now()
                due_date = borrow_date + timedelta(days=3)
                book["quatity"] = str(int(book["quatity"]) - 1)
                save_book(all_books)
                lend_book_info = {
                    "borrower_name": borrower_name,
                    "borrower_phone": borrower_phone,
                    "book_title": book_title,
                    "borrow_date": borrow_date.strftime("%d-%m-%Y"),
                    "due_date": due_date.strftime("%d-%m-%Y")
                }

                lend_books.append(lend_book_info)
                with open("lend_books.json", "w") as fp:
                    json.dump(lend_books, fp, indent=4)

                print(f"Book '{book_title}' has been lent to {borrower_name}. Due date: {due_date.strftime('%d-%m-%Y')}")
                return

    print(f"Book '{book_title}' is not available .")
