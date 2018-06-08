from datetime import datetime
import os
from flask import Flask, request, session
from flask import jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app)

client = MongoClient('localhost')

db = client.app     #database
post = db.posts   #objects in database


@app.route('/')
def index():
    return '<h1>DISPLAY POSTS</h1>'


@app.route('/api/v1/getposts', methods=['GET'])
def getpost():
    session['userid'] = 'sonakshi'
    if 'userid' in session:
        POSTS = list()
        if post.count() > 0:
            for _posts in post.find({'userid':session['userid']}, {"_id": 0}):
                POSTS.append(_posts)
            return jsonify(POSTS)
        else:
            return jsonify([])
    return jsonify([])



if __name__ == '__main__':
    app.run('0.0.0.0',80)
    # '0.0.0.0',80