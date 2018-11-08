from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery.schedules import crontab, crontab_parser
from dotenv import load_dotenv
load_dotenv()
from os import getenv
import sys

sys.path.append('../')
app = Celery('tasks',
             broker=getenv("broker_connection"),
             backend=getenv("backend_connection"),
             include=['math_tasks','postgres_tasks'])


app.conf.update(
    result_expires=3600,
)

app.conf.beat_schedule = {
    'postgres-backup-every-day': {
        'task': 'postgres_tasks.postgres_backup',
        'schedule': crontab(hour=7, minute=30, day_of_week = '*')
    }
}
app.conf.timezone = 'UTC'

if __name__ == '__main__':
    app.start()
