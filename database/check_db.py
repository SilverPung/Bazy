import fdb

# Connect to the database
con = fdb.connect(
    dsn='localhost:C:/Program Files/Firebird/agency.fdb',
    user='SYSDBA',
    password='postgres'
)
cursor = con.cursor()

# Query to list all tables
cursor.execute("""
SELECT RDB$RELATION_NAME
FROM RDB$RELATIONS
WHERE RDB$SYSTEM_FLAG = 0
ORDER BY RDB$RELATION_NAME
""")

# Fetch and print the table names
tables = cursor.fetchall()
print("Tables in the database:")
for table in tables:
    print(table[0].strip())  # Strip whitespace

# Close the connection
con.close()