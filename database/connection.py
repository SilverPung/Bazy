import fdb


class DatabaseConnection:
    def __init__(self):
        """Connect to the database using the Firebird driver for Python (fdb)."""
        self.db = fdb.connect("localhost:C:/Program Files/Firebird/agency.fdb", user='SYSDBA', password='postgres')

    def get_cursor(self):
        return self.db.cursor()
    
    def commit(self):
        self.db.commit()