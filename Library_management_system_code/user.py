import os
from storage import UserData

class UserManagement:
    def __init__(self,path = None) -> None:
        if path is None:
            path = os.path.abspath(__file__)
            path = os.path.dirname(path)
        if not os.path.exists(f"{path}/data"):
            os.mkdir(f"{path}/data")
        self.path = f"{path}/data"
        self.user_db = UserData(f'{self.path}/user_data.json')
    
    def get_user_details(self):
        userID = input("Enter User ID: ")
        username = input("Enter User Name: ")

        return userID,username

    def add_user(self, userID, username):
        key = userID
        value = {'username':username}
        self.user_db.write_data(key,value)

    def list_user(self):
        print(self.user_db.show_data())

    def search_user(self, attributes):
        data = self.user_db.data
        for key, value in data.items():
            if key == attributes:
                return data[key]
            else:
                for attr, attr_values in data[key].items():
                    if attr_values == attributes:
                        return [key, value]
        return