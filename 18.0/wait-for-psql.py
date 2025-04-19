#!/usr/bin/env python
import os
import time
import psycopg2

while True:
    try:
        conn = psycopg2.connect(
            dbname=os.environ.get('POSTGRES_DB', 'postgres'),
            user=os.environ.get('POSTGRES_USER', 'odoo'),
            password=os.environ.get('POSTGRES_PASSWORD', 'odoo'),
            host=os.environ.get('DB_HOST', 'db'),
            port=os.environ.get('DB_PORT', '5432'),
        )
        conn.close()
        break
    except Exception as e:
        print("Waiting for PostgreSQL...")
        time.sleep(2)

    if error:
        print("Database connection failure: %s" % error, file=sys.stderr)
        sys.exit(1)
