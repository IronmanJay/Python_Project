from pymongo import MongoClient

#实例化client，建立连接
client = MongoClient(host="127.0.0.1",port=27017)
collection = client["test"]["test01"]

#插入一条数据
ret = collection.insert_one({"_id":1010,"name":"xiaofang","age":100})
print(ret)

#插入多条数据
data_list = [{"name":"test{}".format(i)} for i in range(10)]
collection.insert_many(data_list)

#查询一个记录
t = collection.find({"name":"xiaohong"})
print(t)

for i in t:
    print(t)
