import random
from datetime import datetime
from save_book import save_book,load_book


def add_books(all_books):
    title = input("Enter Book Title: ")
    author =input("Enter Author Name:  ")
    year = input("Enter Publishing Year: ")
    price = int(input("Enter Book Price: "))
    quantity = input("Enter Book Quantity: ")



    isbn = random.randint(10000, 99999)
    bookAdd = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


    all_books = load_book()
    book={
        "title": title,
        "author": author,
        "isbn": isbn,
        "year" : year,
        "price": price,
        "quatity": quantity,
        "bookAdd": bookAdd,
       
    }

    all_books.append(book)
    save_book(all_books)

    print("Book Add Sucessfully ")

    return all_books
    
