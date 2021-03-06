from app import db, create_app
from flask_migrate import upgrade, migrate, init, stamp
from models import User

def deploy():
	app = create_app()
	app.app_context().push()
	db.create_all()

	init()
	stamp()
	migrate()
	upgrade()

deploy()
