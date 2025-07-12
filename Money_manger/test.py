from datetime import datetime
import pymongo
con = pymongo.MongoClient("mongodb://localhost:27017")
db = con["fainace_manger"]
col = db["tarakonesh"]
year = int(input("Enter the year : "))
year = datetime.fromtimestamp(year)
print(type(year))
data = list(col.find({"date" : {"$gt" : year}}))
print(data)
