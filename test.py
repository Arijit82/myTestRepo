import requests
from jira.client import JIRA
from jira.resources import Issue
from flask import Flask, request, session
import os
from flask import jsonify
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime
from mongo import chk2

app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app)
chk2.initializeRoute(app)


class PostModel():
    def __init__(self, post):
        self.post = post

    def getJson(self):
        id = 0
        p = post['priority']
        if p == "Highest":
            id = "1"
        elif p == "High":
            id = "2"
        elif p == "Medium":
            id = "3"
        elif p == "Low":
            id = "4"
        elif p == "Lowest":
            id = "5"
        else:
            id = "5"

        self.data = {
            "fields": {
                "project":
                    {
                        "key": "TRAZ"
                    },
                "summary": self.post['title'],
                "description": self.post['desc'],
                "issuetype": {
                    "name": "Bug"
                },
                "priority": {"id": id},
                "customfield_10205": self.post['title'],
                "customfield_10207": self.post['userid'],
                "customfield_10208": self.post['postid'],
                "customfield_10210": self.post['projname'],
                "customfield_10211": self.post['projid'],
                "customfield_10212": self.post['author'],
                "customfield_10213": self.post['visible'],
                "customfield_10214": self.post['moderated'],
                "customfield_10215": self.post['type'],
                "customfield_10216": self.post['subtype'],
                "customfield_10217": self.post['pid'],
                "customfield_10218": str(self.post['DOC']),
                "customfield_10219": str(self.post['DOM'])

            }
        }
        return self.data


url = 'http://localhost:8080/rest/api/2/issue/'
jira = JIRA('http://localhost:8080', auth=('Arijit82', 'admin'))
client = MongoClient('localhost', 27017)

db = client.app  # database
post = db.posts  # objects in database

projects = jira.projects()
jira_proj = jira.project('TRAZ')


def insert():
    if post.count() > 0:
        for _posts in post.find({}):
            _id = _posts['_id']
            del _posts['_id']

            data = PostModel(_posts).getJson()
            _ = requests.post(url, json=data, auth=('Arijit82', 'admin'))
            print(_.text)
            post.update_one({'_id': _id}, {"$set": {'jira': True}})
            print(data)


# insert()
#
# print(jira.editmeta("TRAZ-154"))
data2 = {
    "fields": {
        "project":
            {
                "key": "TRAZ"
            },
        "summary": "Arijit's update",
        "description": "description_updated",
        "issuetype": {
            "name": "Bug"
        },
        "priority": {"id": "3"},
        "customfield_10205": "title_updated",
        "customfield_10207": "userid_updated",
        "customfield_10208": "postid_updated",
        "customfield_10210": "projname_updated",
        "customfield_10211": "projid_updated",
        "customfield_10212": "author_updated",
        "customfield_10213": "visible_updated",
        "customfield_10214": "moderated_updated",
        "customfield_10215": "type_updated",
        "customfield_10216": "subtype_updated",
        "customfield_10217": "pid_updated",
        "customfield_10218": "DOC_updated",
        "customfield_10219": "DOM_updated"

    }}


def update():
    try:
        if post.count() > 0:
            for _posts in post.find({}):
                if _posts['key'] == None and _posts['id'] == None:
                    _id = _posts['_id']
                    del _posts['_id']
                    data = PostModel(_posts).getJson()
                    # jira issue insert code
                    _ = requests.post(url, json=data, auth=('Arijit82', 'admin'))
                    post.update_one({'_id': _id}, {"$set": {'jira': True}})
                    return print(_)
                else:  # jira issue update code
                    _id = _posts['_id']
                    _key = _posts['key']
                    del _posts['_id']
                    print(_key)
                    url_1 = url + _key
                    print(url_1)
                    _ = requests.put(url_1, json=data2, auth=('Arijit82', 'admin'))
                    post.update_one({'_id': _id}, {"$set": {'jira': True}})
                    print(_.status_code, _.content)
                    print(_)
        else:
            return print("NO POSTS AVAILABLE")
    except Exception as e:
        return print(e)


update()