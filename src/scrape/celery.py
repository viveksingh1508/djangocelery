import os
from celery import Celery
from celery.schedules import crontab
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scrape.settings")

app = Celery("scrape")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# Namespace 'CELERY' means all celery-related configs must be prefixed with 'CELERY_'.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "multiple-task-crontab":{
        "task":"multiple_two_numbers",
        "schedule":crontab(hour=7,minute=30,day_of_week=1),
        "args":(16, 16)
    },
    "multiply_every-5-seconds":{
        "task":"multiply_two_numbers",
        "schedule":5.0,
        "args":(16, 16)
    },
    "add-every-30-seconds":{
        "task":"movies.tasks.add",
        "schedule":30.0,
        "args":(16, 16)
    }
}