from flask import Flask
import json
from flask import jsonify
from flask import request
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient('localhost')

db = client.app
user = db.users

@app.route('/',methods=['GET'])
def get():
    return '<h1><ul><li>/api/v1/users:<br>GET to read all data</li><li>/api/v1/user:<br>POST,PUT to insert or update</li>' \
      '<li>/api/v1/deleteuser/"uid":<br>POST to delete</li><li>/api/v1/user/"uid":<br>GET to return user data</li></h1>'


@app.route('/api/v1/users/',methods=['GET'])
def users():
    users = list()
    if db.users.count() > 0:
        for user in db.users.find({}, {"_id": 0}):
            users.append(user)
        return jsonify(users)
    else:
        return jsonify([])

@app.route('/api/v1/user/<uid>',methods=['GET'])
def userdetails(uid):
    try:
        userdet = db.users.find_one({'uid':uid}, {"_id": 0})
        return jsonify(userdet)
    except:
        return "User couldn't be found"



@app.route('/api/v1/user/<uid>/<name>/<email>/<gender>', methods=['POST', 'PUT'])
def update_insert(uid, name, email, gender):
    if request.method == 'PUT':
        db.users.insert_one({
            "uid": uid, "name": name, "email": email, "gender": gender
        })
        return 'insertion sucessful using PUT'
    else:
        if request.method =='POST':
            if db.users.find_one({'uid':uid}, {"_id": 0}):
                return 'id not available'
            else:
                db.users.insert_one({
                    "uid": uid, "name": name, "email": email, "gender": gender
                })
                return 'insertion sucessful using POST'



@app.route('/api/v1/deleteuser/<uid>',methods=['DELETE'])
def delete_user(uid):
    try:
        for user in db.users.find({}, {"_id": 0}):
            db.users.delete_many({"uid": uid })
            return '\nDeletion successful\n'
    except Exception as e:
        return str(e)



if __name__ == '__main__':
 app.run()