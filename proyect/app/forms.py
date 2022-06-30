
from flask_wtf import FlaskForm
from wtforms.fields import EmailField, PasswordField, SubmitField, StringField, BooleanField
from wtforms.validators import Email, DataRequired, EqualTo

class LoginForm (FlaskForm):
    email = EmailField("Email", validators=(Email(), DataRequired()))
    password = PasswordField("Password", validators=[DataRequired()])
    submit_btn = SubmitField("Log In")

class SignForm (FlaskForm):
    user_name = StringField("User Name", validators=[DataRequired()])
    email = EmailField("Email", validators=(Email(), DataRequired()))
    password = PasswordField("Password", validators=[
            DataRequired(),
            EqualTo('repeat_password', "Passwords Don't Match")
        ])
    repeat_password = PasswordField("Repeat Password", validators=(
            DataRequired(), 
            EqualTo('password', "Passwords Don't Match")
        ))
    submit_btn = SubmitField("Sign In")

class ToDoListForm (FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description')
    submit_btn = SubmitField('Create New To Do List')

class AddToDoForm (FlaskForm):
    description = StringField('Description', validators=[DataRequired()])
    status = BooleanField('Status')
    submit_btn = SubmitField('Create To Do')

class DeleteToDoForm (FlaskForm):
    submit_btn = SubmitField('Delete')

class UpdateToDoForm (FlaskForm):
    submit_btn = SubmitField('Update')
