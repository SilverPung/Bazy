from database.connection import DatabaseConnection
from fastapi import HTTPException
import fdb

class DeleteOne(DatabaseConnection):
    def __init__(self):
        super().__init__()

    def delete_agent(self, user_id):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                DELETE FROM "Agent" WHERE USER_ID = ?
            ''', (user_id,))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def delete_agreement(self, agreement_id):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                DELETE FROM "Agreement" WHERE AGREEMENT_ID = ?
            ''', (agreement_id,))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def delete_client(self, user_id):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                DELETE FROM "Client" WHERE USER_ID = ?
            ''', (user_id,))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def delete_manager(self, user_id):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                DELETE FROM "Manager" WHERE USER_ID = ?
            ''', (user_id,))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def delete_manager_agent(self, manager_id, agent_id):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                DELETE FROM "ManagerAgent" WHERE MANAGER_ID = ? AND AGENT_ID = ?
            ''', (manager_id, agent_id))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def delete_meeting(self, meeting_id):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                DELETE FROM "Meeting" WHERE MEETING_ID = ?
            ''', (meeting_id,))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def delete_payment(self, payment_id):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                DELETE FROM "Payment" WHERE PAYMENT_ID = ?
            ''', (payment_id,))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def delete_property(self, property_id):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                DELETE FROM "Property" WHERE PROPERTY_ID = ?
            ''', (property_id,))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def delete_rent(self, rent_id):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                DELETE FROM "Rents" WHERE RENT_ID = ?
            ''', (rent_id,))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def delete_repair(self, repair_id):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                DELETE FROM "Repairs" WHERE REPAIR_ID = ?
            ''', (repair_id,))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def delete_review(self, review_id):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                DELETE FROM "Review" WHERE REVIEW_ID = ?
            ''', (review_id,))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def delete_sale(self, sale_id):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                DELETE FROM "Sales" WHERE SALE_ID = ?
            ''', (sale_id,))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def delete_tel_number(self, user_id, tel_number):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                DELETE FROM "Tel_number" WHERE USER_ID = ? AND TEL_NUMBER = ?
            ''', (user_id, tel_number))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def delete_user(self, user_id):
        try:
            cursor = self.get_cursor()
            cursor.execute('''
                DELETE FROM "User" WHERE USER_ID = ?
            ''', (user_id,))
            self.commit()
        except fdb.Error as e:
            raise HTTPException(status_code=500, detail=str(e))
