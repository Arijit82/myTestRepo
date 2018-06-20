import requests
from jira.client import JIRA

def uploadAttachment(issueId , fileLocation):

    url= "http://localhost:8080/rest/api/2/issue/"+issueId+"/attachments"

    headers = {"X-Atlassian-Token": "nocheck"}
    jira = JIRA('http://localhost:8080', auth=('Arijit82', 'admin'))
    issue = jira.issue('TRAZ-116')
    files = {'file': open(fileLocation, 'rb')}
    r = requests.post(url, auth=('Arijit82', 'admin'), files=files, headers=headers)

    print('Upload Logs', r.text)
    if (r.status_code==200):
        return True
    else:
        return False


done = uploadAttachment('TRAZ-116', './uploads/1529061942_flower.jpg')
print('IsItUplaoded ->', done)
