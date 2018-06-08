from flask import Flask, request, json
from flask import jsonify
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
CORS(app)

client = Mong0oClient('localhost')

db = client.app     #database
post = db.posts   #objects in database


def func(dataDict):
    if db.posts.find_one({'user_id': dataDict['user_id']}):
        if post.find_one({'user_id': dataDict['user_id'], 'title': dataDict['title'], 'proj_id': dataDict['proj_id']}):
            try:
                details = post.find_one({'user_id': dataDict['user_id']}, {"_id": 0})
                if details:
                    post.update_one({"user_id": dataDict['user_id']},
                                    {
                                        "$set":
                                            {
                                                "user_id": dataDict.setdefault('user_id', "Not Present"),
                                                "title": dataDict['title'],
                                                "desc": dataDict['desc'],
                                                "post_id": dataDict['post_id'],
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
                    return jsonify({'status': False, 'message': 'Must fill all details....!!'})
            except:
                return jsonify({'status': False, 'message': 'something went wrong......!'})
        else:
            return jsonify({'status': False, 'message': 'must input user ID, title and Project ID..!!'})
    else:
        return jsonify({'status': False, 'message': 'user not in database......!!!'})

@app.route('/')
def index():
    return '<h1>POST DATA</h1>'

def CheckValidRequest( inuputReq, validReq ):
    for vr in validReq:
        if vr not in inuputReq.keys():
            return False
    return True



@app.route('/checkfields',methods=['POST'])
def checkfields():
    _= request.json
    _= dict(_)
    keys = _.keys()
    print( "Log" , "ValidReq", CheckValidRequest( _ , ["key1", "key2"] ) )
    if  not (( "key1" in keys  )  ):
        _["key1"] = "defaultvalue1"
    return jsonify( _ )



@app.route('/api/v1/posts', methods=['POST'])
def posts():
    dataDict = request.json

    try:
        return func(dataDict)
    except Exception as e:
        return str(e)



if __name__ == '__main__':
    app.run()
