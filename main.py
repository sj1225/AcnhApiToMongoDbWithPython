import pymongo  # insert pymongo pakage
import settings # Mongo DB Settings

ACNH_URL = "https://acnhapi.com/v1/"

# Mongo DB Configuration
MONGODB_URL = settings.MONGODB_URL
MONGODB_DBNM = settings.MONGODB_DBNM

client = pymongo.MongoClient(MONGODB_URL)   # mongo db url
db = client[MONGODB_DBNM]                   # database name

for x in db.fish_list.find() :
    print(x)
    break

client.close()