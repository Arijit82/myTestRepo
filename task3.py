from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)
empDB=[
 {
 'id':'101',
 'name':'Arijit',
 'title':'Chandra'
 },
 {
 'id':'201',
 'name':'Sonakshi',
 'title':'Harjai'
 }
 ]
@app.route('/empdb/employee/',methods=['GET'])
def getAllEmp():
    return jsonify({'emps':empDB})


@app.route('/empdb/employee/<empId>',methods=['GET','PUT'])
def getEmp(empId):
    if request.method == 'PUT':
        return (request.method)
    else:
        usr = [ emp for emp in empDB if (emp['id'] == empId) ]
        return jsonify({'emp':usr})


@app.route('/empdb/employee',methods=['POST'])
def createEmp():
    dat = {
    'id':request.json['id'],
    'name':request.json['name'],
    'title':request.json['title']
    }
    empDB.append(dat)
    return jsonify(dat)

@app.route('/empdb/employee/<empId>',methods=['DELETE'])
def deleteEmp(empId):
    em = [ emp for emp in empDB if (emp['id'] == empId) ]
    if len(em) == 0:
       abort(404)
    empDB.remove(em[0])
    return jsonify({'response':'Success'})


if __name__ == '__main__':
 app.run('0.0.0.0', 80)