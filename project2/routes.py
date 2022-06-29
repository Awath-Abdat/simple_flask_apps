from flask import (Flask, render_template, redirect, flash, url_for, session)
from datetime import timedelta
from sqlalchemy.exc import (IntegrityError, DataError, DatabaseError, InterfaceError, InvalidRequestError)
from werkzeug.routing import BuildError
from flask_bcrypt import Bcrypt, generate_password_hash, check_password_hash
from flask_login import (UserMixin, login_user, LoginManager, current_user, logout_user, login_required)

from app import create_app, db, login_manager, bcrypt
from models import User
from forms import login_form, register_form

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

app = create_app()

@app.route("/", methods=("GET", "POST"))
def index():
	return render_template("index.html", title="Home")

@app.route("/login", methods=("GET", "POST"))
def login():
	form = login_form()
	
	if form.validate_on_submit():
		try:
			username = form.username.data
			password = form.password.data

			cuser = User.query.filter_by(username = username).first()

			if (cuser is not None and check_password_hash(cuser.password, password)):
				login_user(cuser)
				return redirect(url_for('index'))
			else:
				flash(f"Invalid credentials.", "failed")
		except Exception as e:
			flash(e, "failed")

	return render_template("authentication.html", form = form, text = "Login", title = "Login", btn_action = "Login")

@app.route("/register", methods=("GET", "POST"))
def register():
	form = register_form()

	if form.validate_on_submit():
		try:
			username = form.username.data
			email = form.email.data
			password = form.password.data
			new_user = User(username = username, email = email, password = bcrypt.generate_password_hash(password))

			db.session.add(new_user)
			db.session.commit()

			flash(f"Account created successfully.", "success")

			return redirect(url_for('login'))
		except Exception as e:
			flash(e, "failed")

	return render_template("authentication.html", form = form, text = "Register", title = "Register", btn_action = "Register")

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))

if __name__ == "__main__":
	app.run(debug = True)