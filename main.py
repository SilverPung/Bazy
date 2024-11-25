import fdb
from datetime import date

# Connect to the database
con = fdb.connect(
    dsn='localhost:C:/Program Files/Firebird/agency.fdb',
    user='SYSDBA',
    password='postgres'
)
cursor = con.cursor()

"""


"""

# ...existing code...
data=[

]

for row in data:
    cursor.execute(
    """

    """

    
    )

# ...existing code...

# Commit and close the connection
con.commit()
con.close()