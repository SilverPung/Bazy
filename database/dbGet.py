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

    def get_client(self):
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
    
    def get_manager(self):
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
    


class GetOne(DatabaseConnection):
    
    def __init__(self):
        super().__init__()
       

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
    
    def get_client(self, client_id: int):
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
    
    def get_manager(self, manager_id: int):
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





class GetAdvanced(DatabaseConnection):
    def __init__(self):
        super().__init__()

    def get_lone_user(self):
        cursor = self.get_cursor()
        cursor.execute("""
                SELECT U.USER_ID, U.NAME, U.SURNAME, U.EMAIL, U.PASSWORD, U.ADDRESS
                    FROM "User" U
                    LEFT JOIN "Agent" A ON U.USER_ID = A.USER_ID
                    LEFT JOIN "Client" C ON U.USER_ID = C.USER_ID
                    LEFT JOIN "Manager" M ON U.USER_ID = M.USER_ID
                    WHERE A.USER_ID IS NULL
                    AND C.USER_ID IS NULL
                    AND M.USER_ID IS NULL
        """)
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        if not rows:
            raise HTTPException(status_code=404, detail="No lone users found")
        result = [dict(zip(colums, row)) for row in rows]
        return result
    
    def get_user_with_role(self):
        cursor = self.get_cursor()
        cursor.execute("""
                SELECT 
                    U.USER_ID,
                    U.NAME,
                    U.SURNAME,
                    U.EMAIL,
                    U.PASSWORD,
                    U.ADDRESS,
                    CASE 
                        WHEN A.USER_ID IS NOT NULL THEN 'Agent'
                        WHEN C.USER_ID IS NOT NULL THEN 'Client'
                        WHEN M.USER_ID IS NOT NULL THEN 'Manager'
                        ELSE 'None'
                    END AS ROLE
                FROM "User" U
                LEFT JOIN "Agent" A ON U.USER_ID = A.USER_ID
                LEFT JOIN "Client" C ON U.USER_ID = C.USER_ID
                LEFT JOIN "Manager" M ON U.USER_ID = M.USER_ID;
        """)
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="No users found")
        result = [dict(zip(colums, row)) for row in rows]
        return result

    def get_property_with_repair_number(self):
        cursor = self.get_cursor()
        cursor.execute("""
                SELECT 
                    P.PROPERTY_ID,P.ADDRESS, P.CITY,P.STATE,P.POSTAL_CODE,P.SIZE,
                    P.BEDROOMS,P.BATHROOMS,P.PRICE,P.STATUS,P.TYPE, P.DESCRIPTION,COUNT(R.REPAIR_ID) AS REPAIR_NUMBER
                FROM "Property" P
                LEFT JOIN "Repairs" R ON P.PROPERTY_ID = R.PROPERTY_ID
                GROUP BY 
                    P.PROPERTY_ID, P.ADDRESS, P.CITY,  P.STATE, P.POSTAL_CODE, P.SIZE, P.BEDROOMS, P.BATHROOMS, P.PRICE, P.STATUS, P.TYPE, P.DESCRIPTION
                HAVING COUNT(R.REPAIR_ID) > 0
                ORDER BY REPAIR_NUMBER DESC;
        """)
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="No properties found")
        result = [dict(zip(colums, row)) for row in rows]
        return result
    
    def get_renting_user(self):
        cursor = self.get_cursor()
        cursor.execute("""
            SELECT 
                U.USER_ID, U.NAME, U.SURNAME
            FROM "User" U
            WHERE EXISTS (
                SELECT 1
                FROM "Rents" R
                WHERE U.USER_ID = R.CLIENT_ID
            );
        
            """)
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="No properties found")
        result = [dict(zip(colums, row)) for row in rows]
        return result
    
    def get_property_cheaper_than_average(self):
        cursor = self.get_cursor()
        cursor.execute("""
            SELECT 
                P.PROPERTY_ID, P.ADDRESS, P.CITY, P.SIZE, P.BEDROOMS, P.BATHROOMS, P.PRICE, P.STATUS, P.TYPE
            FROM "Property" P
            WHERE P.PRICE < (
                SELECT AVG(PRICE)
                FROM "Property"
            );
        
            """)
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="No properties found")
        result = [dict(zip(colums, row)) for row in rows]
        return result
    
    def get_property_by_type(self, type):
        cursor = self.get_cursor()
        cursor.execute("""
            SELECT * FROM "Property" WHERE TYPE = ?
            ORDER BY PRICE ASC;
        """, (type,))
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="No properties found")
        result = [dict(zip(colums, row)) for row in rows]
        return result
    
    def get_property_by_city(self, city):
        cursor = self.get_cursor()
        cursor.execute("""
            SELECT * FROM "Property" WHERE CITY = ?
            ORDER BY PRICE ASC;
        """, (city,))
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="No properties found")
        result = [dict(zip(colums, row)) for row in rows]
        return result
    
    

if __name__ == "__main__":
    get = GetAdvanced()
    users = get.get_lone_user()
    for user in users:
        print(user)


