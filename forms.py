from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class RegistrationForm(FlaskForm):
	username = StringField('Username', 
		validators = [DataRequired(), Length(min = 2, max = 20)])
	email = StringField('Email',
	    validators = [DataRequired(), Email()])
	password = PasswordField('password', validators = [DataRequired()])
	confirm_password = PasswordField('confirmpassword', 
		validators = [DataRequired(), EqualTo('password')])
	submit = SubmitField('Signup')

class LoginForm(FlaskForm):
	username = StringField('Username', 
		validators = [DataRequired(), Length(min = 2, max = 20)])
	email = StringField('Email',
	    validators = [DataRequired(), Email()])
	password = PasswordField('password', validators = [DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')


class PostForm(FlaskForm):
	title = StringField('Title', validators = [DataRequired()])
	content = TextAreaField('content', validators = [DataRequired()])
	submit = SubmitField('Post')

class AccountForm(FlaskForm):
	username = StringField('Username', validators = [DataRequired(), Length(min = 2, max = 20)])
	email = StringField('Email',validators = [DataRequired(), Email()])


