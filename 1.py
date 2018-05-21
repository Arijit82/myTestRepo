from bottle import route, run
from two import alterdata


@route ('/demo', method=['GET'])
def demo():
    str = 'now in demo file'
    return (str)
alterdata(str)

run(host='localhost', port=8080, debug=True, reloader=True)
