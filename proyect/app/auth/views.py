
from flask import render_template, session, flash, redirect, url_for
from flask_login import login_user, current_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from app.forms import LoginForm, SignForm
from app.firestore_service import create_user, get_user, get_user_id_by_email, create_user
from app.models import UserData, UserModel

from . import auth

@auth.route("/login", methods=("GET", "POST"))
def login ():
    if current_user.is_authenticated:
        flash("To Log In an Account, First Log Out From Your Current Session", "warning")
        return redirect(url_for("index"))

    login_form = LoginForm()

    context = {
            "login_form": login_form
            }

    if login_form.validate_on_submit():
        login_email = login_form.email.data
        login_password = login_form.password.data
        
        user_doc = get_user(get_user_id_by_email(login_email))

        if user_doc.to_dict() is None:
            flash("User Not Found", "danger")
            return redirect(url_for("auth.login"))

        if not check_password_hash(user_doc.to_dict()["password"], login_password):
            flash("Incorrect Email & Password", "danger")
            return redirect(url_for("auth.login"))

        user_data = UserData(**user_doc.to_dict())
        user = UserModel(user_data)

        login_user(user)

        flash(f"Logged as {login_email}", "info")

        return redirect(url_for("index"))

    return render_template("login.html", **context)

@auth.route("/sign_in", methods=("GET", "POST"))
def sign_in ():
    sign_form = SignForm()

    context = {
            "sign_in_form": sign_form
            }

    if sign_form.validate_on_submit():
        sign_in_email = sign_form.email.data

        if not (get_user(get_user_id_by_email(sign_in_email)).to_dict() is None):
            flash("User Email Already Exists", "danger")
            return redirect(url_for("auth.sign_in"))

        sign_in_name = sign_form.user_name.data
        sign_in_password = generate_password_hash(sign_form.password.data)

        user_data = UserData(sign_in_name, sign_in_email, sign_in_password)
        create_user(user_data)

        flash(f"Created {sign_in_email} account", "info")

        return redirect(url_for("auth.login"))

    return render_template("sign_in.html", **context)

@auth.route("/logout")
@login_required
def logout ():
    logout_user()

    flash("Logout, Come Back Soon!!!", "info")

    return redirect(url_for("index"))

