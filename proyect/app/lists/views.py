
from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from app.forms import ToDoListForm, AddToDoForm, DeleteToDoForm, UpdateToDoForm
from app.models import ToDoData, ToDoListData, ToDoData
from app.firestore_service import create_to_do_list, create_to_do, delete_to_do, \
        get_to_do_lists_by_user_title, get_to_do_list, get_to_dos_in_list, get_to_do, get_user, \
        delete_to_do, update_to_do

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

        return redirect(url_for("lists.list_menu", to_do_list_id=list_id))

    return render_template("create_list.html", **context)
    
@lists.route('/<to_do_list_id>', methods=('GET', 'POST'))
@login_required
def list_menu (to_do_list_id):
    to_do_list_ref = get_to_do_list(to_do_list_id)

    to_dos_list = get_to_dos_in_list(to_do_list_id)
    to_dos_objs = tuple(map(lambda to_do: ToDoData(**to_do.to_dict()), to_dos_list))
    to_dos_ids = tuple(map(lambda to_do: to_do.id, to_dos_list))

    to_do_list_obj = ToDoListData(**to_do_list_ref.to_dict(), to_dos=dict(zip(to_dos_ids, to_dos_objs)))
    to_do_list_author = get_user(to_do_list_ref.to_dict()['user_id']).to_dict()

    add_to_do_form = AddToDoForm()
    del_to_do_form = DeleteToDoForm()
    update_to_do_form = UpdateToDoForm()

    context = {
            "to_do_list": to_do_list_obj,
            "to_do_list_author": to_do_list_author['name'] + "  |  " + to_do_list_author['email'],
            "edit": to_do_list_ref.to_dict()["user_id"] == current_user.id,
            "to_do_list_id": to_do_list_ref.id,
            "add_to_do_form": add_to_do_form,
            "delete_to_do_form": del_to_do_form,
            "update_to_do_form": update_to_do_form
            }

    return render_template('list.html', **context)

@lists.route('/add_to_do/<to_do_list_id>', methods=['POST'])
@login_required
def add_to_do_to_list (to_do_list_id):
    to_do_list_ref = get_to_do_list(to_do_list_id)
    add_to_do_form = AddToDoForm()

    if to_do_list_ref.to_dict()['user_id'] != current_user.id:
        flash("You Are Not Allowed to Change This To Do List", "warning")
        return redirect(url_for('index'))

    if add_to_do_form.validate_on_submit():
        to_do_description = add_to_do_form.description.data
        to_do_status = add_to_do_form.status.data
        to_do = ToDoData(to_do_description, to_do_status)

        to_do_id = create_to_do(to_do, to_do_list_id)

        flash('Added New To Do to Your List', 'info')

    return redirect(url_for('lists.list_menu', to_do_list_id=to_do_list_id))

@lists.route('/delete_to_do/<to_do_list_id>/<to_do_id>', methods=["POST"])
@login_required
def delete_to_do_in_list (to_do_list_id, to_do_id):
    to_do_list_ref = get_to_do_list(to_do_list_id)
    del_to_do_form = DeleteToDoForm()

    if to_do_list_ref.to_dict()['user_id'] != current_user.id:
        flash("You Are Not Allowed to Change This To Do List", "warning")
        return redirect(url_for('index'))

    if del_to_do_form.validate_on_submit():
        deleted_to_do = delete_to_do(to_do_list_id, to_do_id)
        flash('Deleted To Do from Your List', "info")

    return redirect(url_for('lists.list_menu', to_do_list_id=to_do_list_id))

@lists.route('/update_to_do/<to_do_list_id>/<to_do_id>', methods=["POST"])
@login_required
def update_to_do_in_list (to_do_list_id, to_do_id):
    to_do_list_ref = get_to_do_list(to_do_list_id)
    update_to_do_form = UpdateToDoForm()

    if to_do_list_ref.to_dict()['user_id'] != current_user.id:
        flash("You Are Not Allowed to Change This To Do List", "warning")
        return redirect(url_for('index'))

    if update_to_do_form.validate_on_submit():
        to_do_status = not get_to_do(to_do_list_id, to_do_id).to_dict()['status']
        update_to_do(to_do_list_id, to_do_id, status=to_do_status)
        flash('Updated To Do From Your List', 'info')

    return redirect(url_for('lists.list_menu', to_do_list_id=to_do_list_id))

