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
    
     CREATE OR ALTER TRIGGER SOLD_PROPERTY_TRIGGER
        BEFORE INSERT OR UPDATE ON "Sales"
        AS
        BEGIN
            IF (EXISTS (
                SELECT 1
                FROM "Sales"
                WHERE PROPERTY_ID = NEW.PROPERTY_ID
                AND STATUS IN ('Pending', 'Completed')
                AND SALE_ID != NEW.SALE_ID
            )) THEN
                EXCEPTION PROPERTY_SOLD_OR_RENTED;

 
            IF (EXISTS (
                SELECT 1
                FROM "Rents"
                WHERE PROPERTY_ID = NEW.PROPERTY_ID
                AND STATUS IN ('Pending', 'Active')
            )) THEN
                EXCEPTION PROPERTY_SOLD_OR_RENTED;
        END;           
    """)
    print("Procedure created or updated.")
except fdb.DatabaseError as e:
    print(f"Error creating/updating Procedure: {e}")

# ...existing code...

# Commit and close the connection
con.commit()
con.close()