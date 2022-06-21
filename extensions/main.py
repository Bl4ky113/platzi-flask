
from flask import Flask, render_template, redirect, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import EmailField, SubmitField
from wtforms.validators import Email, DataRequired
import unittest

app = Flask(__name__)
app.config["SECRET_KEY"] = "HeichIElElOu"
bootstrap = Bootstrap(app)

class SubscribeForm (FlaskForm):
    email = EmailField("Email", validators=(Email(), DataRequired()))
    submit_btn = SubmitField("Subscribe")

@app.cli.command()
def test ():
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(tests)

@app.route("/", methods=("GET", "POST"))
def index ():
    subscribe_form = SubscribeForm()
    subscribed_email = session.get("sub_email")

    context = {
            "subscribe_form": subscribe_form,
            "subscribed_email": subscribed_email
            }

    if subscribe_form.validate_on_submit():
        subscribed_email = subscribe_form.email.data
        session["sub_email"] = subscribed_email
        
        flash("Thanks for Subscribing to my Blog")

        return redirect(url_for("index"))

    return render_template("base.html", **context)
