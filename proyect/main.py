
from flask import render_template
from flask_login import current_user

from app import create_app
from app.firestore_service import get_to_do_lists_by_user_id

app = create_app()

@app.route("/")
def index ():
    context = {}

    return render_template("index.html", **context)
