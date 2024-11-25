import fdb

# Connect to the database
con = fdb.connect(
    dsn='localhost:C:/Program Files/Firebird/agency.fdb',
    user='SYSDBA',
    password='postgres'
)


cursor = con.cursor()

# Use VARCHAR for ENUM-like behavior or consider lookup tables
cursor.execute("DROP TABLE \"PROPERTY\"")

# Commit and close the connection
con.commit()
con.close()