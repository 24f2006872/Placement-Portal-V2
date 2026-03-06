from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import PlacementDrive, StudentProfile, Application
from extensions import db
from utils import role_required
from extensions import cache
import json
from tasks.jobs import export_student_applications

student_bp = Blueprint("student", __name__)

@student_bp.route("/drives")
@jwt_required()
@role_required("STUDENT")
def view_drives():

    cached_drives = cache.get("approved_drives")

    if cached_drives:
        return json.loads(cached_drives)

    drives = PlacementDrive.query.filter_by(status="APPROVED").all()

    result = [
        {
            "id": d.id,
            "title": d.job_title,
            "min_cgpa": d.min_cgpa
        }
        for d in drives
    ]

    cache.setex(
        "approved_drives",
        300,
        json.dumps(result)
    )

    return result

@student_bp.route("/apply/<int:drive_id>", methods=["POST"])
@jwt_required()
@role_required("STUDENT")
def apply_drive(drive_id):

    user_id = int(get_jwt_identity())

    student = StudentProfile.query.filter_by(user_id=user_id).first()

    drive = PlacementDrive.query.get_or_404(drive_id)

    if student.cgpa < drive.min_cgpa:
        return {"message": "CGPA not eligible"}, 403

    application = Application(
        student_id=student.id,
        drive_id=drive_id
    )

    db.session.add(application)
    db.session.commit()

    return {"message": "Applied successfully"}

@student_bp.route("/dashboard")
@jwt_required()
@role_required("STUDENT")
def student_dashboard():

    user_id = get_jwt_identity()
    student = StudentProfile.query.filter_by(user_id=user_id).first()

    applications = Application.query.filter_by(student_id=student.id).all()

    result = []

    for app in applications:
        result.append({
            "drive": app.drive.job_title,
            "status": app.status,
            "applied_on": app.application_date
        })

    return jsonify(result)

@student_bp.route("/search/drives")
@jwt_required()
@role_required("STUDENT")
def search_drives():

    query = request.args.get("q")

    drives = PlacementDrive.query.filter(
        PlacementDrive.job_title.ilike(f"%{query}%"),
        PlacementDrive.status == "APPROVED"
    ).all()

    return jsonify([
        {
            "id": d.id,
            "title": d.job_title,
            "min_cgpa": d.min_cgpa
        }
        for d in drives
    ])

@student_bp.route("/export", methods=["GET"])
@jwt_required()
@role_required("STUDENT")
def export_applications():

    user_id = int(get_jwt_identity())

    student = StudentProfile.query.filter_by(user_id=user_id).first()

    task = export_student_applications.delay(student.id)

    return {
        "message": "Export started",
        "task_id": task.id
    }