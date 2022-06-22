
from flask_wtf import FlaskForm
from wtforms.fields import EmailField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired 

class LoginForm (FlaskForm):
    email = EmailField("Email", validators=(Email(), DataRequired()))
    password = PasswordField("Password", validators=[DataRequired()])
    submit_btn = SubmitField("Log In")
