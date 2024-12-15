from save_book import save_book
  


def remove_book(all_books):
    search_book = input("Enter Book Title to Delete: ")
    for book in all_books:
        if book["title"] == search_book:
            all_books.remove(book)
            save_book(all_books)
            print("Book Deleted Successfully")
            return all_books
    
    print("Book Not Found")
