from flask import Flask, request, json, session
import os
from flask import jsonify
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app)

client = MongoClient('localhost')


db = client.app     #database
user = db.logindb   #objects in database

def validate(username, pas):
        #validates log in
        if user.find_one({'username': username}) == None:
            return jsonify({'status' : False,'message' : 'Logged In Failed...!!'})
        else:
            if user.find_one({'pas': pas}) == None:
                return jsonify({'status' : False,'message' : 'Logged In Failed...!!'})
            else:
                return jsonify({'status' : True,'message' : 'Logged In Successfully...!!'})
@app.route('/')
def index():
     session['user']='Arijit'
     return '<centre><h1>LOGIN APPLICATION</h1><br>' \
            '<h3><p>you are logged in as </p></h3></centre>'+ session['user']

@app.route('/api/v1/login', methods=['POST'])
def login():
    # requested data
    session['user'] = request.json['username']
    username = request.json['username']
    pas = request.json['pas']
    try:
        return (validate(username, pas))
    except Exception as e:
        return str(e)

@app.route('/api/v1/signup', methods=['POST'])
def signup():
    #requested data
    username= request.json['username']
    pas= request.json['pas']
    email = request.json['email']
    gender= request.json['gender']

    #timestamps
    DOC= datetime.now()
    DOM= datetime.now()

    try:
        if username and pas and email:
            if  user.find_one({'username': username})== None:
                user.insert_one({"username": username ,"pas": pas, "email": email, "gender":gender, "DOC": DOC, "DOM": DOM})
                return jsonify({'status': 'True', 'message': 'Sign Up Successful...!!'})
            else:
                #return  str(datetime.now())
                return jsonify({'status': 'False', 'message': 'ID already exists...!!'})
        else:
            return jsonify({'status': 'False', 'message': 'Incorrect Input...!!'})
    except Exception as e:
        return str(e)


@app.route('/api/v1/getsession')
def getsession():
    if 'user' in session:
        return session['user']
    return 'NOT logged in'

@app.route('/api/v1/dropsession')
def dropsession():
    session.pop('user', None)
    return jsonify({'status': 'True', 'message': 'Session Dropped...!!'})



@app.route('/api/v1/dashboard', methods=['POST'])
def dashboard():
    #     check for user if in session
    #     get details from db
    #     show details if in session
    #     return false if not in session
    if 'user' in session:
        if user.find_one({'username':session['user']}):
            try:
                userdet = user.find_one({'username': session['user']}, {"_id": 0})
                if userdet != None:
                    return jsonify(userdet)
                else:
                    return "User details couldn't be found"
            except Exception as e:
                return str(e)
    else:
        return 'User not in session'

if __name__ == '__main__':
     app.run()
     #'0.0.0.0', 80