from fastapi import Depends, HTTPException
from database.connection import DatabaseConnection
import fdb

class GetAll(DatabaseConnection): 
    def get_property(self):
        try:
            cursor = self.get_cursor()
            cursor.execute('SELECT * FROM "Property" ORDER BY STATE,CITY,ADDRESS')
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            if not rows:
                raise HTTPException(status_code=404, detail="No properties found")
            result =[dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_user(self):
        try:
            sql_query = """
                SELECT * FROM "User"
                
                """
            cursor = self.get_cursor()
            cursor.execute(sql_query)
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            if not rows:
                raise HTTPException(status_code=404, detail="No users found")
            result =[dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_repairs(self):
        try:
            cursor = self.get_cursor()
            cursor.execute('SELECT * FROM "Repairs"')
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            if not rows:
                raise HTTPException(status_code=404, detail="No repairs found")
            result =[dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_meeting(self):
        try:
            cursor = self.get_cursor()
            cursor.execute('SELECT * FROM "Meeting"')
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            if not rows:
                raise HTTPException(status_code=404, detail="No meetings found")
            result =[dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_sales(self):
        try:
            cursor = self.get_cursor()
            cursor.execute('SELECT * FROM "Sales"')
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            if not rows:
                raise HTTPException(status_code=404, detail="No sells found")
            result =[dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_rent(self):
        try:
            cursor = self.get_cursor()
            cursor.execute('SELECT * FROM "Rents"')
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            if not rows:
                raise HTTPException(status_code=404, detail="No rents found")
            result =[dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_payment(self):
        try:
            cursor = self.get_cursor()
            cursor.execute('SELECT * FROM "Payment"')
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            if not rows:
                raise HTTPException(status_code=404, detail="No payments found")
            result =[dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_agreements(self):
        try:
            cursor = self.get_cursor()
            cursor.execute('SELECT * FROM "Agreement"')
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            if not rows:
                raise HTTPException(status_code=404, detail="No agreements found")
            result =[dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_reviews(self):
        try:
            cursor = self.get_cursor()
            cursor.execute('SELECT * FROM "Review"')
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            if not rows:
                raise HTTPException(status_code=404, detail="No reviews found")
            result =[dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_tel_number(self):
        try:
            cursor = self.get_cursor()
            cursor.execute('SELECT * FROM "Tel_number"')
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            if not rows:
                raise HTTPException(status_code=404, detail="No tel_numbers found")
            result =[dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_agent(self):
        try:
            sql_query = """
                SELECT * 
                FROM \"Agent\" A LEFT JOIN \"User\"  U 
                ON A.USER_ID=U.USER_ID; 
        
                """
            cursor = self.get_cursor()
            cursor.execute(sql_query)
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            if not rows:
                raise HTTPException(status_code=404, detail="No users found")
            result =[dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_client(self):
        try:
            sql_query = """
                SELECT *
                FROM \"Client\" C LEFT JOIN \"User\"  U
                ON C.USER_ID=U.USER_ID; 
                
                """
            cursor = self.get_cursor()
            cursor.execute(sql_query)
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            if not rows:
                raise HTTPException(status_code=404, detail="No users found")
            result =[dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_manager(self):
        try:
            sql_query = """
                SELECT *
                FROM \"Manager\" M LEFT JOIN \"User\"  U
                ON M.USER_ID=U.USER_ID; 
                
                """
            cursor = self.get_cursor()
            cursor.execute(sql_query)
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            if not rows:
                raise HTTPException(status_code=404, detail="No users found")
            result =[dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_manager_agent(self):
        try:
            cursor = self.get_cursor()
            cursor.execute('SELECT * FROM "ManagerAgent"')
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            if not rows:
                raise HTTPException(status_code=404, detail="No manager_agents found")
            result =[dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))