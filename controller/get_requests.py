from database.dbGet import GetAll, GetOne, GetAdvanced
from fastapi import APIRouter, Query
from typing import List

router = APIRouter()
GetAll = GetAll()
GetOne = GetOne()
GetAdvanced = GetAdvanced()

@router.get("/agency/property", tags=["GetAll"])
def get_property():
    return GetAll.get_property()

@router.get("/agency/user", tags=["GetAll"])
def get_user():
    return GetAll.get_user()

@router.get("/agency/repair", tags=["GetAll"])
def get_repairs():
    return GetAll.get_repairs()

@router.get("/agency/meeting", tags=["GetAll"])
def get_meeting():
    return GetAll.get_meeting()

@router.get("/agency/sale", tags=["GetAll"])
def get_sales():
    return GetAll.get_sales()

@router.get("/agency/rent", tags=["GetAll"])
def get_rent():
    return GetAll.get_rent()

@router.get("/agency/payment", tags=["GetAll"])
def get_payment():
    return GetAll.get_payment()

@router.get("/agency/tel_number", tags=["GetAll"])
def get_tel_number():
    return GetAll.get_tel_number()

@router.get("/agency/review", tags=["GetAll"])
def get_reviews():
    return GetAll.get_reviews()

@router.get("/agency/agreement", tags=["GetAll"])
def get_agreements():
    return GetAll.get_agreements()

@router.get("/agency/agent", tags=["GetAll"])
def get_agent():
    return GetAll.get_agent()

@router.get("/agency/client", tags=["GetAll"])
def get_client():
    return GetAll.get_client()

@router.get("/agency/manager", tags=["GetAll"])
def get_manager():
    return GetAll.get_manager()

@router.get("/agency/property/{property_id}", tags=["GetOne"])
def get_property_by_id(property_id: int):
    return GetOne.get_property(property_id)

@router.get("/agency/user/{user_id}", tags=["GetOne"])
def get_user_by_id(user_id: int):
    return GetOne.get_user(user_id)

@router.get("/agency/repair/{repair_id}", tags=["GetOne"])
def get_repair_by_id(repair_id: int):
    return GetOne.get_repair(repair_id)

@router.get("/agency/meeting/{meeting_id}", tags=["GetOne"])
def get_meeting_by_id(meeting_id: int):
    return GetOne.get_meeting(meeting_id)

@router.get("/agency/sale/{sale_id}", tags=["GetOne"])
def get_sale_by_id(sale_id: int):
    return GetOne.get_sell(sale_id)

@router.get("/agency/rent/{rent_id}", tags=["GetOne"])
def get_rent_by_id(rent_id: int):
    return GetOne.get_rent(rent_id)

@router.get("/agency/payment/{payment_id}", tags=["GetOne"])
def get_payment_by_id(payment_id: int):
    return GetOne.get_payment(payment_id)

@router.get("/agency/tel_number/{tel_number_id}", tags=["GetOne"])
def get_tel_number_by_id(tel_number_id: int):
    return GetOne.get_tel_number(tel_number_id)

@router.get("/agency/review/{review_id}", tags=["GetOne"])
def get_review_by_id(review_id: int):
    return GetOne.get_review(review_id)

@router.get("/agency/agreement/{agreement_id}", tags=["GetOne"])
def get_agreement_by_id(agreement_id: int):
    return GetOne.get_agreement(agreement_id)

@router.get("/agency/agent/{agent_id}", tags=["GetOne"])
def get_agent_by_id(agent_id: int):
    return GetOne.get_agent(agent_id)

@router.get("/agency/client/{client_id}", tags=["GetOne"])
def get_client_by_id(client_id: int):
    return GetOne.get_client(client_id)

@router.get("/agency/manager/{manager_id}", tags=["GetOne"])
def get_manager_by_id(manager_id: int):
    return GetOne.get_manager(manager_id)

@router.get("/agency/lone_user", tags=["GetAdvanced"])
def get_lone_user():
    return GetAdvanced.get_lone_user()

@router.get("/agency/user_with_role", tags=["GetAdvanced"])
def get_user_with_role():
    return GetAdvanced.get_user_with_role()

@router.get("/agency/property_with_repair_number", tags=["GetAdvanced"])
def get_property_with_repair_number():
    return GetAdvanced.get_property_with_repair_number()

@router.get("/agency/renting_user", tags=["GetAdvanced"])
def get_renting_user():
    return GetAdvanced.get_renting_user()

@router.get("/agency/property_cheaper_than_average", tags=["GetAdvanced"])
def get_property_cheaper_than_average():
    return GetAdvanced.get_property_cheaper_than_average()

@router.get("/agency/property_by_type/{type}", tags=["GetAdvanced"])
def get_property_by_type(type: str):
    return GetAdvanced.get_property_by_type(type)

@router.get("/agency/property_by_city/{city}", tags=["GetAdvanced"])
def get_property_by_city(city: str):
    return GetAdvanced.get_property_by_city(city)

@router.get("/agency/user_from_city/{city}", tags=["GetAdvanced"])
def get_user_from_city(city: str):
    return GetAdvanced.get_user_from_city(city)

@router.get("/agency/property_in_cities", tags=["GetAdvanced"])
def get_property_in_cities(cities: List[str] = Query(...)):

    return GetAdvanced.get_property_in_cities(cities)

@router.get("/agency/property_not_in_cities", tags=["GetAdvanced"])
def get_property_not_in_cities(cities: List[str] = Query(...)):

    return GetAdvanced.get_property_not_in_cities(cities)

@router.get("/agency/user_with_phone_numbers", tags=["GetAdvanced"])
def get_user_with_phone_numbers():
    return GetAdvanced.get_user_with_phone_numbers()

@router.get("/agency/unique_cities_for_property", tags=["GetAdvanced"])
def get_unique_cities_for_property():
    return GetAdvanced.get_unique_cities_for_property()

@router.get("/agency/agent_with_supervisor", tags=["GetAdvanced"])
def get_agent_with_supervisor():
    return GetAdvanced.get_agent_with_supervisor()

@router.get("/agency/property_not_sold_or_rented", tags=["GetAdvanced"])
def get_property_not_sold_or_rented():
    return GetAdvanced.get_property_not_sold_or_rented()

@router.get("/agency/rents_with_money_paid_in_payment", tags=["GetAdvanced"])
def get_rents_with_money_paid_in_payment():
    return GetAdvanced.get_rents_with_money_paid_in_payment()

@router.get("/agency/property_not_s_or_r_cheaper_then/{budget}", tags=["GetAdvanced"])
def get_property_not_s_or_r_cheaper_then(budget: int):
    return GetAdvanced.get_property_not_s_or_r_cheaper_then(budget)

@router.get("/agency/possible_property_types", tags=["GetAdvanced"])
def get_possible_property_types():
    return GetAdvanced.get_possible_property_types()

@router.get("/agency/review_with_client_and_agent", tags=["GetAdvanced"])
def get_review_with_client_and_agent():
    return GetAdvanced.get_review_with_client_and_agent()


@router.get("/agency/repairs_with_property", tags=["GetAdvanced"])
def get_repairs_with_property():
    return GetAdvanced.get_repairs_with_property()


@router.get("/agency/repair_with_property/{repair_id}", tags=["GetAdvanced"])
def get_repair_with_property(repair_id: int):
    return GetAdvanced.get_repair_with_property(repair_id)

@router.get("/agency/sales_with_info", tags=["GetAdvanced"])
def get_sales_with_info():
    return GetAdvanced.get_sales_with_info()


@router.get("/agency/meetings_with_info", tags=["GetAdvanced"])
def get_meetings_with_info():
    return GetAdvanced.get_meetings_with_info()


@router.get("/agency/client/{client_id}/sales", tags=["GetAdvanced"])
def get_client_with_sales(client_id: int):
    return GetAdvanced.get_client_with_sales(client_id)

@router.get("/agency/client/{client_id}/meetings", tags=["GetAdvanced"])
def get_client_with_meetings(client_id: int):
    return GetAdvanced.get_client_with_meetings(client_id)


@router.get("/agency/client/{client_id}/rents", tags=["GetAdvanced"])
def get_client_with_rents(client_id: int):
    return GetAdvanced.get_client_with_rents(client_id)
