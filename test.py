from database.dbGet import GetAdvanced



if __name__ == "__main__":
    GetAdvanced = GetAdvanced()
    for user in GetAdvanced.get_property_by_city(city="Bydgoszcz"):
        print(user)