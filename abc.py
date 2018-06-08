from flask import Flask, request, json
from flask import jsonify
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
CORS(app)

client = MongoClient('localhost')

db = client.app     #database
post = db.posts   #objects in database


def func(data):
    return 'nsnsd'


@app.route('/')
def index():
    return '<h1>POST DATA</h1>'


@app.route('/api/v1/posts', methods=['POST'])
def posts():
    data = request.json()
    dataDict = json.loads(data)

    return func(data)





if __name__ == '__main__':
    app.run()
    #'0.0.0.0', 80