from flask import Flask
from config import Config
from extensions import db
from models import User
from werkzeug.security import generate_password_hash

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()
        create_admin()

    return app


def create_admin():
    admin_email = "admin@ppa.com"

    existing_admin = User.query.filter_by(email=admin_email).first()

    if not existing_admin:
        admin = User(
            name="Admin",
            email=admin_email,
            password_hash=generate_password_hash("admin123"),
            role="ADMIN"
        )
        db.session.add(admin)
        db.session.commit()
        print("Admin created successfully!")