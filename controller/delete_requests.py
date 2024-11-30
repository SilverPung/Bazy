from database.dbDelete import DeleteOne
from fastapi import APIRouter

router = APIRouter()
DeleteOne = DeleteOne()

@router.delete("/agency/agent/{user_id}")
def delete_agent(user_id: int):
    DeleteOne.delete_agent(user_id)
    return {"message": "Agent deleted successfully"}

@router.delete("/agency/agreement/{agreement_id}")
def delete_agreement(agreement_id: int):
    DeleteOne.delete_agreement(agreement_id)
    return {"message": "Agreement deleted successfully"}

@router.delete("/agency/client/{user_id}")
def delete_client(user_id: int):
    DeleteOne.delete_client(user_id)
    return {"message": "Client deleted successfully"}

@router.delete("/agency/manager/{user_id}")
def delete_manager(user_id: int):
    DeleteOne.delete_manager(user_id)
    return {"message": "Manager deleted successfully"}

@router.delete("/agency/manager_agent/{manager_id}/{agent_id}")
def delete_manager_agent(manager_id: int, agent_id: int):
    DeleteOne.delete_manager_agent(manager_id, agent_id)
    return {"message": "Manager-Agent relationship deleted successfully"}

@router.delete("/agency/meeting/{meeting_id}")
def delete_meeting(meeting_id: int):
    DeleteOne.delete_meeting(meeting_id)
    return {"message": "Meeting deleted successfully"}

@router.delete("/agency/payment/{payment_id}")
def delete_payment(payment_id: int):
    DeleteOne.delete_payment(payment_id)
    return {"message": "Payment deleted successfully"}

@router.delete("/agency/property/{property_id}")
def delete_property(property_id: int):
    DeleteOne.delete_property(property_id)
    return {"message": "Property deleted successfully"}

@router.delete("/agency/rent/{rent_id}")
def delete_rent(rent_id: int):
    DeleteOne.delete_rent(rent_id)
    return {"message": "Rent deleted successfully"}

@router.delete("/agency/repair/{repair_id}")
def delete_repair(repair_id: int):
    DeleteOne.delete_repair(repair_id)
    return {"message": "Repair deleted successfully"}

@router.delete("/agency/review/{review_id}")
def delete_review(review_id: int):
    DeleteOne.delete_review(review_id)
    return {"message": "Review deleted successfully"}

@router.delete("/agency/sale/{sale_id}")
def delete_sale(sale_id: int):
    DeleteOne.delete_sale(sale_id)
    return {"message": "Sale deleted successfully"}

@router.delete("/agency/tel_number/{user_id}/{tel_number}")
def delete_tel_number(user_id: int, tel_number: str):
    DeleteOne.delete_tel_number(user_id, tel_number)
    return {"message": "Telephone number deleted successfully"}

@router.delete("/agency/user/{user_id}")
def delete_user(user_id: int):
    DeleteOne.delete_user(user_id)
    return {"message": "User deleted successfully"}
