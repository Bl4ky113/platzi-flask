
from flask import render_template, session
from flask_login import login_required, current_user

from app import create_app

app = create_app()

@app.route("/")
@login_required
def index ():
    user_email = current_user.email

    context = {
            "u_email": user_email
            }

    return render_template("index.html", **context)
