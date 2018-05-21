from bottle import route, run, request
import json

people_string='''
    {
    "people":[
        {
            "name": "Arijit",
            "age":"23",
            "gender":"male",
            "email":"arij"
        },
        {
            "name": "Sonakshi",
            "age":"22",
            "gender":"female",
            "email":"sona"
        },
        {
            "name": "Kaushik",
            "age":"24",
            "gender":"male",
            "email":"kaus"
        }
    ]
}
'''
#displaying data
@route ('/display', method=['GET'])
def demo():
    data = json.loads(people_string)
    return (data)


@route ('/edit', method=['GET'])
def edit():
    data = json.loads(people_string)
    for person in data['people']:
        del person['email']

    new_string = json.dumps(data)
    return (new_string)

@route ('/resp', method=['POST'])
def index():
   print(request.json)
   return (request.json)


run(host='localhost', port=8080, debug=True, reloader=True)