from flask import Flask
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
    return '<h1><ul><li>/api/v1/users: GET to read all data</li><li>/api/v1/user: POST,PUT to insert or update</li>' \
      '<li>/api/v1/deleteuser: POST to delete</li><li>/api/v1/user/"uid": GET to return user data</li></h1>'


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
        if userdet != None:
            return jsonify(userdet)
        else:
            return "User couldn't be found"
    except:
        return "ERROR"


@app.route('/api/v1/user', methods=['POST', 'PUT'])
def update_insert():
    if request.method == 'PUT':
        data =request.get_json()

        uid=data['uid']
        name=data['name']
        email=data['email']
        gender=data['gender']

        db.users.update_one({"uid": uid},

                            {"$set":
                                {
                                    "name": name,
                                    "email": email,
                                    "gender": gender
                                }, }
                            )
        return jsonify({'result' : 'success using PUT'})
    else:
        if request.method =='POST':
            data = request.get_json()

            uid = 123
            name = data['name']
            email = data['email']
            gender = "male"

            if db.users.find_one({'uid' : uid}) != None:
                return 'id not available'
            else:
                db.users.insert_one({
                    "uid": uid, "name": name, "email": email, "gender": gender
                })
                return jsonify({'result' : 'success using POST'})


@app.route('/api/v1/deleteuser',methods=['POST'])
def delete_user():
    try:
        data = request.get_json()
        uid = data['uid']
        if db.users.find_one({'uid': uid}) == None:
            return 'id not available'
        else:
            db.users.remove({"uid": uid })
            return '\nDeletion successful\n'
    except Exception as e:
        return str(e)



if __name__ == '__main__':
 app.run()