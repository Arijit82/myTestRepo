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


# def func(dataDict):

def func(dataDict):
    try:
        if dataDict['user_id'] and dataDict['proj_id'] and dataDict['title'] in dataDict.keys():
            defd=posts.dataDict(lambda :'default value')

            post.update_one({"user_id": dataDict['user_id']},
                            {
                                "$set":
                                    {
                                        "user_id": dataDict['user_id'],
                                        "title": dataDict['title'],
                                        "post_id": dataDict['post_id'],
                                        "desc": dataDict['desc'],
                                        "image": dataDict['image'],
                                        "video": dataDict['video'],
                                        "reference": dataDict['reference'],
                                        "proj_name": dataDict['proj_name'],
                                        "proj_id": dataDict['proj_id'],
                                        "author": dataDict['author'],
                                        "visible": dataDict['visible'],
                                        "moderated": dataDict['moderated'],
                                        "cover_img": dataDict['cover_img'],
                                        "disp_img": dataDict['disp_img'],
                                        "type": dataDict['type'],
                                        "subtype": dataDict['subtype'],
                                        "priority": dataDict['priority'],
                                        "DOC": datetime.now(),
                                        "DOM": datetime.now()
                                    },
                            })
            return jsonify({'status': True, 'message': 'data posted and details posted...!!'})

        else:
            return jsonify({'status': False, 'message': 'User details could not be found..!!'})

    except Exception as e:
        return jsonify({'status': False, 'message': 'please input title and project id........!!'})



@app.route('/')
def index():
    return '<h1>POST DATA</h1>'

@app.route('/api/v1/posts', methods=['POST'])
def posts():
    dataDict = request.json
    CheckValidRequest( dict(dataDict) ,  )
    return func(dataDict)

if __name__ == '__main__':
    app.run()
