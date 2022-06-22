
from flask import render_template, session
from app import create_app

app = create_app()

@app.route("/")
def index ():
    user_email = session.get("u_email")

    context = {
            "u_email": user_email
            }

    return render_template("index.html", **context)
