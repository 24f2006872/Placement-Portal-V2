from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import CompanyProfile, PlacementDrive, Application
from extensions import db
from utils import role_required
from datetime import datetime

company_bp = Blueprint("company", __name__)


@company_bp.route("/drive/create", methods=["POST"])
@jwt_required()
@role_required("COMPANY")
def create_drive():

    user_id = get_jwt_identity()
    company = CompanyProfile.query.filter_by(user_id=user_id).first()

    if company.approval_status != "APPROVED":
        return {"message": "Company not approved"}, 403

    data = request.get_json()

    deadline_str = data.get("deadline")

    deadline = None
    if deadline_str:
        deadline = datetime.strptime(deadline_str, "%Y-%m-%d")

    drive = PlacementDrive(
        company_id=company.id,
        job_title=data["job_title"],
        job_description=data.get("job_description"),
        min_cgpa=data.get("min_cgpa"),
        eligible_branch=data.get("eligible_branch"),
        eligible_year=data.get("eligible_year"),
        application_deadline=deadline,
        status="PENDING")

    db.session.add(drive)
    db.session.commit()

    return {"message": "Drive created. Await admin approval"}

@company_bp.route("/drives")
@jwt_required()
@role_required("COMPANY")
def view_drives():

    user_id = get_jwt_identity()
    company = CompanyProfile.query.filter_by(user_id=user_id).first()

    drives = PlacementDrive.query.filter_by(company_id=company.id).all()

    result = []
    for d in drives:
        result.append({
            "id": d.id,
            "title": d.job_title,
            "status": d.status
        })

    return jsonify(result)


@company_bp.route("/applications/<int:drive_id>")
@jwt_required()
@role_required("COMPANY")
def view_applications(drive_id):

    applications = Application.query.filter_by(drive_id=drive_id).all()

    result = []
    for a in applications:
        result.append({
            "student_id": a.student_id,
            "status": a.status
        })

    return jsonify(result)

@company_bp.route("/application/<int:id>/update", methods=["PUT"])
@jwt_required()
@role_required("COMPANY")
def update_status(id):

    data = request.get_json()

    app = Application.query.get_or_404(id)
    app.status = data["status"]

    db.session.commit()

    return {"message": "Application updated"}

@company_bp.route("/dashboard")
@jwt_required()
@role_required("COMPANY")
def company_dashboard():

    user_id = get_jwt_identity()
    print("USER ID:", user_id)
    company = CompanyProfile.query.filter_by(user_id=user_id).first()
    print("COMPANY:", company)
    drives = PlacementDrive.query.filter_by(company_id=company.id).all()

    result = []

    for d in drives:
        applicant_count = Application.query.filter_by(drive_id=d.id).count()

        result.append({
            "drive_id": d.id,
            "title": d.job_title,
            "status": d.status,
            "applicants": applicant_count
        })

    return jsonify(result)