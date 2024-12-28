from fastapi import Depends, HTTPException
from database.connection import DatabaseConnection
import fdb


class GetOne(DatabaseConnection):
    
    def __init__(self):
        super().__init__()
       

    def get_property(self, property_id: int):
        try:
            cursor = self.get_cursor()
            cursor.execute('SELECT * FROM "Property" WHERE PROPERTY_ID = ?', (property_id,))
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            if not rows:
                raise HTTPException(status_code=404, detail="Property not found")
            result = [dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_user(self, user_id: int):
        try:
            sql_query = """
                SELECT * FROM "User" WHERE USER_ID = ?;
                
                """
            cursor = self.get_cursor()
            cursor.execute(sql_query, (user_id,))
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            if not rows:
                raise HTTPException(status_code=404, detail="User not found")
            result = [dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_repair(self, repair_id: int):
        try:
            cursor = self.get_cursor()
            cursor.execute('SELECT * FROM "Repairs" WHERE REPAIR_ID = ?', (repair_id,))
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            if not rows:
                raise HTTPException(status_code=404, detail="Repair not found")
            result = [dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
   
    def get_meeting(self, meeting_id: int):
        try:
            cursor = self.get_cursor()
            cursor.execute('SELECT * FROM "Meeting" WHERE MEETING_ID = ?', (meeting_id,))
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            if not rows:
                raise HTTPException(status_code=404, detail="Meeting not found")
            result = [dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_sell(self, sell_id: int):
        try:
            cursor = self.get_cursor()
            cursor.execute('SELECT * FROM "Sales" WHERE SALE_ID = ?', (sell_id,))
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            if not rows:
                raise HTTPException(status_code=404, detail="Sell not found")
            result = [dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_rent(self, rent_id: int):
        try:
            cursor = self.get_cursor()
            cursor.execute('SELECT * FROM "Rents" WHERE RENT_ID = ?', (rent_id,))
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            if not rows:
                raise HTTPException(status_code=404, detail="Rent not found")
            result = [dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_payment(self, payment_id: int):
        try:
            cursor = self.get_cursor()
            cursor.execute('SELECT * FROM "Payment" WHERE PAYMENT_ID = ?', (payment_id,))
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            if not rows:
                raise HTTPException(status_code=404, detail="Payment not found")
            result = [dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_agreement(self, agreement_id: int):
        try:
            cursor = self.get_cursor()
            cursor.execute('SELECT * FROM "Agreement" WHERE AGREEMENT_ID = ?', (agreement_id,))
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            if not rows:
                raise HTTPException(status_code=404, detail="Agreement not found")
            result = [dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_review(self, review_id: int):
        try:
            cursor = self.get_cursor()
            cursor.execute('SELECT * FROM "Review" WHERE REVIEW_ID = ?', (review_id,))
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            if not rows:
                raise HTTPException(status_code=404, detail="Review not found")
            result = [dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_tel_number(self, tel_number_id: int):
        try:
            cursor = self.get_cursor()
            cursor.execute('SELECT * FROM "Tel_number" WHERE USER_ID=?', (tel_number_id,))
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            if not rows:
                raise HTTPException(status_code=404, detail="Tel_number not found")
            result = [dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_agent(self, agent_id: int):
        try:
            sql_query = """
                SELECT *
                FROM \"Agent\" A LEFT JOIN \"User\"  U
                ON A.USER_ID=U.USER_ID
                WHERE A.USER_ID = ?;
                
                """
            cursor = self.get_cursor()
            cursor.execute(sql_query, (agent_id,))
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            if not rows:
                raise HTTPException(status_code=404, detail="Agent not found")
            result = [dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_client(self, client_id: int):
        try:
            sql_query = """
                SELECT *
                FROM \"Client\" C LEFT JOIN \"User\"  U
                ON C.USER_ID=U.USER_ID
                WHERE C.USER_ID = ?;
                
                """
            cursor = self.get_cursor()
            cursor.execute(sql_query, (client_id,))
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            if not rows:
                raise HTTPException(status_code=404, detail="Client not found")
            result = [dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_manager(self, manager_id: int):
        try:
            sql_query = """
                SELECT *
                FROM \"Manager\" M LEFT JOIN \"User\"  U
                ON M.USER_ID=U.USER_ID
                WHERE M.USER_ID = ?;
                
                """
            cursor = self.get_cursor()
            cursor.execute(sql_query, (manager_id,))
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            if not rows:
                raise HTTPException(status_code=404, detail="Manager not found")
            result = [dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))