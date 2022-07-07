from app import db
from flask_login import UserMixin
from sqlalchemy import create_engine

class User(UserMixin, db.Model):
	__tablename__ = "user"
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(50), unique = True, nullable = False)
	email = db.Column(db.String(100), unique = True, nullable = False)
	password = db.Column(db.String(300), unique = True, nullable = False)

	def __repr__(self):
		return '<User %r>' % self.username

engine = create_engine('sqlite:///database.db')