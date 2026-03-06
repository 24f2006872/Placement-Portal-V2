from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import PlacementDrive, StudentProfile, Application
from extensions import db
from utils import role_required

student_bp = Blueprint("student", __name__)

@student_bp.route("/drives")
@jwt_required()
@role_required("STUDENT")
def view_drives():

    drives = PlacementDrive.query.filter_by(status="APPROVED").all()

    result = []
    for d in drives:
        result.append({
            "id": d.id,
            "title": d.job_title,
            "min_cgpa": d.min_cgpa
        })

    return jsonify(result)

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

