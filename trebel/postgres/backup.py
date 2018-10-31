import os
import sys
import subprocess
from datetime import *
from dotenv import load_dotenv
load_dotenv()
from os import getenv

DB_USER = getenv("PG_DB_USER")
DB_NAME = getenv("PG_DB_NAME")
PASS = getenv("PG_PASS")
HOST = getenv("PG_HOST")
PORT = getenv("PG_PORT")

TEMP_BACKUP_PATH = getenv("PG_TEMP_BACKUP_PATH")
BACKUP_PATH = getenv("PG_BACKUP_PATH")

def trable_postgres_backup():

    try:
        db_table_name = sys.argv[1]
    except:
        yesterday = datetime.now() - timedelta(days=1)
        day = '%02d' % yesterday.day
        month = '%02d' % yesterday.month
        year = yesterday.year
        db_table_name = 'daily_%s%s%s' % (year,month,day)

    destination = r'%s%s' % (TEMP_BACKUP_PATH, db_table_name + '.sql')
    print("Backing up %s - %s database to %s" %(DB_NAME, db_table_name, destination))
    
    os.putenv('PGPASSWORD', PASS)
    ps = subprocess.Popen(
            ['pg_dump', '-U', DB_USER, '-h', HOST, '-p', PORT, '-Fc', DB_NAME, '-t', db_table_name, '-f', destination],
            stdout=subprocess.PIPE
    )
    output = ps.communicate()[0]

    for line in output.splitlines():
        print(line)

