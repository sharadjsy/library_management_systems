import json
import os

class DataBase:
    def __init__(self,path) -> None:
        self.path = path
        with open(path,'r') as f:
            # data = f.read()
            data = json.load(f)
        self.data = data

    def get_data(self,key):
        return self.data.get(key, None)
    
    def write_data(self,key,value):
        self.data[key] = value

    def commit_data(self):
        with open(self.path,'w') as f:
            f.write(json.dumps(self.data,indent=1))
    
    def delete(self, key):
        del self.data[key]
    
    def show_data(self):
        return json.dumps(self.data, indent=1)

class BookData(DataBase):
    def __init__(self, path) -> None:
        if not os.path.exists(path):
            with open(path,'w') as f:
                f.write("{}")
        super().__init__(path)

    def get_data(self, key):
        book_data = super().get_data(key)
        if book_data is None:
            print("Book Not Available")
        else:
            return book_data
    
    def write_data(self, key, value):
        book_data = super().get_data(key)
        if book_data is None:
            super().write_data(key, value)
        else:
            print("Book already exists")
    
    def delete(self, key):
        book_data = super().get_data(key)
        if book_data is None:
            print("Book doesn't exist")
        
        else:
            super().delete(key)


class UserData(DataBase):
    def __init__(self, path) -> None:
        if not os.path.exists(path):
            with open(path,'w') as f:
                f.write("{}")
        super().__init__(path)

    def get_data(self, key):
        user_data = super().get_data(key)
        if user_data is None:
            print("User not found")
        else:
            return user_data
    
    def write_data(self, key, value):
        user_data = super().get_data(key)
        if user_data is None:
            super().write_data(key, value)
        else:
            print("User already exists")
    
    def delete(self, key):
        user_data = super().get_data(key)
        if user_data is None:
            print("User doesn't exist")
        
        else:
            super().delete(key)


def checkout_book(book_db, user_db, title, user_id):
    book_data = book_db.get_data(title)
    if book_data is None:
        return book_db, user_db
    
    copies = book_data['copies']
    if copies == 0:
        print("NO copies Availble")

    book_data['copies'] -= 1
    
    user_data = user_db.get_data(user_id)
    if user_data is None:
        return book_db, user_db
    
    if user_data.get('books issued', None) is not None:
        user_data['books issued'].append(title)
    
    else:
        user_data['books issued'] = [title]
    
    book_db.write_data(title, book_data)
    user_db.write_data(user_id, user_data)


    return book_db, user_db

def checkin_book(book_db, user_db, title, user_id):
    book_data = book_db.get_data(title)
    if book_data is None:
        return book_db, user_db


    book_data['copies'] += 1
    
    user_data = user_db.get_data(user_id)
    if user_data is None:
        return book_db, user_db
    
    if user_data.get('books issued', None) is None:
        print("User issued no books")
        return book_db, user_db
    
    if title not in user_data['books issued']:
        print("User didn't issue this book")
    
    idx = user_data['books issued'].index(title)
    del user_data['books issued'][idx]

    
    book_db.write_data(title, book_data)
    user_db.write_data(user_id, user_data)


    return book_db, user_db

