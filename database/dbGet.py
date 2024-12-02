from fastapi import Depends, HTTPException
from database.connection import DatabaseConnection
import fdb
class GetAll(DatabaseConnection): 
    def get_property(self):
        cursor = self.get_cursor()
        cursor.execute('SELECT * FROM "Property"')
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        if not rows:
            raise HTTPException(status_code=404, detail="No properties found")
        result =[dict(zip(colums, row)) for row in rows]
        return result

    def get_user(self):
        sql_query = """
            SELECT u.USER_ID, u.NAME, u.SURNAME, u.EMAIL, t.TEL_NUMBER
            FROM "User" u
            JOIN "Tel_number" t ON u.USER_ID = t.USER_ID
            ORDER BY u.USER_ID
            
            """
        cursor = self.get_cursor()
        cursor.execute(sql_query)
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        if not rows:
            raise HTTPException(status_code=404, detail="No users found")
        result =[dict(zip(colums, row)) for row in rows]
        return result
    
    def get_repairs(self):
        cursor = self.get_cursor()
        cursor.execute('SELECT * FROM "Repairs"')
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        if not rows:
            raise HTTPException(status_code=404, detail="No repairs found")
        result =[dict(zip(colums, row)) for row in rows]
        return result
    
    def get_meeting(self):
        cursor = self.get_cursor()
        cursor.execute('SELECT * FROM "Meeting"')
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        if not rows:
            raise HTTPException(status_code=404, detail="No meetings found")
        result =[dict(zip(colums, row)) for row in rows]
        return result
    
    def get_sales(self):
        cursor = self.get_cursor()
        cursor.execute('SELECT * FROM "Sales"')
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        if not rows:
            raise HTTPException(status_code=404, detail="No sells found")
        result =[dict(zip(colums, row)) for row in rows]
        return result
    
    def get_rent(self):
        cursor = self.get_cursor()
        cursor.execute('SELECT * FROM "Rents"')
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        if not rows:
            raise HTTPException(status_code=404, detail="No rents found")
        result =[dict(zip(colums, row)) for row in rows]
        return result
    
    def get_payment(self):
        cursor = self.get_cursor()
        cursor.execute('SELECT * FROM "Payment"')
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        if not rows:
            raise HTTPException(status_code=404, detail="No payments found")
        result =[dict(zip(colums, row)) for row in rows]
        return result
    
    def get_agreements(self):
        cursor = self.get_cursor()
        cursor.execute('SELECT * FROM "Agreement"')
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        if not rows:
            raise HTTPException(status_code=404, detail="No agreements found")
        result =[dict(zip(colums, row)) for row in rows]
        return result
    
    def get_reviews(self):
        cursor = self.get_cursor()
        cursor.execute('SELECT * FROM "Review"')
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        if not rows:
            raise HTTPException(status_code=404, detail="No reviews found")
        result =[dict(zip(colums, row)) for row in rows]
        return result

    def get_tel_number(self):
        cursor = self.get_cursor()
        cursor.execute('SELECT * FROM "Tel_number"')
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        if not rows:
            raise HTTPException(status_code=404, detail="No tel_numbers found")
        result =[dict(zip(colums, row)) for row in rows]
        return result
    
    def get_agent(self):
        sql_query = """
            SELECT u.USER_ID, u.NAME, u.SURNAME, u.EMAIL, a.LICENSE_NUMBER, a.COMMISION_RATE, a.EMPLOYEMENT_DATE
            FROM "User" u
            JOIN "Agent" a ON u.USER_ID = a.USER_ID
            ORDER BY u.USER_ID
            
            """
        cursor = self.get_cursor()
        cursor.execute(sql_query)
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        if not rows:
            raise HTTPException(status_code=404, detail="No users found")
        result =[dict(zip(colums, row)) for row in rows]
        return result

    def get_client(self):
        sql_query = """
            SELECT u.USER_ID, u.NAME, u.SURNAME, u.EMAIL, c.BUDGET, c.PREFFERED_LOCATION
            FROM "User" u
            JOIN "Client" c ON u.USER_ID = c.USER_ID
            ORDER BY u.USER_ID
            
            """
        cursor = self.get_cursor()
        cursor.execute(sql_query)
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        if not rows:
            raise HTTPException(status_code=404, detail="No users found")
        result =[dict(zip(colums, row)) for row in rows]
        return result
    
    def get_manager(self):
        sql_query = """
            SELECT u.USER_ID, u.NAME, u.SURNAME, u.EMAIL, m.SUPERVISION_AREA, m.EMPLOYMENT_DATE
            FROM "User" u
            JOIN "Manager" m ON u.USER_ID = m.USER_ID
            ORDER BY u.USER_ID
            
            """
        cursor = self.get_cursor()
        cursor.execute(sql_query)
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        if not rows:
            raise HTTPException(status_code=404, detail="No users found")
        result =[dict(zip(colums, row)) for row in rows]
        return result

class GetOne:
    
    def __init__(self):
        """Connect to the database using the Firebird driver for Python (fdb) and and output the data from the tables in the database based on the id.
        """
        self.db = fdb.connect("localhost:C:/Program Files/Firebird/agency.fdb", user='SYSDBA',password='postgres')

    def get_property(self, property_id: int):
        cursor = self.get_cursor()
        cursor.execute('SELECT * FROM "Property" WHERE PROPERTY_ID = ?', (property_id,))
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="Property not found")
        result = [dict(zip(colums, row)) for row in rows]
        return result
    
    def get_user(self, user_id: int):
        sql_query = """
            SELECT u.USER_ID, u.NAME, u.SURNAME, u.EMAIL, t.TEL_NUMBER
            FROM "User" u
            JOIN "Tel_number" t ON u.USER_ID = t.USER_ID
            WHERE u.USER_ID = ?
            ORDER BY u.USER_ID
            
            """
        cursor = self.get_cursor()
        cursor.execute(sql_query, (user_id,))
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="User not found")
        result = [dict(zip(colums, row)) for row in rows]
        return result
    
    def get_repair(self, repair_id: int):
        cursor = self.get_cursor()
        cursor.execute('SELECT * FROM "Repairs" WHERE REPAIR_ID = ?', (repair_id,))
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="Repair not found")
        result = [dict(zip(colums, row)) for row in rows]
        return result
   
    def get_meeting(self, meeting_id: int):
        cursor = self.get_cursor()
        cursor.execute('SELECT * FROM "Meeting" WHERE MEETING_ID = ?', (meeting_id,))
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="Meeting not found")
        result = [dict(zip(colums, row)) for row in rows]
        return result
    
    def get_sell(self, sell_id: int):
        cursor = self.get_cursor()
        cursor.execute('SELECT * FROM "Sales" WHERE SELL_ID = ?', (sell_id,))
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="Sell not found")
        result = [dict(zip(colums, row)) for row in rows]
        return result
    
    def get_rent(self, rent_id: int):
        cursor = self.get_cursor()
        cursor.execute('SELECT * FROM "Rents" WHERE RENT_ID = ?', (rent_id,))
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="Rent not found")
        result = [dict(zip(colums, row)) for row in rows]
        return result
    
    def get_payment(self, payment_id: int):
        cursor = self.get_cursor()
        cursor.execute('SELECT * FROM "Payment" WHERE PAYMENT_ID = ?', (payment_id,))
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="Payment not found")
        result = [dict(zip(colums, row)) for row in rows]
        return result
    
    def get_agreement(self, agreement_id: int):
        cursor = self.get_cursor()
        cursor.execute('SELECT * FROM "Agreement" WHERE AGREEMENT_ID = ?', (agreement_id,))
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="Agreement not found")
        result = [dict(zip(colums, row)) for row in rows]
        return result
    
    def get_review(self, review_id: int):
        cursor = self.get_cursor()
        cursor.execute('SELECT * FROM "Review" WHERE REVIEW_ID = ?', (review_id,))
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="Review not found")
        result = [dict(zip(colums, row)) for row in rows]
        return result
    
    def get_tel_number(self, tel_number_id: int):
        cursor = self.get_cursor()
        cursor.execute('SELECT * FROM "Tel_number" WHERE USER_ID=?', (tel_number_id,))
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="Tel_number not found")
        result = [dict(zip(colums, row)) for row in rows]
        return result
    
    def get_agent(self, agent_id: int):
        sql_query = """
            SELECT u.USER_ID, u.NAME, u.SURNAME, u.EMAIL, a.LICENSE_NUMBER, a.COMMISION_RATE, a.EMPLOYEMENT_DATE
            FROM "User" u
            JOIN "Agent" a ON u.USER_ID = a.USER_ID
            WHERE u.USER_ID = ?
            ORDER BY u.USER_ID
            
            """
        cursor = self.get_cursor()
        cursor.execute(sql_query, (agent_id,))
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="Agent not found")
        result = [dict(zip(colums, row)) for row in rows]
        return result
    
    def get_client(self, client_id: int):
        sql_query = """
            SELECT u.USER_ID, u.NAME, u.SURNAME, u.EMAIL, c.BUDGET, c.PREFFERED_LOCATION
            FROM "User" u
            JOIN "Client" c ON u.USER_ID = c.USER_ID
            WHERE u.USER_ID = ?
            ORDER BY u.USER_ID
            
            """
        cursor = self.get_cursor()
        cursor.execute(sql_query, (client_id,))
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="Client not found")
        result = [dict(zip(colums, row)) for row in rows]
        return result
    
    def get_manager(self, manager_id: int):
        sql_query = """
            SELECT u.USER_ID, u.NAME, u.SURNAME, u.EMAIL, m.SUPERVISION_AREA, m.EMPLOYMENT_DATE
            FROM "User" u
            JOIN "Manager" m ON u.USER_ID = m.USER_ID
            WHERE u.USER_ID = ?
            ORDER BY u.USER_ID
            
            """
        cursor = self.get_cursor()
        cursor.execute(sql_query, (manager_id,))
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="Manager not found")
        result = [dict(zip(colums, row)) for row in rows]
        return result

if __name__ == "__main__":
    get = GetAll()
    print(get.get_property())