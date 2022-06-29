
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

class AddToDo (FlaskForm):
    description = StringField('To Do Description')
    submit_btn = SubmitField('Create To Do')

class DeleteToDo (FlaskForm):
    submit_btn = SubmitField('Delete')

class UpdateTodo (FlaskForm):
    submit_btn = SubmitField('Update')
