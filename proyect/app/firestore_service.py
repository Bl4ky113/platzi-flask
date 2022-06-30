import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred)

db = firestore.client()

def get_user (user_id):
    return db.collection("users").document(user_id).get()

def get_to_do_list (list_id):
    return db.collection("to_do_lists").document(list_id).get()

def get_to_do_lists ():
    return db.collection("to_do_lists").get()

def get_to_do (list_id, to_do_id):
    return db.collection("to_do_lists").document(list_id)\
            .collection("to_dos").document(to_do_id).get()

def get_user_id_by_email (user_email):
    user_list = db.collection("users").where("email", "==", user_email).get()

    if len(user_list) != 1:
        return None
    
    return user_list[0].id

def get_to_do_lists_by_user_id (user_id):
    to_do_lists = db.collection("to_do_lists").where("user_id", "==", user_id).get()

    return to_do_lists

def get_to_do_lists_except_user_id (user_id):
    return db.collection("to_do_lists").where("user_id", "!=", user_id).get()

def get_to_do_lists_by_user_title (user_id, list_title):
    to_do_list = db.collection("to_do_lists")\
            .where("user_id", "==", user_id)\
            .where("title", "==", list_title).get()

    if len(to_do_list) != 1:
        return None

    return to_do_list[0]

def get_to_dos_in_list (to_do_list_id):
    return db.collection("to_do_lists").document(to_do_list_id)\
            .collection("to_dos").get()

def create_user (user_data):
    user_ref = db.collection("users").document()
    user_ref.set({
        "name": user_data.name,
        "email": user_data.email,
        "password": user_data.password
        })

    return user_ref.id

def create_to_do_list (to_do_list_data):
    list_ref = db.collection("to_do_lists").document()
    list_ref.set({
        "title": to_do_list_data.title,
        "description": to_do_list_data.description,
        "user_id": to_do_list_data.user_id
        })

    return list_ref.id

def create_to_do (to_do_data, to_do_list_id):
    to_do_ref = db.collection("to_do_lists").document(to_do_list_id)\
            .collection("to_dos").document()

    to_do_ref.set({
        "description": to_do_data.description,
        "status": to_do_data.status
        })

    return to_do_ref.id

def update_to_do (to_do_list_id, to_do_id, **kargs):
    db.collection("to_do_lists").document(to_do_list_id)\
            .collection("to_dos").document(to_do_id).update(dict(**kargs))


def delete_to_do (to_do_list_id, to_do_id):
    to_do_ref = get_to_do(to_do_list_id, to_do_id)
    
    db.collection("to_do_lists").document(to_do_list_id)\
            .collection("to_dos").document(to_do_id).delete()

    return to_do_ref
