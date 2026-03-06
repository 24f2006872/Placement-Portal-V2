from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from models import CompanyProfile, PlacementDrive
from extensions import db
from utils import role_required
from models import *
from extensions import cache
import json

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/companies")
@jwt_required()
@role_required("ADMIN")
def view_companies():
    companies = CompanyProfile.query.all()

    data = []
    for c in companies:
        data.append({
            "id": c.id,
            "company_name": c.company_name,
            "approval_status": c.approval_status
        })

    return jsonify(data)

@admin_bp.route("/company/<int:id>/approve", methods=["PUT"])
@jwt_required()
@role_required("ADMIN")
def approve_company(id):
    company = CompanyProfile.query.get_or_404(id)

    company.approval_status = "APPROVED"
    db.session.commit()

    return {"message": "Company approved"}

@admin_bp.route("/company/<int:id>/reject", methods=["PUT"])
@jwt_required()
@role_required("ADMIN")
def reject_company(id):
    company = CompanyProfile.query.get_or_404(id)

    company.approval_status = "REJECTED"
    db.session.commit()

    return {"message": "Company rejected"}

@admin_bp.route("/drive/<int:id>/approve", methods=["PUT"])
@jwt_required()
@role_required("ADMIN")
def approve_drive(id):

    drive = PlacementDrive.query.get_or_404(id)

    drive.status = "APPROVED"

    db.session.commit()

    cache.delete("approved_drives")

    return {"message": "Drive approved"}

@admin_bp.route("/dashboard")
@jwt_required()
@role_required("ADMIN")
def admin_dashboard():

    cached_data = cache.get("admin_dashboard")

    if cached_data:
        return json.loads(cached_data)

    total_students = StudentProfile.query.count()
    total_companies = CompanyProfile.query.count()
    total_drives = PlacementDrive.query.count()
    total_applications = Application.query.count()

    result = {
        "students": total_students,
        "companies": total_companies,
        "drives": total_drives,
        "applications": total_applications
    }

    cache.setex(
        "admin_dashboard",
        600,
        json.dumps(result)
    )

    return result

@admin_bp.route("/search/companies")
@jwt_required()
@role_required("ADMIN")
def search_companies():

    query = request.args.get("q")

    companies = CompanyProfile.query.filter(
        CompanyProfile.company_name.ilike(f"%{query}%")
    ).all()

    return jsonify([
        {
            "id": c.id,
            "company_name": c.company_name,
            "status": c.approval_status
        }
        for c in companies
    ])

@admin_bp.route("/search/students")
@jwt_required()
@role_required("ADMIN")
def search_students():

    query = request.args.get("q")

    students = StudentProfile.query.join(User).filter(
        User.name.ilike(f"%{query}%")
    ).all()

    return jsonify([
        {
            "id": s.id,
            "name": s.user.name,
            "branch": s.branch,
            "cgpa": s.cgpa
        }
        for s in students
    ])