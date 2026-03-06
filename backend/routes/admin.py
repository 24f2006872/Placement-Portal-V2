from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from models import CompanyProfile, PlacementDrive
from extensions import db
from utils import role_required

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

    return {"message": "Drive approved"}