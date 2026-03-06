from flask import Flask
from flask_cors import CORS
from config import Config
from extensions import db, jwt
from models import User
from werkzeug.security import generate_password_hash
from routes.auth import auth_bp
from routes.admin import admin_bp
from routes.company import company_bp
from routes.student import student_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(auth_bp, url_prefix="/auth")

    CORS(app)

    db.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        db.create_all()
        create_admin()


    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.register_blueprint(company_bp, url_prefix="/company")
    app.register_blueprint(student_bp, url_prefix="/student")

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


