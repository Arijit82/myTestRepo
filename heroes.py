from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS

from pymongo import MongoClient
app = Flask(__name__)
CORS(app)


client = MongoClient('localhost', 5000)
app.debug = True



db = client.app

heroesdb=[
 {
 'id':'01',
 'name':'Wonder Woman',
 },
 {
 'id':'02',
 'name':'Catwoman',
 },
 {
  'id': '03',
  'name': 'Captain Marvel',
 }
 ]
@app.route('/',methods=['GET'])
def get():
    return jsonify(heroesdb)
    # return jsonify({'heroes':heroesdb})


@app.route('/update/<heroId>',methods=['GET','PUT'])
def gethero(heroId):
    if request.method == 'PUT':
        return (request.method)
    else:

        hero = [ heroes for heroes in heroesdb if (heroes['id'] == heroId) ]
        return jsonify(hero)


@app.route('/insert/<id>/<name>',methods=['POST'])

def insert_data(id=None, name=None):
	if id != None and name != None:
		db.users.insert_one({
			"id": id,
			"name": name
		})
		return 'Data inserted successfully: ' +  id + ', ' \
		+ name
	else:
		return 'Data insufficient. Please try again!'


@app.route('/delete/<empId>',methods=['DELETE'])
def deletehero(heroId):
    hero = [hero for hero in heroesdb if (heroesdb['id'] == heroId)]
    if len(hero) == 0:
      return ("error")
    heroesdb.remove(hero[0])
    return jsonify({'response':'Success'})


if __name__ == '__main__':
 app.run("0.0.0.0", 80)