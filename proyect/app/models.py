
from flask_login import UserMixin

from .firestore_service import get_user_id_by_email, get_user

class UserData ():
    def __init__ (self, name, email, password):
        self.id = get_user_id_by_email(email)
        self.name = name
        self.email = email
        self.password = password

class UserModel (UserMixin):
    def __init__ (self, user_data:UserData):
        self.id = user_data.id
        self.name = user_data.name
        self.email = user_data.email
        self.password = user_data.password

    @staticmethod
    def query (user_id):
        print("email", user_id)
        user_doc = get_user(user_id)
        user_data = UserData(**user_doc.to_dict())

        return UserModel(user_data)
