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
        EXECUTE PROCEDURE CREATE_CLIENT(
            'Jan', -- Use single quotes
            'Kowalski',
            'jan.kowalski@onet.pl',
            'jan123456',
            'ul. Gdańska 20, 80-006 Gdańsk',
            600000,
            'Gdańsk'
        );
    
    """)
    print("Procedure created or updated.")
except fdb.DatabaseError as e:
    print(f"Error creating/updating Procedure: {e}")

# ...existing code...

# Commit and close the connection
con.commit()
con.close()