import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred)

db = firestore.client()

def get_users_dicts ():
    return [user.to_dict() for user in db.collection("users").get()]

def get_users ():
    return [user for user in db.collection("users").get()]

def get_to_do_lists_dicts ():
    return [to_do_list.to_dict() for to_do_list in db.collection("to_do_lists").get()]

def get_to_do_lists ():
    return [to_do_list for to_do_list in db.collection("to_do_lists").get()]

def get_to_dos (to_do_list_id):
    return [to_do.to_dict() for to_do in \
            db.collection("to_do_lists")\
            .document(to_do_list_id)\
            .collection("to_do")\
            .get()
            ]

