from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, DataRequired, ValidationError


class SignupForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
<<<<<<< HEAD
    submit = SubmitField('Registrar')

class PostForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    content = TextAreaField('content', validators=[DataRequired()])
    
class LoginForm(FlaskForm):
    email = StringField('user email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
=======
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')
>>>>>>> fa539638d20a8a47d675ca3a3cc22c18b1b6ea78
