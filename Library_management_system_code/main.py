# This is a deliberately poorly implemented main script for a Library Management System.
from book import BookManagement
from user import UserManagement
from storage import checkin_book, checkout_book
# import book_management
# import user_management
# import checkout_management


class Library_Management_System:
    '''This class will hold all the operation required in library'''
    
    def __init__(self):
        self.book_manage = BookManagement()
        self.user_manage = UserManagement()
    
    def manager(self,choice):
        if choice == 1:
            
            title, author, isbn, n_copies = self.book_manage.get_book_details()
            self.book_manage.add_book(title, author, isbn, n_copies)
            print("Book added.")
            return
        elif choice == 2:
            self.book_manage.list_books()
            return
        elif choice == 3:
            user_id, name = self.user_manage.get_user_details()
            self.user_manage.add_user(user_id,name)
            self.user_manage.list_user()
            print("User added.")

            return
        
        elif choice == 4:
            title = input("Enter title: ")
            self.book_manage.book_db.delete(title)

            return
        
        elif choice == 5:
            user_id = input("Enter user ID: ")
            self.user_manage.user_db.delete(user_id)

            return
        
        elif choice == 6:
            title = input("Enter title: ")
            user_id = input("Enter user ID: ")
            book_db, user_db = checkout_book(self.book_manage.book_db, self.user_manage.user_db, title, user_id)
            self.book_manage.book_db = book_db
            self.user_manage.user_db = user_db
        
        elif choice == 7:
            title = input("Enter title: ")
            user_id = input("Enter user ID: ")
            book_db, user_db = checkin_book(self.book_manage.book_db, self.user_manage.user_db, title, user_id)
            self.book_manage.book_db = book_db
            self.user_manage.user_db = user_db            

        elif choice == 8:
            self.book_manage.book_db.commit_data()
            self.user_manage.user_db.commit_data()
            print("Saved the Changes .")
            return 

        elif choice ==9:
            attributes = input("Enter attributes like title, author or ISBN, : ")
            details = self.book_manage.search_book(attributes)
            print(details) if details else print("Try with different attributes")
            return

        elif choice ==10:
            attributes = input("Enter attributes like name, user ID : ")
            details = self.user_manage.search_user(attributes)
            print(details) if details else print("Try with different attributes")
            return
        
        elif choice == 11:
            print("Exiting")
            return -1
        else:
            print("Invalid choice, please try again.")
            return

if __name__ == "__main__":
    lms = Library_Management_System()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. List Books")
        print("3. Add User")
        print("4. Delete book")
        print("5. Delete user")
        print("6. Checkout books")
        print("7. Checkin books")
        print("8. Save the Changes")
        print("9. Search the Book ")
        print("10. Search the user ")
        print("11. Exit")
        
        choice = int(input("Enter choice: "))
        if (choice >11):
            print("... Invalid Choice. Please select again ... ")
        else:
            
            record = lms.manager(choice)
            if record == -1:
                break
