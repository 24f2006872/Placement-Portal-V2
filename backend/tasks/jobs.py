from celery_app import celery
from models import *
from datetime import datetime, timedelta
import csv

@celery.task
def send_deadline_reminders():

    upcoming = datetime.utcnow() + timedelta(days=2)

    drives = PlacementDrive.query.filter(
        PlacementDrive.application_deadline <= upcoming,
        PlacementDrive.status == "APPROVED"
    ).all()

    for drive in drives:
        print(f"Reminder: Drive closing soon → {drive.job_title}")




@celery.task
def generate_monthly_report():

    total_drives = PlacementDrive.query.count()

    total_applications = Application.query.count()

    selected = Application.query.filter_by(
        status="SELECTED"
    ).count()

    report = f"""
    Monthly Placement Report

    Total Drives: {total_drives}
    Applications: {total_applications}
    Students Selected: {selected}
    """

    print(report)


@celery.task
def export_student_applications(student_id):

    applications = Application.query.filter_by(
        student_id=student_id
    ).all()

    filename = f"applications_{student_id}.csv"

    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Drive",
            "Status",
            "Application Date"
        ])

        for app in applications:
            writer.writerow([
                app.drive.job_title,
                app.status,
                app.application_date
            ])

    return filename