from database.dbGet import GetAdvanced, GetAll, GetOne
from database.dbPost import InsertOne



if __name__ == "__main__":
    get = GetAdvanced()
    for output in get.get_possible_property_types():
        print(output)

