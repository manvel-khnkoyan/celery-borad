from __future__ import absolute_import, unicode_literals

from settings import app
from trebel.postgres.backup import trable_postgres_backup


@app.task
def postgres_backup():
    return trable_postgres_backup()


