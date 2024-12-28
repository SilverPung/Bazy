from fastapi import Depends, HTTPException
from database.connection import DatabaseConnection
import fdb



class GetAdvanced(DatabaseConnection):
    def __init__(self):
        super().__init__()

    def get_lone_user(self):
        try:
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
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_user_with_role(self):
        try:
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
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_property_with_repair_number(self):
        try:
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
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_renting_user(self):
        try:
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
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_property_cheaper_than_average(self):
        try:
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
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_property_by_type(self, type):
        try:
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
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_property_by_city(self, city):
        try:
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
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_user_from_city(self, city):
        try:
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
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_property_in_cities(self, cities: list):
        try:
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
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_property_not_in_cities(self, cities: list):
        try:
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
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_user_with_phone_numbers(self):
        try:
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
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_unique_cities_for_property(self):
        try:
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
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_agent_with_supervisor(self):
        try:
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
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_property_not_sold_or_rented(self):
        try:
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
                )
                ORDER BY P.CITY, P.ADDRESS;
            """)
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            if not rows:
                raise HTTPException(status_code=404, detail="No properties found")
            result = [dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_rents_with_money_paid_in_payment(self):
        try:
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
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_property_not_s_or_r_cheaper_then(self,budget):
        try:
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
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_possible_property_types(self):
        try:
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
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_review_with_client_and_agent(self):
        try:
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
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    def get_repairs_with_property(self):
        try:
            cursor = self.get_cursor()
            cursor.execute("""
                SELECT 
                    R.REPAIR_ID,
                    R.PROPERTY_ID,
                    R.DESCRIPTION,
                    R.STATUS,
                    R.REPAIR_DATE,
                    P.ADDRESS,
                    P.CITY,
                    P.STATE
                FROM 
                    "Repairs" R
                JOIN
                    "Property" P ON R.PROPERTY_ID = P.PROPERTY_ID;
            """)
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            if not rows:
                raise HTTPException(status_code=404, detail="No repairs found")
            result = [dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    def get_repair_with_property(self,repair_id):
        try:
            cursor = self.get_cursor()
            cursor.execute("""
                SELECT 
                    R.REPAIR_ID,
                    R.PROPERTY_ID,
                    R.DESCRIPTION,
                    R.STATUS,
                    R.REPAIR_DATE,
                    P.ADDRESS,
                    P.CITY,
                    P.STATE
                FROM 
                    "Repairs" R
                JOIN
                    "Property" P ON R.PROPERTY_ID = P.PROPERTY_ID
                WHERE R.REPAIR_ID = ?;
            """,(repair_id,))
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            if not rows:
                raise HTTPException(status_code=404, detail="No repairs found")
            result = [dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
        

    def get_sales_with_info(self):
        try:
            cursor = self.get_cursor()
            cursor.execute("""
                SELECT 
                    S.SALE_ID,
                    S.PROPERTY_ID,
                    S.CLIENT_ID,
                    S.AGENT_ID,
                    S.SALE_DATE,
                    S.STATUS,
                    P.ADDRESS,
                    P.CITY,
                    CU.NAME AS CLIENT_NAME,
                    CU.SURNAME AS CLIENT_SURNAME,
                    AU.NAME AS AGENT_NAME,
                    AU.SURNAME AS AGENT_SURNAME
                FROM 
                    "Sales" S
                JOIN
                    "Property" P ON S.PROPERTY_ID = P.PROPERTY_ID
                JOIN
                    "Client" C ON S.CLIENT_ID = C.USER_ID
                JOIN
                    "Agent" A ON S.AGENT_ID = A.USER_ID
                JOIN 
                    "User" CU ON C.USER_ID = CU.USER_ID   
                JOIN 
                    "User" AU ON A.USER_ID = AU.USER_ID
                ORDER BY P.CITY, P.ADDRESS, AU.SURNAME, AU.NAME;
            """)
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            if not rows:
                raise HTTPException(status_code=404, detail="No sales found")
            result = [dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    def get_meetings_with_info(self):
        try:
            cursor = self.get_cursor()
            cursor.execute("""
                SELECT 
                    M.MEETING_ID,
                    M.CLIENT_ID,
                    M.AGENT_ID,
                    M.DATE_MEETING,
                    M.TIME_MEETING,
                    M.STATUS,
                    CU.NAME AS CLIENT_NAME,
                    CU.SURNAME AS CLIENT_SURNAME,
                    AU.NAME AS AGENT_NAME,
                    AU.SURNAME AS AGENT_SURNAME,
                    P.ADDRESS,
                    P.CITY
                FROM 
                    "Meeting" M
                JOIN
                    "Client" C ON M.CLIENT_ID = C.USER_ID
                JOIN
                    "Agent" A ON M.AGENT_ID = A.USER_ID
                JOIN 
                    "User" CU ON C.USER_ID = CU.USER_ID   
                JOIN 
                    "User" AU ON A.USER_ID = AU.USER_ID
                JOIN 
                    "Property" P ON M.PROPERTY_ID = P.PROPERTY_ID
                ORDER BY P.CITY, P.ADDRESS, AU.SURNAME, AU.NAME;
            """)
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            if not rows:
                raise HTTPException(status_code=404, detail="No meetings found")
            result = [dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_client_with_sales(self,client_id):
        try:
            cursor = self.get_cursor()
            cursor.execute("""
                SELECT 
                    C.USER_ID,
                    S.SALE_ID,
                    S.PROPERTY_ID,
                    S.AGENT_ID,
                    A.NAME AS AGENT_NAME,
                    A.SURNAME AS AGENT_SURNAME,
                    S.SALE_DATE,
                    S.STATUS,
                    S.PRICE,
                    P.ADDRESS,
                    P.CITY,
                    P.STATE
                FROM 
                    "Client" C
                JOIN
                    "Sales" S ON C.USER_ID = S.CLIENT_ID
                JOIN
                    "User" A ON S.AGENT_ID = A.USER_ID
                JOIN
                    "Property" P ON S.PROPERTY_ID = P.PROPERTY_ID
                WHERE C.USER_ID = ?
            ORDER BY S.SALE_DATE DESC, P.CITY, P.ADDRESS;
            """,(client_id,))
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            if not rows:
                raise HTTPException(status_code=404, detail="No sales found")
            result = [dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_client_with_meetings(self,client_id):
        try:
            cursor = self.get_cursor()
            cursor.execute("""
                SELECT 
                    C.USER_ID,
                    M.MEETING_ID,
                    M.AGENT_ID,
                    A.NAME AS AGENT_NAME,
                    A.SURNAME AS AGENT_SURNAME,
                    M.DATE_MEETING,
                    M.TIME_MEETING,
                    M.STATUS,
                    P.ADDRESS,
                    P.CITY,
                    P.STATE
                FROM 
                    "Client" C
                JOIN
                    "Meeting" M ON C.USER_ID = M.CLIENT_ID
                JOIN
                    "User" A ON M.AGENT_ID = A.USER_ID
                JOIN
                    "Property" P ON M.PROPERTY_ID = P.PROPERTY_ID
                WHERE C.USER_ID = ?
            ORDER BY M.DATE_MEETING DESC, M.TIME_MEETING, P.CITY, P.ADDRESS;
            """,(client_id,))
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            if not rows:
                raise HTTPException(status_code=404, detail="No meetings found")
            result = [dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
            
    def get_client_with_rents(self,client_id):

        try:
            cursor = self.get_cursor()
            cursor.execute("""
                SELECT 
                    C.USER_ID,
                    R.RENT_ID,
                    R.PROPERTY_ID,
                    R.START_DATE,
                    R.END_DATE,
                    R.DEPOSIT,
                    R.STATUS,
                    P.ADDRESS,
                    P.CITY,
                    P.STATE
                FROM 
                    "Client" C
                JOIN
                    "Rents" R ON C.USER_ID = R.CLIENT_ID
                JOIN
                    "Property" P ON R.PROPERTY_ID = P.PROPERTY_ID
                WHERE C.USER_ID = ?
            ORDER BY R.START_DATE DESC, P.CITY, P.ADDRESS;
                           
            """,(client_id,))
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            if not rows:
                raise HTTPException(status_code=404, detail="No rents found")
            result = [dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
        

    def get_property_with_repairs(self,property_id):
        try:
            cursor = self.get_cursor()
            cursor.execute("""
                SELECT 
                    P.PROPERTY_ID,
                    R.REPAIR_ID,
                    R.DESCRIPTION,
                    R.STATUS,
                    R.REPAIR_DATE
                FROM 
                    "Property" P
                JOIN
                    "Repairs" R ON P.PROPERTY_ID = R.PROPERTY_ID
                WHERE P.PROPERTY_ID = ?
                ORDER BY R.REPAIR_DATE DESC;
                           
            """,(property_id,))
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            if not rows:
                raise HTTPException(status_code=404, detail="No repairs found")
            result = [dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_property_with_sales(self,property_id):
        try:
            cursor = self.get_cursor()
            cursor.execute("""
                SELECT 
                    P.PROPERTY_ID,
                    S.SALE_ID,
                    S.CLIENT_ID,
                    S.AGENT_ID,
                    S.SALE_DATE,
                    S.STATUS
                FROM 
                    "Property" P
                JOIN
                    "Sales" S ON P.PROPERTY_ID = S.PROPERTY_ID
                WHERE P.PROPERTY_ID = ?
                ORDER BY S.SALE_DATE DESC;
            """,(property_id,))
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            if not rows:
                raise HTTPException(status_code=404, detail="No sales found")
            result = [dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    def get_property_with_rents(self,property_id):
        try:
            cursor = self.get_cursor()
            cursor.execute("""
                SELECT 
                    P.PROPERTY_ID,
                    R.RENT_ID,
                    R.CLIENT_ID,
                    R.START_DATE,
                    R.END_DATE,
                    R.STATUS
                FROM 
                    "Property" P
                JOIN
                    "Rents" R ON P.PROPERTY_ID = R.PROPERTY_ID
                WHERE P.PROPERTY_ID = ?
                ORDER BY R.START_DATE DESC;
            """,(property_id,))
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            if not rows:
                raise HTTPException(status_code=404, detail="No rents found")
            result = [dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    def get_property_with_meetings(self,property_id):
        try:
            cursor = self.get_cursor()
            cursor.execute("""
                SELECT 
                    P.PROPERTY_ID,
                    M.MEETING_ID,
                    M.CLIENT_ID,
                    M.AGENT_ID,
                    M.DATE_MEETING,
                    M.TIME_MEETING,
                    U.NAME AS CLIENT_NAME,
                    U.SURNAME AS CLIENT_SURNAME,
                    A.NAME AS AGENT_NAME,
                    A.SURNAME AS AGENT_SURNAME,
                    M.STATUS
                FROM 
                    "Property" P
                JOIN
                    "Meeting" M ON P.PROPERTY_ID = M.PROPERTY_ID
                JOIN
                    "User" U ON M.CLIENT_ID = U.USER_ID
                JOIN
                    "User" A ON M.AGENT_ID = A.USER_ID
                WHERE P.PROPERTY_ID = ?
                ORDER BY M.DATE_MEETING DESC, M.TIME_MEETING;
            """,(property_id,))
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            if not rows:
                raise HTTPException(status_code=404, detail="No meetings found")
            result = [dict(zip(colums, row)) for row in rows]
            return result
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))




