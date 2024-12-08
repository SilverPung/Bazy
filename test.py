from database.dbGet import GetAdvanced, GetAll, GetOne



if __name__ == "__main__":
    get = GetAdvanced()
    for user in get.get_rents_with_money_paid_in_payment():
        print(user)

