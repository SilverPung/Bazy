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
    
    def get_manager_agent(self):
        cursor = self.get_cursor()
        cursor.execute('SELECT * FROM "ManagerAgent"')
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        if not rows:
            raise HTTPException(status_code=404, detail="No manager_agents found")
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
                    P.BEDROOMS,P.BATHROOMS,P.PRICE,P.TYPE, P.DESCRIPTION,COUNT(R.REPAIR_ID) AS REPAIR_NUMBER
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
                P.PROPERTY_ID, P.ADDRESS, P.CITY, P.SIZE, P.BEDROOMS, P.BATHROOMS, P.PRICE, P.TYPE
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
        city= city.capitalize()
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
    
    def get_user_from_city(self, city):
        cursor = self.get_cursor()
        cursor.execute("""
            SELECT U.USER_ID, U.NAME, U.SURNAME, U.EMAIL, U.PASSWORD, U.ADDRESS
            FROM "User" U
            WHERE U.ADDRESS LIKE ?
        """, (f'%{city}%',))
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="No users found")
        result = [dict(zip(colums, row)) for row in rows]
        return result
    
    def get_property_in_cities(self, cities: list):
        cursor = self.get_cursor()
        cursor.execute("""
            SELECT * FROM "Property" WHERE CITY IN ({})
            ORDER BY PRICE ASC;
        """.format(', '.join(['?']*len(cities))), cities)
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="No properties found")
        result = [dict(zip(colums, row)) for row in rows]
        return result
    
    def get_property_not_in_cities(self, cities: list):
        cursor = self.get_cursor()
        cursor.execute("""
            SELECT * FROM "Property" WHERE CITY NOT IN ({})
            ORDER BY PRICE ASC;
        """.format(', '.join(['?']*len(cities))), cities)
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="No properties found")
        result = [dict(zip(colums, row)) for row in rows]
        return result

    def get_user_with_phone_numbers(self):
        cursor = self.get_cursor()
        cursor.execute("""
            SELECT 
                U.USER_ID, 
                U.NAME, 
                U.SURNAME, 
                U.EMAIL, 
                U.PASSWORD, 
                U.ADDRESS, 
                LIST(T.TEL_NUMBER, ', ') AS TEL_NUMBERS
            FROM "User" U
            LEFT JOIN "Tel_number" T ON U.USER_ID = T.USER_ID
            GROUP BY U.USER_ID, U.NAME, U.SURNAME, U.EMAIL, U.PASSWORD, U.ADDRESS
        """)
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="No users found")
        result = [dict(zip(colums, row)) for row in rows]
        return result
    
    def get_unique_cities_for_property(self):
        cursor = self.get_cursor()
        cursor.execute("""
            SELECT DISTINCT CITY FROM "Property"
        """)
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="No cities found")
        result = [dict(zip(colums, row)) for row in rows]
        return result

    def get_agent_with_supervisor(self):
        cursor = self.get_cursor()
        cursor.execute("""
            SELECT 
                A.USER_ID AS AGENT_ID,
                AU.NAME AS AGENT_NAME,
                AU.SURNAME AS AGENT_SURNAME,
                AU.EMAIL AS AGENT_EMAIL,
                A.LICENSE_NUMBER,
                A.COMMISION_RATE,
                A.EMPLOYEMENT_DATE,
                M.USER_ID AS SUPERVISOR_ID,
                MU.NAME AS SUPERVISOR_NAME,
                MU.SURNAME AS SUPERVISOR_SURNAME,
                MU.EMAIL AS SUPERVISOR_EMAIL,
                M.SUPERVISION_AREA,
                M.EMPLOYMENT_DATE AS SUPERVISOR_EMPLOYMENT_DATE
            FROM 
                "Agent" A
            JOIN 
                "User" AU ON A.USER_ID = AU.USER_ID
            RIGHT JOIN
                "ManagerAgent" MA ON A.USER_ID = MA.AGENT_ID
            LEFT JOIN
                "Manager" M ON MA.MANAGER_ID = M.USER_ID
            LEFT JOIN
                "User" MU ON M.USER_ID = MU.USER_ID;
        """)
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="No agents found")
        result = [dict(zip(colums, row)) for row in rows]
        return result

    def get_property_not_sold_or_rented(self):
        cursor = self.get_cursor()
        cursor.execute("""
            SELECT 
                P.PROPERTY_ID,
                P.ADDRESS,
                P.CITY,
                P.STATE,
                P.POSTAL_CODE,
                P.SIZE,
                P.BEDROOMS,
                P.BATHROOMS,
                P.PRICE,
                P.TYPE,
                P.DESCRIPTION
            FROM 
                "Property" P
            WHERE NOT EXISTS (
                SELECT 1
                FROM "Sales" S
                WHERE P.PROPERTY_ID = S.PROPERTY_ID
                AND S.STATUS IN ('Pending', 'Completed')
            )
            AND NOT EXISTS (
                SELECT 1
                FROM "Rents" R
                WHERE P.PROPERTY_ID = R.PROPERTY_ID
                AND R.STATUS IN ('Pending', 'Active')
            );
        """)
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="No properties found")
        result = [dict(zip(colums, row)) for row in rows]
        return result
    
    def get_rents_with_money_paid_in_payment(self):
        cursor = self.get_cursor()
        cursor.execute("""
            SELECT 
                R.RENT_ID,
                R.PROPERTY_ID,
                R.CLIENT_ID,
                R.START_DATE,
                R.END_DATE,
                R.DEPOSIT,
                R.STATUS,
                CAST(SUM(CASE WHEN P.STATUS IN ('Pending', 'Paid') THEN P.AMOUNT ELSE 0 END) AS NUMERIC(10, 2)) AS TOTAL_PAID
            FROM 
                "Rents" R
            JOIN
                "Payment" P ON R.RENT_ID = P.RENT_ID
            GROUP BY
                R.RENT_ID, R.PROPERTY_ID, R.CLIENT_ID, R.START_DATE, R.END_DATE, R.DEPOSIT, R.STATUS
            ORDER BY R.RENT_ID;
        """)
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="No rents found")
        result = [dict(zip(colums, row)) for row in rows]
        return result

    def get_property_not_s_or_r_cheaper_then(self,budget):
        cursor = self.get_cursor()
        cursor.execute("""
            SELECT 
                P.PROPERTY_ID,
                P.ADDRESS,
                P.CITY,
                P.STATE,
                P.POSTAL_CODE,
                P.SIZE,
                P.BEDROOMS,
                P.BATHROOMS,
                P.PRICE,
                P.TYPE,
                P.DESCRIPTION
            FROM 
                "Property" P
            WHERE P.PRICE > ?
            AND NOT EXISTS (
                SELECT 1
                FROM "Sales" S
                WHERE P.PROPERTY_ID = S.PROPERTY_ID
                AND S.STATUS IN ('Pending', 'Completed')
            )
            AND NOT EXISTS (
                SELECT 1
                FROM "Rents" R
                WHERE P.PROPERTY_ID = R.PROPERTY_ID
                AND R.STATUS IN ('Pending', 'Active')
            );
        """,(budget,))
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="No properties found")
        result = [dict(zip(colums, row)) for row in rows]
        return result
    
    def get_possible_property_types(self):
        cursor = self.get_cursor()
        cursor.execute("""
            SELECT DISTINCT TYPE FROM "Property"
        """)
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="No types found")
        result = [dict(zip(colums, row)) for row in rows]
        return result
    
    def get_review_with_client_and_agent(self):
        cursor = self.get_cursor()
        cursor.execute("""
            SELECT 
                R.REVIEW_ID,
                R.RATING,
                R.DESCRIPTION,
                C.USER_ID AS CLIENT_ID,
                UC.NAME AS CLIENT_NAME,
                UC.SURNAME AS CLIENT_SURNAME,
                A.USER_ID AS AGENT_ID,
                UA.NAME AS AGENT_NAME,
                UA.SURNAME AS AGENT_SURNAME
            FROM 
                "Review" R
            JOIN
                "Client" C ON R.CLIENT_ID = C.USER_ID
            JOIN
                "Agent" A ON R.AGENT_ID = A.USER_ID
            JOIN 
                "User" UC ON C.USER_ID = UC.USER_ID
            JOIN
                "User" UA ON A.USER_ID = UA.USER_ID;
        """)
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="No reviews found")
        result = [dict(zip(colums, row)) for row in rows]
        return result