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
              
       EXECUTE PROCEDURE UpdatePropertyStatus;
            
    """)

    con.commit()

except fdb.DatabaseError as e:
    print(f"Error creating/updating Procedure: {e}")

# ...existing code...


# Commit and close the connection