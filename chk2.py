from datetime import datetime
import os
from flask import Flask, request, session, render_template
from werkzeug import secure_filename
from flask import jsonify
from flask_cors import CORS
from pymongo import MongoClient

def initializeRoute(app):

    client = MongoClient('localhost')
    db = client.app     #database
    post = db.posts   #objects in database
    ReqFields =[{"fieldName":"userid","default":"sonakshi"},{"fieldName":"title","default":"title"},{"fieldName":"projid","default":"projid"}]
    default_fields = {"desc": " ",
                      "userid": " ",
                      "title": " ",
                      "postid": " ",
                      "image": [" "],
                      "video": [" "],
                      "reference": [" "],
                      "projname": " ",
                      "projid": " ",
                      "author": " ",
                      "visible": " ",
                      "moderated": " ",
                      "coverimg": " ",
                      "dispimg": " ",
                      "type": " ",
                      "subtype": " ",
                      "priority": " ",
                      "pid": "0"}

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
        session['userid'] = 'sonakshi'
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
                                                "userid": session['userid'],
                                                "title": datadict['title'],
                                                "desc": datadict['desc'],
                                                "postid": datadict['postid'],
                                                "images": datadict['images'],
                                                "videos": datadict['videos'],
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
                                                "pid": datadict['pid'],
                                                "jira": False,
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

                        post.insert_one({
                                         "userid":session['userid'],
                                         "title": datadict['title'],
                                         "desc": datadict['desc'],
                                         "postid": datadict['postid'],
                                         "images": datadict['images'],
                                         "videos": datadict['videos'],
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
                                         "pid": datadict['pid'],
                                            "jira":False,
                                         "DOC": datetime.now(),
                                         "DOM": datetime.now()
                                         })
                        return jsonify({'status': True, 'message': 'data inserted using POST ...!!'})
                    # return str(datadict)
                    else:
                        return jsonify({'status': False, 'message': 'required fields not inserted ...!!'})
                except Exception as e:
                    return jsonify({'status': False, 'message': 'SOMETHING WENT WRONG ...!!'})


    @app.route('/api/v1/getposts', methods=['GET','OPTIONS'])
    def get():
        session['userid'] = 'sonakshi'
        if 'userid' in session:
            posts = list()
            if db.posts.count() > 0:
                for _P in db.posts.find({'userid':session['userid']}, {"_id": 0}):
                    posts.append(_P)
                return jsonify(posts)
            else:
                return jsonify([])
        return jsonify({'status': False, 'message': 'user not logged in ...!!'})


    @app.route('/api/v1/get/<pid>', methods=['GET'])
    def getp(pid):
        try:
            session['userid'] = 'sonakshi'
            if 'userid' in session:
                POSTS = list()
                if post.count() > 0:
                    for _posts in post.find({'pid':str(pid),'userid':session['userid']}, {"_id": 0}):
                        POSTS.append(_posts)
                        print(POSTS)
                    return jsonify(POSTS)
                else:
                    return jsonify([])
            return jsonify({'status':False, 'message': 'user not in session'})
        except Exception as e:
            print (e)
            return jsonify({'status':False})






