import fdb
from datetime import date

# Connect to the database
con = fdb.connect(
    dsn='localhost:C:/Program Files/Firebird/agency.fdb',
    user='SYSDBA',
    password='postgres'
)
cur = con.cursor()

try:
    cur.execute("""
        SELECT RDB$TRIGGER_NAME
        FROM RDB$TRIGGERS

    """)
    for row in cur.fetchall():
        print(row)
        
except fdb.DatabaseError as e:
    print(f"Error creating/updating Procedure: {e}")

