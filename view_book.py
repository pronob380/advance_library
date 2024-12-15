

import json

def view_book(all_books):
    with open("all_book.json", "r") as fp:
        all_books = json.load(fp)

    if all_books != []:
        for i, book in enumerate (all_books, start=1):
            print(f"{i}. Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | Year: {book['year']} | Price: {book['price']} | Quantity: {book['quatity']} | Book Added At: {book['bookAdd']}")
    else:
        print("No Book found.")

 

