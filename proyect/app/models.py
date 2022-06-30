
from flask_login import UserMixin

from .firestore_service import get_user_id_by_email, get_user

class UserData ():
    def __init__ (self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

class UserModel (UserMixin):
    def __init__ (self, user_data:UserData):
        self.id = get_user_id_by_email(user_data.email)
        self.name = user_data.name
        self.email = user_data.email
        self.password = user_data.password

    @staticmethod
    def query (user_id):
        user_doc = get_user(user_id)
        user_data = UserData(**user_doc.to_dict())

        return UserModel(user_data)

class ToDoListData ():
    def __init__ (self, title, description, user_id, to_dos=[]):
        self.title = title
        self.description = description
        self.user_id = user_id
        self.to_dos = to_dos

class ToDoData ():
    def __init__ (self, description, status):
        self.description = description
        self.status = status
