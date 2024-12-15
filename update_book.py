

from save_book import save_book



def update_book(all_books):

    search_book = input("Enter Book Title To Update: ")
    for book in all_books:
        if book['title'] == search_book:
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            year = input("Enter Publishing Year: ")
            price = input("Enter Book Price: ")
            quantity = input("Enter Book Quantity: ")
            

            book['title']=title
            book["author"]=author
            book["year"]=year
            book["price"]=price
            book["quantity"]=quantity
            

            save_book(all_books)
            print("Book Updated Successfully")

            return all_books

    print("Book Not Found ")    


