import pymongo
import random
from pymongo import MongoClient

con = pymongo.MongoClient("mongodb+srv://ahmet:*****@flaskmongodb.cespais.mongodb.net/?retryWrites=true&w=majority")
db = con['flaskmongodb']
collection = db['Users']

for _ in range(50):
    name = 'User {}'.format(random.randint(1, 100))
    age = random.randint(0, 50)
    job = random.choice(['Developer', 'Designer', 'Engineer', 'Manager'])
    description = '1'

    user = {
        'Name': name,
        'Age': age,
        'Job': job,
        'Description': description
    }

    collection.insert_one(user)




