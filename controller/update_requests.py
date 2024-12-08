from database.dbUpdate import UpdateOne
from fastapi import APIRouter

router = APIRouter()
UpdateOne = UpdateOne()

@router.put("/agency/agent/{user_id}")
def update_agent(user_id: int, license_number: str, commision_rate: float, employement_date: str):
    UpdateOne.update_agent(user_id, license_number, commision_rate, employement_date)
    return {"status": "Agent updated"}

@router.put("/agency/agreement/{agreement_id}")
def update_agreement(agreement_id: int, title: str, description: str, agreement_date: str, user_id: int):
    UpdateOne.update_agreement(agreement_id, title, description, agreement_date, user_id)
    return {"status": "Agreement updated"}

@router.put("/agency/client/{user_id}")
def update_client(user_id: int, budget: float, preffered_location: str):
    UpdateOne.update_client(user_id, budget, preffered_location)
    return {"status": "Client updated"}

@router.put("/agency/manager/{user_id}")
def update_manager(user_id: int, supervision_area: str, employment_date: str):
    UpdateOne.update_manager(user_id, supervision_area, employment_date)
    return {"status": "Manager updated"}

@router.put("/agency/manager_agent/{manager_id}")
def update_manager_agent(manager_id: int, agent_id: int):
    UpdateOne.update_manager_agent(manager_id, agent_id)
    return {"status": "Manager-Agent relationship updated"}

@router.put("/agency/meeting/{meeting_id}")
def update_meeting(meeting_id: int, date_meeting: str, time_meeting: str, status: str, property_id: int, client_id: int, agent_id: int):
    UpdateOne.update_meeting(meeting_id, date_meeting, time_meeting, status, property_id, client_id, agent_id)
    return {"status": "Meeting updated"}

@router.put("/agency/payment/{payment_id}")
def update_payment(payment_id: int, amount: float, payment_date: str, status: str, method: str, rent_id: int):
    UpdateOne.update_payment(payment_id, amount, payment_date, status, method, rent_id)
    return {"status": "Payment updated"}

@router.put("/agency/property/{property_id}")
def update_property(property_id: int, address: str, city: str, state: str, postal_code: str, size: float, bedrooms: int, bathrooms: int, price: float, status: str, type: str, description: str):
    UpdateOne.update_property(property_id, address, city.capitalize(), state, postal_code, size, bedrooms, bathrooms, price, status, type, description)
    return {"status": "Property updated"}

@router.put("/agency/rent/{rent_id}")
def update_rent(rent_id: int, start_date: str, end_date: str, deposit: float, status: str, client_id: int, property_id: int):
    UpdateOne.update_rent(rent_id, start_date, end_date, deposit, status, client_id, property_id)
    return {"status": "Rent updated"}

@router.put("/agency/repair/{repair_id}")
def update_repair(repair_id: int, repair_date: str, status: str, description: str, property_id: int):
    UpdateOne.update_repair(repair_id, repair_date, status, description, property_id)
    return {"status": "Repair updated"}

@router.put("/agency/review/{review_id}")
def update_review(review_id: int, rating: int, description: str, client_id: int, agent_id: int):
    UpdateOne.update_review(review_id, rating, description, client_id, agent_id)
    return {"status": "Review updated"}

@router.put("/agency/sale/{sale_id}")
def update_sale(sale_id: int, price: float, status: str, sale_date: str, property_id: int, client_id: int, agent_id: int):
    UpdateOne.update_sale(sale_id, price, status, sale_date, property_id, client_id, agent_id)
    return {"status": "Sale updated"}

@router.put("/agency/tel_number/{user_id}")
def update_tel_number(user_id: int, tel_number: str):
    UpdateOne.update_tel_number(user_id, tel_number)
    return {"status": "Telephone number updated"}

@router.put("/agency/user/{user_id}")
def update_user(user_id: int, name: str, surname: str, email: str, password: str, address: str):
    UpdateOne.update_user(user_id, name, surname, email, password, address)
    return {"status": "User updated"}
