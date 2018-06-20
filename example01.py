
from collections import Counter
from jira import JIRA
import jira.client
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

client = MongoClient('localhost',27017)

db = client.app     #database
post = db.posts    #objects in database

jira = JIRA('http://localhost:8080', auth=('Arijit82', 'admin'))

projects = jira.projects()

jra = jira.project('AR123')
print(jra.name)                 # 'JIRA'
print(jra.lead.displayName)
print(projects)


issue_dict = {
    'project': {'key': 'AR123'},
    'summary': 'New issue from jira-python',
    'description': 'Look into this one',
    'issuetype': {'name': 'Task'},
}



# new_issue = jira.create_issue(fields=issue_dict)
# print(new_issue)
#
# issue=Issue.find({'id':'10000'})
# print(issue.add_field_value({'new', '1'}))

# Types = jira.issue_types()
# print(Types)


# createmeta(self, projectKeys=None, projectIds=[], issuetypeIds=None, issuetypeNames=None, expand=None):
_ =jira.createmeta("AR123", "AR123-1")
# print(jira.editmeta("AR123-1"))
#
# print(jira.remote_links("AR123-1"))


# allfields=jira.fields()
# print(allfields)

# new_issue = jira.create_issue(project='AR123', summary='New issue from jira-python',  description='Look into this one', issuetype={'name': 'Task'})

# print(new_issue)

