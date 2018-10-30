

import os
import sys
import subprocess
from datetime import *

DB_USER = 'mnm'
DB_NAME = 'reports'
PASS = 'fg4d_a9n0dw'
HOST = '52.173.81.58'
PORT = '5432'

TEMP_BACKUP_PATH = r'/mnt/storage/backups/reports/'
BACKUP_PATH = r''

def main():

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

if __name__ == '__main__':
    main()

