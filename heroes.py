from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient('localhost')
app.debug = True

db = client.app

@app.route('/',methods=['GET'])
def get():
    HEROES = list()
    for hero in db.heroesdb.find({}, {"_id":0}):
        HEROES.append(hero)
    return jsonify(HEROES)
    # return jsonify({'heroes':heroesdb})


@app.route('/get/<heroId>',methods=['GET'])
def getHero(heroId):

       heroname=db.heroesdb.find();
       print('all data from database')
       HeroName = [heroes for heroes in db.heroesdb if (heroes['id'] == heroId)]
       return jsonify(HeroName)


@app.route('/insert/<heroId>/<name>',methods=['POST'])
def insert_data(heroId=None, name=None):
	if heroId != None and name !=None:
		db.heroesdb.insert_one({
            "id": heroId, "name": name
        })
		return 'Data inserted successfully: ' +  heroId + ', ' \
               + name
	else:
		return 'Data insufficient. Please try again!'


@app.route('/update/<heroId>/<name>',methods=['PUT'])
def update(heroId, name):
        if heroId != None and name != None:
            HeroName = [heroes for heroes in db.heroesdb if (heroes['id'] == heroId)]
            db.heroesdb.update_one({"id": heroId},
                    {"$set":
                        {
                            "name":name
                        },}
                    )
            return ("\nRecords updated successfully\n")

@app.route('/delete/<heroId>',methods=['DELETE'])
def delete_hero(heroId):
    try:
        for hero in db.heroesdb.find({}, {"_id": 0}):
            db.heroesdb.delete_many({"id": heroId })
            return '\nDeletion successful\n'
    except Exception as e:
        return (str(e))

if __name__ == '__main__':
 app.run('0.0.0.0',80)