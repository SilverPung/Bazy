from database.connection import DatabaseConnection
from fastapi import HTTPException
import fdb

class InsertOne(DatabaseConnection):
    def __init__(self):
        super().__init__()

    def insert_agent(self, user_id, license_number, commision_rate, employement_date):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                INSERT INTO "Agent" (USER_ID, LICENSE_NUMBER, COMMISION_RATE, EMPLOYEMENT_DATE)
                VALUES (?, ?, ?, ?)
            ''', (user_id, license_number, commision_rate, employement_date))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def insert_agreement(self, title, description, agreement_date, user_id):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                INSERT INTO "Agreement" (TITLE, DESCRIPTION, AGREEMENT_DATE, USER_ID)
                VALUES (?, ?, ?, ?)
            ''', (title, description, agreement_date, user_id))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def insert_client(self, user_id, budget, preffered_location):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                INSERT INTO "Client" (USER_ID, BUDGET, PREFFERED_LOCATION)
                VALUES (?, ?, ?)
            ''', (user_id, budget, preffered_location))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def insert_manager(self, user_id, supervision_area, employment_date):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                INSERT INTO "Manager" (USER_ID, SUPERVISION_AREA, EMPLOYEMENT_DATE)
                VALUES (?, ?, ?)
            ''', (user_id, supervision_area, employment_date))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def insert_manager_agent(self, manager_id, agent_id):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                INSERT INTO "ManagerAgent" (MANAGER_ID, AGENT_ID)
                VALUES (?, ?)
            ''', (manager_id, agent_id))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def insert_meeting(self, date_meeting, time_meeting, status, property_id, client_id, agent_id):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                INSERT INTO "Meeting" (DATE_MEETING, TIME_MEETING, STATUS, PROPERTY_ID, CLIENT_ID, AGENT_ID)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (date_meeting, time_meeting, status, property_id, client_id, agent_id))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def insert_payment(self, amount, payment_date, status, method, rent_id):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                INSERT INTO "Payment" (AMOUNT, PAYMENT_DATE, STATUS, METHOD, RENT_ID)
                VALUES (?, ?, ?, ?, ?)
            ''', (amount, payment_date, status, method, rent_id))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def insert_property(self, address, city, state, postal_code, size, bedrooms, bathrooms, price, type1, description):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                INSERT INTO "Property" (ADDRESS, CITY, STATE, POSTAL_CODE, SIZE, BEDROOMS, BATHROOMS, PRICE, TYPE, DESCRIPTION)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (address, city, state, postal_code, size, bedrooms, bathrooms, price, type1, description))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def insert_rent(self, start_date, end_date, price, deposit, status, client_id, property_id):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                INSERT INTO "Rents" (START_DATE, END_DATE, DEPOSIT, STATUS, CLIENT_ID, PROPERTY_ID, PRICE)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (start_date, end_date, deposit, status, client_id, property_id,price))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def insert_repair(self, repair_date, status, description, property_id):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                INSERT INTO "Repairs" (REPAIR_DATE, STATUS, DESCRIPTION, PROPERTY_ID)
                VALUES (?, ?, ?, ?)
            ''', (repair_date, status, description, property_id))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def insert_review(self, rating, description, client_id, agent_id):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                INSERT INTO "Review" (RATING, DESCRIPTION, CLIENT_ID, AGENT_ID)
                VALUES (?, ?, ?, ?)
            ''', (rating, description, client_id, agent_id))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def insert_sale(self, price, status, sale_date, property_id, client_id, agent_id):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                INSERT INTO "Sales" (PRICE, STATUS, SALE_DATE, PROPERTY_ID, CLIENT_ID, AGENT_ID)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (price, status, sale_date, property_id, client_id, agent_id))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def insert_tel_number(self, user_id, tel_number):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                INSERT INTO "Tel_number" (USER_ID, TEL_NUMBER)
                VALUES (?, ?)
            ''', (user_id, tel_number))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def insert_user(self, name, surname, email, password, address):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                INSERT INTO "User" (NAME, SURNAME, EMAIL, PASSWORD, ADDRESS)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, surname, email, password, address))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

class InsertByProcedure(DatabaseConnection):
    def __init__(self):
        super().__init__()

    def insert_new_client(self, name, surname, email, password, address, budget, preffered_location):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                EXECUTE PROCEDURE CREATE_CLIENT (?, ?, ?, ?, ?, ?, ?)
            ''', (name, surname, email, password, address, budget, preffered_location))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    def insert_new_agent(self, name, surname, email, password, address, license_number, commision_rate, employement_date):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                EXECUTE PROCEDURE CREATE_AGENT (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (name, surname, email, password, address, license_number, commision_rate, employement_date))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def insert_new_manager(self, name, surname, email, password, address, supervision_area, employment_date):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                EXECUTE PROCEDURE CREATE_MANAGER (?, ?, ?, ?, ?, ?, ?)
            ''', (name, surname, email, password, address, supervision_area, employment_date))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def update_property_status(self):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                 EXECUTE PROCEDURE UpdatePropertyStatus;
            ''')
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
        
if __name__ == '__main__':
    insert = InsertOne()
    insert.insert_property("Marii Skłodowskiej Curie 82/1", 'Bydgoszcz', 'Kujawsko-Pomorskie', '85-733', 130, 3, 2, 600000, 'AVAILABLE', 'Flat', 'A beautiful flat in the city center.')


