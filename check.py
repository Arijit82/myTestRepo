from datetime import datetime
from flask import Flask, request
from flask import jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient('localhost')

db = client.app     #database
post = db.posts   #objects in database


@app.route('/')
def index():
    return '<h1>POST DATA</h1>'

ReqFields =[{"fieldName":"userid","default":"userid"},{"fieldName":"title","default":"title"},{"fieldName":"projid","default":"projid"}]

default_fields = {"desc": " ",
                  "userid": " ",
                  "title": " ",
                  "postid": " ",
                  "image": " ",
                  "video": " ",
                  "reference": " ",
                  "projname": " ",
                  "projid": " ",
                  "author": " ",
                  "visible": " ",
                  "moderated": " ",
                  "coverimg": " ",
                  "dispimg": " ",
                  "type": " ",
                  "subtype": " ",
                  "priority": " "}

def CheckValidRequest( inuputReq, validReq ):

    for _vr in validReq:
        vr = _vr["fieldName"]
        if vr not in inuputReq.keys():
            inuputReq[vr] = _vr["default"]
            return False
    return True


def set_default_val(inputReq, default_fields):

    for _i in default_fields.keys():
        if _i not in inputReq.keys():
            inputReq[_i] =default_fields[_i]
    return  jsonify(inputReq)

@app.route('/api/v1/posts', methods=['POST', 'PUT'])
def posts():
    data= request.json
    datadict= dict(data)
    if request.method == 'PUT':#updation
        try:
            if CheckValidRequest(datadict, ReqFields)==True:
                set_default_val(datadict,default_fields)
                post.update_one({"userid": datadict['userid']},
                                {
                                    "$set":
                                        {
                                            "userid": datadict['userid'],
                                            "title": datadict['title'],
                                            "desc": datadict['desc'],
                                            "postid": datadict['postid'],
                                            "image": datadict['image'],
                                            "video": datadict['video'],
                                            "reference": datadict['reference'],
                                            "projname": datadict['projname'],
                                            "projid": datadict['projid'],
                                            "author": datadict['author'],
                                            "visible": datadict['visible'],
                                            "moderated": datadict['moderated'],
                                            "coverimg": datadict['coverimg'],
                                            "dispimg": datadict['dispimg'],
                                            "type": datadict['type'],
                                            "subtype": datadict['subtype'],
                                            "priority": datadict['priority'],
                                            "DOC": datetime.now(),
                                            "DOM": datetime.now()

                                        },
                                })
                return jsonify({'status': True, 'message': 'post updated using PUT ...!!'})
                # return str(datadict)
            else:
                return jsonify({'status': False, 'message': 'required fields not inserted ...!!'})
        except Exception as e:
            print (e)
            return jsonify({'status': False, 'message': 'SOMETHING WENT WRONG ...!!'})
    else:
        if request.method == 'POST':#insertion
            try:
                if CheckValidRequest(datadict,ReqFields):
                    data = set_default_val(datadict,default_fields)
                    print(data)
                    post.insert_one({"userid": datadict['userid'],
                                     "title": datadict['title'],
                                     "desc": datadict['desc'],
                                     "postid": datadict['postid'],
                                     "image": datadict['image'],
                                     "video": datadict['video'],
                                     "reference": datadict['reference'],
                                     "projname": datadict['projname'],
                                     "projid": datadict['projid'],
                                     "author": datadict['author'],
                                     "visible": datadict['visible'],
                                     "moderated": datadict['moderated'],
                                     "coverimg": datadict['coverimg'],
                                     "dispimg": datadict['dispimg'],
                                     "type": datadict['type'],
                                     "subtype": datadict['subtype'],
                                     "priority": datadict['priority'],
                                     "DOC": datetime.now(),
                                     "DOM": datetime.now()
                                     })
                    return jsonify({'status': True, 'message': 'data inserted using POST ...!!'})
                # return str(datadict)
                else:
                    return jsonify({'status': False, 'message': 'required fields not inserted ...!!'})
            except Exception as e:
                print (e)
                return jsonify({'status': False, 'message': 'SOMETHING WENT WRONG ...!!'})




if __name__ == '__main__':
    app.run()
    # '0.0.0.0',80
