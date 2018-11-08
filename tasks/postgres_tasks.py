from __future__ import absolute_import, unicode_literals

from settings import app
from trebel.postgres.backup import *


@app.task
def postgres_backup(arg=None):
    return trable_postgres_backup(arg)