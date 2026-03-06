from flask import Blueprint, request, jsonify
from models import *
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register/student", methods=["POST"])
def register_student():
    data = request.get_json()

    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"message": "Email already exists"}), 400

    user = User(
        name=data["name"],
        email=data["email"],
        password_hash=generate_password_hash(data["password"]),
        role="STUDENT"
    )

    db.session.add(user)
    db.session.flush()

    student_profile = StudentProfile(
        user_id=user.id,
        branch=data.get("branch"),
        cgpa=data.get("cgpa"),
        graduation_year=data.get("graduation_year")
    )

    db.session.add(student_profile)
    db.session.commit()

    return jsonify({"message": "Student registered successfully"}), 201


@auth_bp.route("/register/company", methods=["POST"])
def register_company():
    data = request.get_json()

    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"message": "Email already exists"}), 400

    user = User(
        name=data["name"],
        email=data["email"],
        password_hash=generate_password_hash(data["password"]),
        role="COMPANY"
    )

    db.session.add(user)
    db.session.flush()

    company_profile = CompanyProfile(
        user_id=user.id,
        company_name=data["company_name"],
        hr_contact=data.get("hr_contact"),
        website=data.get("website")
    )

    db.session.add(company_profile)
    db.session.commit()

    return jsonify({"message": "Company registered. Await admin approval."}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    user = User.query.filter_by(email=data["email"]).first()

    if not user:
        return jsonify({"message": "Invalid credentials"}), 401

    if not check_password_hash(user.password_hash, data["password"]):
        return jsonify({"message": "Invalid credentials"}), 401

    if not user.is_active:
        return jsonify({"message": "Account deactivated"}), 403

    access_token = create_access_token(
        identity=str(user.id),
        additional_claims={"role": user.role}
    )

    return jsonify({
        "access_token": access_token,
        "role": user.role
    })