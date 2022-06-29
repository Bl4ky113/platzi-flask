
from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from app.forms import ToDoListForm
from app.models import ToDoListData
from app.firestore_service import create_to_do_list, get_to_do_lists_by_user_title

from . import lists

@lists.route('/create', methods=('GET', 'POST'))
@login_required
def create ():
    to_do_list_form = ToDoListForm()

    context = {
            "to_do_list_form": to_do_list_form
            }

    if to_do_list_form.validate_on_submit():
        to_do_title = to_do_list_form.title.data
        to_do_description = to_do_list_form.description.data
        to_do_author = current_user.id

        to_do_list = ToDoListData(
                to_do_title,
                to_do_description,
                to_do_author
                )

        if not (get_to_do_lists_by_user_title(to_do_author, to_do_title) is None):
            flash("To Do List already Exists", "danger")
            return redirect(url_for("lists.create"))

        create_to_do_list(to_do_list)
        flash(f"Created {to_do_title} To Do List", "info")

        return redirect(url_for("index"))

    return render_template("create_list.html", **context)
    
