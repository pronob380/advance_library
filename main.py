from add_book import add_books
from view_book import view_book
from update_book import update_book
from remove_book import remove_book
from borrow import lend_book
from return_book import return_book


all_books =[]

while True:
    print("Welcome To Library Management System")
    print("0. Exit")
    print("1. Add Book ")
    print("2. View All Book")
    print("3. Update Book")
    print("4. Remove Book")
    print("5. Borrow Book")
    print("6. Return Book")


    menu = input("Enter The Number: ")


    if menu == "0":
        print("Thanks For Using Library Management System")
        break

    elif menu == "1":
       add_books(all_books)

    elif menu == "2":
     view_book(all_books)

    elif menu == "3":
       view_book(all_books)
       update_book(all_books)

    elif menu == "4":
         view_book(all_books)
         remove_book(all_books)

    elif menu =="5":
            lend_book(all_books)

    elif menu == "6": 
        return_book(all_books)


    else:
       print("Invalid Choice ")     

