from bottle import route, run

def alterdata(data):
    data='altered data'
    return data

@route ('/demo2', method=['GET'])
def demo():
    data=0
    return alterdata(data)



