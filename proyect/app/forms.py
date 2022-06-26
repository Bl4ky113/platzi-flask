
from flask_wtf import FlaskForm
from wtforms.fields import EmailField, PasswordField, SubmitField, StringField
from wtforms.validators import Email, DataRequired, EqualTo

class LoginForm (FlaskForm):
    email = EmailField("Email", validators=(Email(), DataRequired()))
    password = PasswordField("Password", validators=[DataRequired()])
    submit_btn = SubmitField("Log In")

class SignForm (FlaskForm):
    user_name = StringField("User Name", validators=[DataRequired()])
    email = EmailField("Email", validators=(Email(), DataRequired()))
    password = PasswordField("Password", validators=[DataRequired()])
    repeat_password = PasswordField("Repeat Password", validators=(
            DataRequired(), 
            EqualTo(password, "Passwords Don't Match")
        ))
    submit_btn = SubmitField("Log In")
