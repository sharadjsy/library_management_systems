'''This class is to manage books like add, update, delete, list, and search by various attributes like title,
author or ISBN'''
import os
from storage import BookData

class BookManagement():
    def __init__(self,path = None) -> None:
        if path is None:
            path = os.path.abspath(__file__)
            path = os.path.dirname(path)
        if not os.path.exists(f"{path}/data"):
            os.mkdir(f"{path}/data")
        self.path = f"{path}/data"
        self.book_db = BookData(f'{self.path}/book_data.json')
        pass

    def get_book_details(self):
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        no_of_copies = int(input("Enter availability: "))

        return title,author,isbn, no_of_copies

    def add_book(self, title, author, isbn, no_of_copies):
        key = title
        value = {'author':author,'isbn':isbn, 'copies': no_of_copies}
        self.book_db.write_data(key,value)

    def list_books(self):
        print(self.book_db.show_data())

    def search_book(self, attributes):
        data = self.book_db.data
        for key, value in data.items():
            if key == attributes:
                return data[key]
            else:
                for attr, attr_values in data[key].items():
                    if attr_values == attributes:
                        return [key, value]
        return

        

