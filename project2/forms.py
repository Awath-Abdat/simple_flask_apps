from wtforms import (StringField, PasswordField, BooleanField, IntegerField, DateField, TextAreaField)

from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, EqualTo, Email, Regexp
import email_validator
from flask_login import current_user
from wtforms import ValidationError, validators
from models import User

class register_form(FlaskForm):
	username = StringField(validators = [InputRequired(), Length(3, 50, "Invalid Username"), Regexp("^[A-Za-z][A-Za-z0-9_.]*$", 0, "Usernames must only have letters, numbers, and underscores")])
	email = StringField(validators = [InputRequired(), Length(1, 100, "Invalid email length"), Email()])
	password = PasswordField(validators = [InputRequired(), Length(8, 72, "Invalid password length")])
	confirm_password = PasswordField(validators = [InputRequired(), Length(8, 72), EqualTo("password", message="Passwords don't match")])

	def validate_email(self, email):
		if(User.query.filter_by(email = email.data).first()):
			raise ValidationError("Email already in use")

	def validate_username(self, username):
		if(User.query.filter_by(username = username.data).first()):
			raise ValidationError("Username already in use")

class login_form(FlaskForm):
	username = StringField(validators = [InputRequired(), Length(3, 50)])
	password = PasswordField(validators = [InputRequired(), Length(8, 72)])