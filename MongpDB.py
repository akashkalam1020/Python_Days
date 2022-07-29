import pymongo

client = pymongo.MongoClient("mongodb+srv://akashkalam1020:Athens4797@cluster0.6klo4.mongodb.net/?retryWrites=true&w=majority")
db = client.test

d = {
    'name':'Akash',
    'surname':'Kalam',
    'email':'akashkalam1020@gmail.com'
}

db1 = client['Database1']
coll = db1['collection1']
coll.insert_one(d)

for data in coll.find():
    print(data)
    print()