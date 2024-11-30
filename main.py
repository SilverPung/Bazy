import fdb
from datetime import date

# Connect to the database
con = fdb.connect(
    dsn='localhost:C:/Program Files/Firebird/agency.fdb',
    user='SYSDBA',
    password='postgres'
)
cur = con.cursor()

max_id=20

# Step 2: Create a generator if it doesn't exist
"""
try:
    cur.execute("CREATE GENERATOR GEN_REPAIRS_ID;")
    print("Generator created.")
except fdb.DatabaseError as e:
    print(f"Generator already exists or error: {e}")

# Step 3: Set the generator to start from max_id + 1
try:
    cur.execute(f"SET GENERATOR GEN_REPAIRS_ID TO {max_id};")
    print(f"Generator set to start from {max_id + 1}.")
except fdb.DatabaseError as e:
    print(f"Error setting generator value: {e}")
"""

# Step 4: Create the trigger if it doesn't exist
try:
    cur.execute("""
    CREATE OR ALTER TRIGGER BI_REPAIR_ID FOR \"Repairs\"
    ACTIVE BEFORE INSERT POSITION 0
    AS
    DECLARE VARIABLE GENERATED_ID INTEGER;
    BEGIN
        IF (NEW.REPAIR_ID IS NULL) THEN
        BEGIN
            -- Generate the first ID
            GENERATED_ID = GEN_ID(GEN_REPAIRS_ID, 1);

            -- Check for conflicts and increment until unique
            WHILE (EXISTS (SELECT 1 FROM \"Repairs\" WHERE REPAIR_ID = :GENERATED_ID)) DO
            BEGIN
                -- Increment the generator again
                GENERATED_ID = GEN_ID(GEN_REPAIRS_ID, 1);
            END

            -- Assign the unique ID to the new row
            NEW.REPAIR_ID = GENERATED_ID;
        END
    END;
                
    """)
    print("Trigger created or updated.")
except fdb.DatabaseError as e:
    print(f"Error creating/updating trigger: {e}")


    """

    """





# ...existing code...

# Commit and close the connection
con.commit()
con.close()