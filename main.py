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
        CREATE OR ALTER PROCEDURE UPDATE_MANAGER( 

            USER_ID INT, 

            NAME VARCHAR(50), 

            SURNAME VARCHAR(50), 

            EMAIL VARCHAR(50), 

            PASSWORD VARCHAR(50), 

            ADDRESS VARCHAR(50), 

            SUPERVISION_AREA VARCHAR(50), 

            EMPLOYMENT_DATE DATE 

        ) 

        AS 

        BEGIN 

            IF (NOT EXISTS(SELECT * FROM "Manager" WHERE USER_ID = :USER_ID)) THEN 

                EXCEPTION USER_IS_NOT_MANAGER; 

  

            UPDATE "User" 

            SET NAME = :NAME, SURNAME = :SURNAME, EMAIL = :EMAIL, PASSWORD = :PASSWORD, ADDRESS = :ADDRESS 

            WHERE USER_ID = :USER_ID; 

             

            UPDATE "Manager" 

            SET SUPERVISION_AREA = :SUPERVISION_AREA, EMPLOYMENT_DATE = :EMPLOYMENT_DATE 

            WHERE USER_ID = :USER_ID; 

        END; 
            
    """)

    con.commit()

except fdb.DatabaseError as e:
    print(f"Error creating/updating Procedure: {e}")

# ...existing code...


# Commit and close the connection