
from flask import render_template
from flask_login import current_user

from app import create_app
from app.firestore_service import get_to_do_lists_by_user_id, get_to_do_lists_except_user_id, get_to_do_lists, get_user
from app.models import ToDoListData

app = create_app()

@app.route("/")
def index ():
    context = {}

    others_lists = get_to_do_lists()

    if current_user.is_authenticated:
        user_lists = get_to_do_lists_by_user_id(current_user.id)

        if len(user_lists) >= 1:
            user_lists_objs = tuple(map(lambda to_do_list: {"author": current_user.name} | to_do_list.to_dict(), user_lists))
            user_lists_ids = tuple(map(lambda to_do_list: to_do_list.id, user_lists))
            context['user_lists'] = dict(zip(user_lists_ids, user_lists_objs))

        others_lists = get_to_do_lists_except_user_id(current_user.id)

    others_lists_objs = tuple(map(lambda to_do_list: {"author": get_user(to_do_list.to_dict()['user_id']).to_dict()['name']} | to_do_list.to_dict(), others_lists))
    others_lists_ids = tuple(map(lambda to_do_list: to_do_list.id, others_lists))

    context['others_lists'] = dict(zip(others_lists_ids, others_lists_objs))

    return render_template("index.html", **context)
