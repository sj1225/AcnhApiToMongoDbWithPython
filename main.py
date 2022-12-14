import pymongo  # Insert pymongo pakage
import settings # Mongo DB Settings

import requests, json   # For Reading JSON File

# ACNH API URL
ACNH_URL = "https://acnhapi.com/v1/"

FISH_LIST_URL = ACNH_URL + "fish/"  # + 1, 2, 3...
SEA_LIST_URL = ACNH_URL + "sea/"    # + 1, 2, 3...
BUG_LIST_URL = ACNH_URL + "bugs/"   # + 1, 2, 3...
FOS_LIST_URL = ACNH_URL + "fossils/"   # + fossilName
VIL_LIST_URL = ACNH_URL + "villagers/"   # + 1, 2, 3...
ART_LIST_URL = ACNH_URL + "art/"            # + 1, 2, 3...
ITEM01_LIST_URL = ACNH_URL + "houseware/"      # + 1, 2, 3...
ITEM02_LIST_URL = ACNH_URL + "wallmounted/"    # + 1, 2, 3...
ITEM03_LIST_URL = ACNH_URL + "misc/"           # + 1, 2, 3...

# Mongo DB Configuration
MONGODB_URL = settings.MONGODB_URL
MONGODB_DBNM = settings.MONGODB_DBNM

client = pymongo.MongoClient(MONGODB_URL)   # Mongo db url
db = client[MONGODB_DBNM]                   # Database name
############################################
######################################################
# Name: convLocation
# Desc: Location Data Convert Function
# Para: Location Data ( Pier, Pond, etc.)
# Return: Location Code ( Pier -> 0, Pond -> 1, etc.)
def convLocation(loca):
    result = ""

    if loca == "Pier":
        result = "0"
    
    elif loca == "Pond":
        result = "1"
    
    elif loca == "River":
        result = "2"
    
    elif loca == "River (Clifftop)":
        result = "3"
    
    elif loca == "River (Mouth)":
        result = "4"
    
    elif loca == "Sea":
        result = "5"
    
    elif loca == "Sea (when raining or snowing)":
        result = "6"

    elif loca == "River (Clifftop) & Pond":
        result = "7"

    else :
        result = loca

    return result

############################################

def main():
    # Json reading test
    #fish_list_json = requests.get(FISH_LIST_URL)
    #fish_list_txt = fish_list_json.text
    #fish_list_data = json.loads(fish_list_txt)

    #print(fish_list_data['oarfish']) # Fish name must be entered to output results (Inefficient)

    db["fish_list"].delete_many({}) # Collection clear

    i = 1
    while 1:
        try:
            fish_list_json = requests.get(FISH_LIST_URL + str(i))
            fish_list_txt = fish_list_json.text
            fish_list_data = json.loads(fish_list_txt)
        
        except:
            print("Exception!!!")
            break

        else :
            print(str(i) + " " + fish_list_data['file-name'])
            db["fish_list"].insert_one({"id":fish_list_data['file-name']
                                    , "name":fish_list_data['name']['name-KRko']
                                    , "location": convLocation(fish_list_data['availability']['location'])
                                        })
            
            i = i + 1


    # Read Mongo DB Data
    #for x in db.fish_list.find() :
    #    print(x)
    #    break

    client.close()

if __name__ == "__main__":
    main()

