from database.dbGet import GetAdvanced, GetAll, GetOne
from database.dbPost import InsertOne



if __name__ == "__main__":
    get = GetAdvanced()
    for output in get.get_review_with_client_and_agent():
        print(output)

