from flask import Flask, request, session
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
    #validates log in route
    if user.find_one({'username': username}) == None:
        return jsonify({'status' : False,'message' : 'Logged In Failed...!!'})
    else:
        if user.find_one({'pas': pas}) == None:
            return jsonify({'status' : False,'message' : 'Logged In Failed...!!'})
        else:
            return jsonify({'status' : True,'message' : 'Logged In Successfully...!!'})

def getdetails(username):
    #called from dashboard route
    userdet = user.find_one({'username': username}, {"_id": 0})
    if userdet != None:
        return jsonify(userdet)
    else:
        return jsonify({'status' : False, 'message' : 'Details not Found...!!'})


@app.route('/')
def index():
    return '<h1>LOGIN APPLICATION<br>' \
           '<h3><p>' \
           '<ul>' \
           '<li>/api/v1/login-----------------login[POST]</li>' \
           '<li>/api/v1/signup-----------------signup[POST]</li>' \
           '<li>/api/v1/getsession-----------------get session user[GET]</li>' \
           '<li>/api/v1/dropsession-----------------drop session user[GET]</li>' \
           '<li>/api/v1/dashboard-----------------get session user details[POST]</li>' \
           '</ul>' \
           '</p></h3>'

@app.route('/api/v1/login', methods=['POST'])
def login():
    # requested data
    username = request.json['username']
    pas = request.json['pas']
    try:
        return (validate(username, pas))
    except Exception as e:
        return str(e)

@app.route('/api/v1/signup', methods=['POST'])
def signup():
    username = request.json['username']
    pas = request.json['pas']
    email = request.json['email']
    gender = request.json['gender']
    #timestamps
    DOC= datetime.now()
    DOM=DOC
    try:
        if username and pas and email:
            if  user.find_one({'username': username})== None:
                user.insert_one({"username": username ,"pas": pas, "email": email, "gender":gender, "DOC": DOC, "DOM": DOM})
                return jsonify({'status': True, 'message': 'Sign Up Successful...!!'})
            else:
                return jsonify({'status': False, 'message': 'ID already exists...!!'})
        else:
            return jsonify({'status': False, 'message': 'Incorrect Input...!!'})
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
    return jsonify({'status': True, 'message': 'Session Dropped...!!'})

@app.route('/api/v1/dashboard', methods=['POST'])
def dashboard():
    session['user'] = 'sonakshi'
    #if 'user' in session:
        #return session['user']
    #return 'NOT logged in'
    if 'user' in session:
        if user.find_one({'username': session['user']}):
            try:
                details = user.find_one({'username': session['user']}, {"_id": 0})
                status = True
                message = 'User details fetched...!!'
                if details != None:
                    return jsonify({'details': details, 'status':status, 'message':message})
                else:
                    return "User details couldn't be found"
            except Exception as e:
                return str(e)
        return jsonify({'status': False, 'message': 'User not in Database...!!'})
    return jsonify({'status': True, 'message': 'User not in session...!!'})


if __name__ == '__main__':
    app.run('0.0.0.0', 80)
    #'0.0.0.0', 80