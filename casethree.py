import pymongo
from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)
con = pymongo.MongoClient("mongodb+srv://ahmet:*****@flaskmongodb.cespais.mongodb.net/?retryWrites=true&w=majority")
db = con['flaskmongodb']
collection = db['Users']



@app.route('/adduser', methods=['POST','GET'])
def add_user():

    name = request.form.get('name')
    age = request.form.get('age')
    job = request.form.get('job')
    description = request.form.get('description', 'Description')
    user = {
        "Name": "ahmet",
        "Age": 24,
        "Job": "network security",
        "Description": 1
    }
    collection.insert_one(user)

    return {'message': "kullanici basarili bir sekilde eklenmistir."}


@app.route('/25',methods=['GET'])
def get_users_over_25():

    users = collection.find({"Age": {"$gt": 25}})


    user_list = []
    for user in users:
        user.pop('_id')
        user_list.append(user)


    return jsonify(user_list)

@app.route('/',methods=['GET'])
def get_all_users():
    all_users = collection.find()

    users = []
    for i in all_users:
        i.pop('_id')
        users.append(i)

    return jsonify(users)



if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)




