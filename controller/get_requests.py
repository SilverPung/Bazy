from database.dbGet import GetAll,GetOne
from fastapi import APIRouter


router = APIRouter()
GetAll = GetAll()
GetOne = GetOne()


@router.get("/agency/property")
def get_property():
    return GetAll.get_property()

@router.get("/agency/user")
def get_user():
    return GetAll.get_user()

@router.get("/agency/repair")
def get_repairs():
    return GetAll.get_repairs()

@router.get("/agency/meeting")
def get_meeting():
    return GetAll.get_meeting()

@router.get("/agency/sale")
def get_sales():
    return GetAll.get_sales()

@router.get("/agency/rent")
def get_rent():
    return GetAll.get_rent()

@router.get("/agency/payment")
def get_payment():
    return GetAll.get_payment()

@router.get("/agency/tel_number")
def get_tel_number():
    return GetAll.get_tel_number()

@router.get("/agency/review")
def get_reviews():
    return GetAll.get_reviews()

@router.get("/agency/agreement")
def get_agreements():
    return GetAll.get_agreements()

@router.get("/agency/agent")
def get_agent():
    return GetAll.get_agent()

@router.get("/agency/client")
def get_client():
    return GetAll.get_client()

@router.get("/agency/manager")
def get_manager():
    return GetAll.get_manager()


@router.get("/agency/property/{property_id}")
def get_property_by_id(property_id: int):
    return GetOne.get_property(property_id)

@router.get("/agency/user/{user_id}")
def get_user_by_id(user_id: int):
    return GetOne.get_user(user_id)

@router.get("/agency/repair/{repair_id}")
def get_repair_by_id(repair_id: int):
    return GetOne.get_repair(repair_id)

@router.get("/agency/meeting/{meeting_id}")
def get_meeting_by_id(meeting_id: int):
    return GetOne.get_meeting(meeting_id)
    
@router.get("/agency/sale/{sale_id}")
def get_sale_by_id(sale_id: int):
    return GetOne.get_sell(sale_id)

@router.get("/agency/rent/{rent_id}")
def get_rent_by_id(rent_id: int):
    return GetOne.get_rent(rent_id)

@router.get("/agency/payment/{payment_id}")
def get_payment_by_id(payment_id: int):
    return GetOne.get_payment(payment_id)

@router.get("/agency/tel_number/{tel_number_id}")
def get_tel_number_by_id(tel_number_id: int):
    return GetOne.get_tel_number(tel_number_id)

@router.get("/agency/review/{review_id}")
def get_review_by_id(review_id: int):
    return GetOne.get_review(review_id)

@router.get("/agency/agreement/{agreement_id}")
def get_agreement_by_id(agreement_id: int):
    return GetOne.get_agreement(agreement_id)

@router.get("/agency/agent/{agent_id}")
def get_agent_by_id(agent_id: int):
    return GetOne.get_agent(agent_id)

@router.get("/agency/client/{client_id}")
def get_client_by_id(client_id: int):
    return GetOne.get_client(client_id)

@router.get("/agency/manager/{manager_id}")
def get_manager_by_id(manager_id: int):
    return GetOne.get_manager(manager_id)

