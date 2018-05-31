from flask import Flask
from flask import jsonify
from flask import request
import os
import json
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)
app.config['MONGO_URI'] = os.environ.get('DB')

client = MongoClient('localhost')
app.debug = True

db = client.app
@app.route('/',methods=['GET'])
def get():
    query = request.args
    db.heroesdb.find_one({'uid': id})
    data = db.heroesdb.find_one(query)
    return jsonify(data), 200

if __name__ == '__main__':
 app.run()