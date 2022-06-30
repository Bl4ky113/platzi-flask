
from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from app.forms import ToDoListForm, AddToDoForm
from app.models import ToDoData, ToDoListData, ToDoData
from app.firestore_service import create_to_do_list, get_to_do_lists_by_user_title, get_to_do_list, \
get_to_dos_in_list

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

        list_id = create_to_do_list(to_do_list)
        flash(f"Created {to_do_title} To Do List", "info")

        return redirect(url_for("list_menu", to_do_list_id=list_id))

    return render_template("create_list.html", **context)
    
@lists.route('/<to_do_list_id>', methods=('GET', 'POST'))
@login_required
def list_menu (to_do_list_id):
    to_do_list_ref = get_to_do_list(to_do_list_id)
    to_dos_objs = tuple(map(lambda to_do: ToDoData(**to_do.to_dict()), get_to_dos_in_list(to_do_list_id)))
    to_do_list_obj = ToDoListData(**to_do_list_ref.to_dict(), to_dos=to_dos_objs)

    add_to_do_form = AddToDoForm()

    context = {
            "to_do_list": to_do_list_obj,
            "add_to_do_form": add_to_do_form,
            "edit": to_do_list_ref.to_dict()["user_id"] == current_user.id
            }

    return render_template('list.html', **context)

# @lists.route('/delete/<to_do_list_id>', methods=('POST'))
# @login_required
# def delete (to_do_list_id):
    # return redirect(url_for('index.html'))
