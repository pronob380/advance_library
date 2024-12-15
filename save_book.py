import json


def save_book(all_books):
    with open("all_book.json", "w") as fp:
        json.dump(all_books, fp, indent=4)



def load_book(all_books):
    with open("all_book.json", "r") as fp:
        json.load(all_books, fp)

    return all_books           
