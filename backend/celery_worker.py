from celery_app import celery
from celery.schedules import crontab
from app import create_app

flask_app = create_app()

def init_celery(app):

    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return super().__call__(*args, **kwargs)

    celery.Task = ContextTask


init_celery(flask_app)


celery.conf.beat_schedule = {

    "daily-reminder-job": {
        "task": "tasks.jobs.send_deadline_reminders",
        "schedule": crontab(hour=8, minute=0)
    },

    "monthly-report-job": {
        "task": "tasks.jobs.generate_monthly_report",
        "schedule": crontab(day_of_month=1, hour=9)
    }
}

import tasks.jobs