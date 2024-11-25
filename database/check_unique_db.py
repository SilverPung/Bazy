import fdb


def show_client_table():
    # Connect to the Firebird database
    try:
        con = fdb.connect(
            dsn='localhost:C:/Program Files/Firebird/agency.fdb',  # Update with your actual path
            user='SYSDBA',  # Your username
            password='postgres'  # Your password
        )
        
        # Create a cursor to execute queries
        cursor = con.cursor()

        # Query to select all columns from the "Client" table
        cursor.execute('SELECT * FROM "Repairs"')

        # Fetch the column names
        column_names = [desc[0] for desc in cursor.description]

        # Print column names
        print("Column Names:", column_names)

        # Fetch all rows
        rows = cursor.fetchall()

        # Check if the table is empty
        if not rows:
            print("The table is empty.")
        else:
            # Print the rows
            for row in rows:
                print(row)

    except fdb.DatabaseError as e:
        print(f"Database error: {e}")
    finally:
        # Close the connection
        if con:
            con.close()
def options():
    con = fdb.connect(
    dsn='localhost:C:/Program Files/Firebird/agency.fdb',
    user='SYSDBA',
    password='postgres'
    )
    cursor = con.cursor()

    # Define the table and column to check
    table_name = '\"Property\"'
    column_name = 'Status'

    # Query to find CHECK constraints on the specified table
    cursor.execute(f"""
    SELECT
        CC.RDB$CONSTRAINT_NAME AS constraint_name,
        CC.RDB$TRIGGER_SOURCE AS trigger_source
    FROM
        RDB$CHECK_CONSTRAINTS CC
    JOIN
        RDB$RELATION_CONSTRAINTS RC ON CC.RDB$CONSTRAINT_NAME = RC.RDB$CONSTRAINT_NAME
    WHERE
        RC.RDB$RELATION_NAME = ?
        AND RC.RDB$CONSTRAINT_TYPE = 'CHECK'
    """, (table_name,))

    # Fetch all results
    constraints = cursor.fetchall()

    # Filter constraints for the specific column
    for constraint in constraints:
        constraint_name = constraint[0].strip()
        trigger_source = constraint[1].strip()
        if column_name in trigger_source.upper():
            print(f"Constraint Name: {constraint_name}")
            print(f"Constraint Definition: {trigger_source}")
            print("-" * 50)

    # Close the connection
    con.close()

# Call the function to display the Client table

show_client_table()