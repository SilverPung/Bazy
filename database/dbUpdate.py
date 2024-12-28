from database.connection import DatabaseConnection
from fastapi import HTTPException
import fdb
import sys

class UpdateOne(DatabaseConnection):
    def __init__(self):
        super().__init__()

    def update_agent(self, user_id, license_number, commision_rate, employement_date):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                UPDATE "Agent"
                SET LICENSE_NUMBER = ?, COMMISION_RATE = ?, EMPLOYEMENT_DATE = ?
                WHERE USER_ID = ?
            ''', (license_number, commision_rate, employement_date, user_id))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def update_agreement(self, agreement_id, title, description, agreement_date, user_id):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                UPDATE "Agreement"
                SET TITLE = ?, DESCRIPTION = ?, AGREEMENT_DATE = ?, USER_ID = ?
                WHERE AGREEMENT_ID = ?
            ''', (title, description, agreement_date, user_id, agreement_id))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def update_client(self, user_id, budget, preffered_location):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                UPDATE "Client"
                SET BUDGET = ?, PREFFERED_LOCATION = ?
                WHERE USER_ID = ?
            ''', (budget, preffered_location, user_id))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def update_manager(self, user_id, supervision_area, employment_date):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                UPDATE "Manager"
                SET SUPERVISION_AREA = ?, EMPLOYMENT_DATE = ?
                WHERE USER_ID = ?
            ''', (supervision_area, employment_date, user_id))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def update_manager_agent(self, manager_id, agent_id):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                UPDATE "ManagerAgent"
                SET AGENT_ID = ?
                WHERE MANAGER_ID = ?
            ''', (agent_id, manager_id))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def update_meeting(self, meeting_id, date_meeting, time_meeting, status, property_id, client_id, agent_id):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                UPDATE "Meeting"
                SET DATE_MEETING = ?, TIME_MEETING = ?, STATUS = ?, PROPERTY_ID = ?, CLIENT_ID = ?, AGENT_ID = ?
                WHERE MEETING_ID = ?
            ''', (date_meeting, time_meeting, status, property_id, client_id, agent_id, meeting_id))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def update_payment(self, payment_id, amount, payment_date, status, method, rent_id):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                UPDATE "Payment"
                SET AMOUNT = ?, PAYMENT_DATE = ?, STATUS = ?, METHOD = ?, RENT_ID = ?
                WHERE PAYMENT_ID = ?
            ''', (amount, payment_date, status, method, rent_id, payment_id))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def update_property(self, property_id, address, city, state, postal_code, size, bedrooms, bathrooms, price, type1, description):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                UPDATE "Property"
                SET ADDRESS = ?, CITY = ?, STATE = ?, POSTAL_CODE = ?, SIZE = ?, BEDROOMS = ?, BATHROOMS = ?, PRICE = ?, TYPE = ?, DESCRIPTION = ?
                WHERE PROPERTY_ID = ?
            ''', (address, city, state, postal_code, size, bedrooms, bathrooms, price, type1, description, property_id))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def update_rent(self, rent_id, start_date, end_date, price, deposit, status, client_id, property_id):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                UPDATE "Rents"
                SET START_DATE = ?, END_DATE = ?, DEPOSIT = ?, STATUS = ?, CLIENT_ID = ?, PROPERTY_ID = ?, PRICE = ?
                WHERE RENT_ID = ?
            ''', (start_date, end_date, deposit, status, client_id, property_id, rent_id, price))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def update_repair(self, repair_id, repair_date, status, description, property_id):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                UPDATE "Repairs"
                SET REPAIR_DATE = ?, STATUS = ?, DESCRIPTION = ?, PROPERTY_ID = ?
                WHERE REPAIR_ID = ?
            ''', (repair_date, status, description, property_id, repair_id))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def update_review(self, review_id, rating, description, client_id, agent_id):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                UPDATE "Review"
                SET RATING = ?, DESCRIPTION = ?, CLIENT_ID = ?, AGENT_ID = ?
                WHERE REVIEW_ID = ?
            ''', (rating, description, client_id, agent_id, review_id))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def update_sale(self, sale_id, price, status, sale_date, property_id, client_id, agent_id):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                UPDATE "Sales"
                SET PRICE = ?, STATUS = ?, SALE_DATE = ?, PROPERTY_ID = ?, CLIENT_ID = ?, AGENT_ID = ?
                WHERE SALE_ID = ?
            ''', (price, status, sale_date, property_id, client_id, agent_id, sale_id))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def update_tel_number(self, user_id, tel_number):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                UPDATE "Tel_number"
                SET TEL_NUMBER = ?
                WHERE USER_ID = ?
            ''', (tel_number, user_id))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def update_user(self, user_id, name, surname, email, password, address):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                UPDATE "User"
                SET NAME = ?, SURNAME = ?, EMAIL = ?, PASSWORD = ?, ADDRESS = ?
                WHERE USER_ID = ?
            ''', (name, surname, email, password, address, user_id))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))


class UpdateByProcedure(DatabaseConnection):
    def __init__(self):
        super().__init__()
    
    def update_client(self, user_id, name, surname, email, password, address, budget, preffered_location):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                EXECUTE PROCEDURE UPDATE_CLIENT(?, ?, ?, ?, ?, ?, ?, ?)
            ''', (user_id, name, surname, email, password, address, budget, preffered_location))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    def update_agent(self, user_id, name, surname, email, password, address, license_number, commision_rate, employment_date):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                EXECUTE PROCEDURE UPDATE_AGENT(?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (user_id, name, surname, email, password, address, license_number, commision_rate, employment_date))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    def update_manager(self, user_id, name, surname, email, password, address, supervision_area, employment_date):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                EXECUTE PROCEDURE UPDATE_MANAGER(?, ?, ?, ?, ?, ?, ?, ?)
            ''', (user_id, name, surname, email, password, address, supervision_area, employment_date))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
        