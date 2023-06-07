import pymongo
from pymongo import MongoClient

con = pymongo.MongoClient("mongodb+srv://ahmet:*****@flaskmongodb.cespais.mongodb.net/?retryWrites=true&w=majority")
db = con['flaskmongodb']
collection = db['Users']

#users_data=collection.find()
#for i in users_data:
# print(i)

#ismi_ahmet = collection.find({'Name': 'ahmet'})
#for i in result:
#print(i)

#yirmiden_fazla = collection.find({'Age':{'$gt':20}})
#for i in yirmiden_fazla:
#print(i)

#yirmibesten_fazla = collection.update_many(
   # {'Age': {'$gt' : 25}},
    # {'$set':{'Description' : '0'}}
#)

#yirmibesten_fazlas = collection.find({'Age' : {'$gt' : 25}})
#for i in yirmibesten_fazlas:
   # print(i)

#kirkbes_kirksekiz = collection.delete_many({'Age': {'$gt': 45, '$lt': 48}})

#kirkbes_kirksekizs = collection.find({'Age': {'$gt': 45, '$lt': 48}})
#for i in kirkbes_kirksekizs:
 #   print(i)

