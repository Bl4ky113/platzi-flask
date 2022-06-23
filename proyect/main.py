
from flask import render_template, session

from app import create_app
from app.firestore_service import get_users_dicts, get_to_do_lists_dicts, get_to_do_lists, get_to_dos

app = create_app()

@app.route("/")
def index ():
    user_email = session.get("u_email")
    
    to_do_lists = get_to_do_lists()
    to_dos = [get_to_dos(to_do_list.id) for to_do_list in to_do_lists]

    context = {
            "u_email": user_email,
            "users": get_users_dicts(),
            "to_do_lists": get_to_do_lists_dicts(),
            "to_dos": to_dos
            }

    return render_template("index.html", **context)
