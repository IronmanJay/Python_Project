from pymongo import MongoClient

client = MongoClient()
collection = client["test"]["test03"]

data_list = [{"_id":i,"name":"py{}".format(i)} for i in range(1000)]
collection.insert_many(data_list)

ret = collection.find()
data_list = list(ret)
data_list = [i for i in data_list if i["_id"]%100 == 0 and i["_id"]!=0]
print(data_list)
