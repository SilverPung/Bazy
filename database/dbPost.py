from database.connection import DatabaseConnection

class InsertOne(DatabaseConnection):
    
    def __init__(self):
        super().__init__()

    def insert_agent(self,user_id, license_number, commision_rate, employement_date):
        cursor = self.get_cursor()
        cursor.execute('''
            INSERT INTO "Agent" (USER_ID, LICENSE_NUMBER, COMMISION_RATE, EMPLOYEMENT_DATE)
            VALUES (?, ?, ?, ?)
        ''', (user_id, license_number, commision_rate, employement_date))
        self.commit()

    def insert_agreement(self, title, description, agreement_date, user_id):
        cursor = self.get_cursor()
        cursor.execute('''
            INSERT INTO "Agreement" (TITLE, DESCRIPTION, AGREEMENT_DATE, USER_ID)
            VALUES (?, ?, ?, ?)
        ''', (title, description, agreement_date, user_id))
        self.commit()

    def insert_client(self,user_id ,budget, preffered_location):
        cursor = self.get_cursor()
        cursor.execute('''
            INSERT INTO "Client" (USER_ID ,BUDGET, PREFFERED_LOCATION)
            VALUES (?, ?, ?)
        ''', (user_id,budget, preffered_location))
        self.commit()

    def insert_manager(self,user_id, supervision_area, employment_date):
        cursor = self.get_cursor()
        cursor.execute('''
            INSERT INTO "Manager" (USER_ID, SUPERVISION_AREA, EMPLOYEMENT_DATE)
            VALUES (?, ?, ?)
        ''', (user_id, supervision_area, employment_date))
        self.commit()

    def insert_manager_agent(self, manager_id, agent_id):
        cursor = self.get_cursor()
        cursor.execute('''
            INSERT INTO "ManagerAgent" (MANAGER_ID, AGENT_ID)
            VALUES (?, ?)
        ''', (manager_id, agent_id))
        self.commit()

    def insert_meeting(self, date_meeting, time_meeting, status, property_id, client_id, agent_id):
        cursor = self.get_cursor()
        cursor.execute('''
            INSERT INTO "Meeting" (DATE_MEETING, TIME_MEETING, STATUS, PROPERTY_ID, CLIENT_ID, AGENT_ID)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (date_meeting, time_meeting, status, property_id, client_id, agent_id))
        self.commit()

    def insert_payment(self, amount, payment_date, status, method, rent_id):
        cursor = self.get_cursor()
        cursor.execute('''
            INSERT INTO "Payment" (AMOUNT, PAYMENT_DATE, STATUS, METHOD, RENT_ID)
            VALUES (?, ?, ?, ?, ?)
        ''', (amount, payment_date, status, method, rent_id))
        self.commit()

    def insert_property(self, address, city, state, postal_code, size, bedrooms, bathrooms, price, status, type, description):
        cursor = self.get_cursor()
        cursor.execute('''
            INSERT INTO "Property" (ADDRESS, CITY, STATE, POSTAL_CODE, SIZE, BEDROOMS, BATHROOMS, PRICE, STATUS, TYPE, DESCRIPTION)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (address, city, state, postal_code, size, bedrooms, bathrooms, price, status, type, description))
        self.commit()

    def insert_rent(self, start_date, end_date, deposit, status, client_id, property_id):
        cursor = self.get_cursor()
        cursor.execute('''
            INSERT INTO "Rents" (START_DATE, END_DATE, DEPOSIT, STATUS, CLIENT_ID, PROPERTY_ID)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (start_date, end_date, deposit, status, client_id, property_id))
        self.commit()

    def insert_repair(self, repair_date, status, description, property_id):
        cursor = self.get_cursor()
        cursor.execute('''
            INSERT INTO "Repairs" (REPAIR_DATE, STATUS, DESCRIPTION, PROPERTY_ID)
            VALUES (?, ?, ?, ?)
        ''', (repair_date, status, description, property_id))
        self.commit()

    def insert_review(self, rating, description, client_id, agent_id):
        cursor = self.get_cursor()
        cursor.execute('''
            INSERT INTO "Review" (RATING, DESCRIPTION, CLIENT_ID, AGENT_ID)
            VALUES (?, ?, ?, ?)
        ''', (rating, description, client_id, agent_id))
        self.commit()

    def insert_sale(self, price, status, sale_date, property_id, client_id, agent_id):
        cursor = self.get_cursor()
        cursor.execute('''
            INSERT INTO "Sales" (PRICE, STATUS, SALE_DATE, PROPERTY_ID, CLIENT_ID, AGENT_ID)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (price, status, sale_date, property_id, client_id, agent_id))
        self.commit()

    def insert_tel_number(self, user_id, tel_number):
        cursor = self.get_cursor()
        cursor.execute('''
            INSERT INTO "Tel_number" (USER_ID, TEL_NUMBER)
            VALUES (?, ?)
        ''', (user_id, tel_number))
        self.commit()

    def insert_user(self, name, surname, email, password, address):
        cursor = self.get_cursor()
        cursor.execute('''
            INSERT INTO "User" (NAME, SURNAME, EMAIL, PASSWORD, ADDRESS)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, surname, email, password, address))
        self.commit()


class InsertByProcedure(DatabaseConnection):
        
    def __init__(self):
        super().__init__()

    def insert_new_client(self, name, surname, email, password, address, budget, preffered_location):
        cursor = self.get_cursor()
        cursor.execute('''
            EXECUTE PROCEDURE CREATE_CLIENT (?, ?, ?, ?, ?, ?, ?)
        ''', (name, surname, email, password, address, budget, preffered_location))
        self.commit()
        
    def insert_new_agent(self, name, surname, email, password, address, license_number, commision_rate, employement_date):
        cursor = self.get_cursor()
        cursor.execute('''
            EXECUTE PROCEDURE CREATE_AGENT (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, surname, email, password, address, license_number, commision_rate, employement_date))
        self.commit()
    
    def insert_new_manager(self, name, surname, email, password, address, supervision_area, employment_date):
        cursor = self.get_cursor()
        cursor.execute('''
            EXECUTE PROCEDURE CREATE_MANAGER (?, ?, ?, ?, ?, ?, ?)
        ''', (name, surname, email, password, address, supervision_area, employment_date))
        self.commit()


if __name__ == '__main__':
    insert = InsertOne()

    insert.insert_property("Marii Skłodowskiej Curie 82/1", 'Bydgoszcz', 'Kujawsko-Pomorskie', '85-733', 130, 3, 2, 600000, 'AVAILABLE', 'Flat', 'A beautiful flat in the city center.')


