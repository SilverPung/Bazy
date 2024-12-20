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
        ALTER TABLE "Property" ADD CONSTRAINT "Property_Type" CHECK (TYPE IN ('House', 'Apartment','Flat', 'Condo', 'Townhouse', 'Duplex', 'Triplex', 'Fourplex', 'Villa', 'Cottage', 'Bungalow', 'Mobile Home', 'Other')) 
    """)
    print("Procedure created or updated.")
except fdb.DatabaseError as e:
    print(f"Error creating/updating Procedure: {e}")

# ...existing code...

# Commit and close the connection
con.commit()
con.close()