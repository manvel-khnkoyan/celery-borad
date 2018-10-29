from __future__ import absolute_import, unicode_literals
from celery import Celery
from dotenv import load_dotenv
load_dotenv()
from os import getenv

app = Celery('job-management-system',
             broker=getenv("broker_connection"),
             backend=getenv("backend_connection"),
             include=['tasks'])


app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()