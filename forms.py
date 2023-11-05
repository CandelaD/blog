from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, DataRequired, ValidationError, EqualTo


class SignupForm(FlaskForm):
    username = StringField('user name')
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_passwsword = PasswordField('confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrer')

class PostForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    content = TextAreaField('content', validators=[DataRequired()])
    
class LoginForm(FlaskForm):
    email = StringField('user email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
