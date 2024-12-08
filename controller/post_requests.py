from database.dbPost import InsertOne, InsertByProcedure
from fastapi import APIRouter

router = APIRouter()
InsertOne = InsertOne()

@router.post("/agency/property",description="Status can be 'AVAILABLE', 'PENDING', 'SOLD'")
def insert_property(address: str, city: str, state: str, postal_code: str, size: int, bedrooms: int, bathrooms: int, price: float, status: str, type: str, description: str):
    InsertOne.insert_property(address, city, state, postal_code, size, bedrooms, bathrooms, price, status, type, description)
    return {"message": "Property inserted successfully"}

@router.post("/agency/user")
def insert_user(name: str, surname: str, email: str, password: str, address: str):
    InsertOne.insert_user(name, surname, email, password, address)
    return {"message": "User inserted successfully"}

@router.post("/agency/agent")
def insert_agent(user_id:int ,license_number: str, commision_rate: float, employement_date: str):
    InsertOne.insert_agent(user_id, license_number, commision_rate, employement_date)
    return {"message": "Agent inserted successfully"}

@router.post("/agency/agreement")
def insert_agreement(title: str, description: str, agreement_date: str, user_id: int):
    InsertOne.insert_agreement(title, description, agreement_date, user_id)
    return {"message": "Agreement inserted successfully"}

@router.post("/agency/client")
def insert_client(user_id: int, budget: float, preffered_location: str):
    InsertOne.insert_client(user_id, budget, preffered_location)
    return {"message": "Client inserted successfully"}

@router.post("/agency/manager")
def insert_manager(user_id: int, supervision_area: str, employment_date: str):
    InsertOne.insert_manager(user_id, supervision_area, employment_date)
    return {"message": "Manager inserted successfully"}

@router.post("/agency/manager_agent")
def insert_manager_agent(manager_id: int, agent_id: int):
    InsertOne.insert_manager_agent(manager_id, agent_id)
    return {"message": "Manager-Agent relationship inserted successfully"}

@router.post("/agency/meeting", summary="Insert a new meeting", description="Status can be 'Scheduled', 'ReScheduled', 'Completed', 'Cancelled'.")
def insert_meeting(date_meeting: str, time_meeting: str, status: str, property_id: int, client_id: int, agent_id: int):
    """
    Insert a new meeting.
    Status can be 'Scheduled', 'ReScheduled', 'Completed', 'Cancelled'.
    """
    InsertOne.insert_meeting(date_meeting, time_meeting, status, property_id, client_id, agent_id)
    return {"message": "Meeting inserted successfully"}

@router.post("/agency/payment", summary="Insert a new payment", description="Status can be 'Pending', 'Paid', 'Failed'.")
def insert_payment(amount: float, payment_date: str, status: str, method: str, rent_id: int):
    """
    Insert a new payment.
    Status can be 'Pending', 'Paid', 'Failed'.
    """
    InsertOne.insert_payment(amount, payment_date, status, method, rent_id)
    return {"message": "Payment inserted successfully"}

@router.post("/agency/rent", summary="Insert a new rent", description="Status can be 'Pending', 'Ended', 'Active'.")
def insert_rent(start_date: str, end_date: str, deposit: float, status: str, client_id: int, property_id: int):
    """
    Insert a new rent.
    Status can be 'Pending', 'Ended', 'Active'.
    """
    InsertOne.insert_rent(start_date, end_date, deposit, status, client_id, property_id)
    return {"message": "Rent inserted successfully"}

@router.post("/agency/repair", summary="Insert a new repair", description="Status can be 'Pending', 'In Progress', 'Completed', 'Rescheduled'.")
def insert_repair(repair_date: str, status: str, description: str, property_id: int):
    """
    Insert a new repair.
    Status can be 'Pending', 'In Progress', 'Completed', 'Rescheduled'.
    """
    InsertOne.insert_repair(repair_date, status, description, property_id)
    return {"message": "Repair inserted successfully"}

@router.post("/agency/review")
def insert_review(rating: int, description: str, client_id: int, agent_id: int):
    InsertOne.insert_review(rating, description, client_id, agent_id)
    return {"message": "Review inserted successfully"}

@router.post("/agency/sale", summary="Insert a new sale", description="Status can be 'Pending', 'Completed', 'Cancelled'.")
def insert_sale(price: float, status: str, sale_date: str, property_id: int, client_id: int, agent_id: int):
    """
    Insert a new sale.
    Status can be 'Pending', 'Completed', 'Cancelled'.
    """
    InsertOne.insert_sale(price, status, sale_date, property_id, client_id, agent_id)
    return {"message": "Sale inserted successfully"}

@router.post("/agency/tel_number")
def insert_tel_number(user_id: int, tel_number: str):
    InsertOne.insert_tel_number(user_id, tel_number)
    return {"message": "Telephone number inserted successfully"}


@router.post("/agency/procedure/client")
def insert_new_client(name: str, surname: str, email: str, password: str, address: str, budget: float, preffered_location: str):
    print(f"Name: {name}, Surname: {surname}, Email: {email}, Password: {password}, Address: {address}, Budget: {budget}, Preffered Location: {preffered_location}")
    insert_by_procedure = InsertByProcedure()  # Instantiate the class
    insert_by_procedure.insert_new_client(name=name, surname=surname, email=email, password=password, address=address, budget=budget, preffered_location=preffered_location)
    return {"message": "New client inserted successfully"}

@router.post("/agency/procedure/agent")
def insert_new_agent(name: str, surname: str, email: str, password: str, address: str, license_number: str, commision_rate: float, employement_date: str):
    insert_by_procedure = InsertByProcedure()  # Instantiate the class
    insert_by_procedure.insert_new_agent(name, surname, email, password, address, license_number, commision_rate, employement_date)
    return {"message": "New agent inserted successfully"}

@router.post("/agency/procedure/manager")
def insert_new_manager(name: str, surname: str, email: str, password: str, address: str, supervision_area: str, employment_date: str):
    insert_by_procedure = InsertByProcedure()  # Instantiate the class
    insert_by_procedure.insert_new_manager(name, surname, email, password, address, supervision_area, employment_date)
    return {"message": "New manager inserted successfully"}
