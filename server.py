from flask import Flask, request
import json
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
CORS(app)


@app.route('/auth/sUp', methods=['GET', 'POST', 'OPTIONS'])
def login():
    response = app.response_class(
        response=json.dumps({"id":"839",
                            "username":"walid",
                             "email":"walid.ben.chikha01@gmail.com"}),
        status=200,
        mimetype='application/json'
    )

    return response

@app.route('/auth/logIn', methods=['GET', 'POST', 'OPTIONS'])
def login():
    response = app.response_class(
        response=json.dumps({"data":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ0b3B0YWwuY29tIiwiZXhwIjoxNDI2NDIwODAwLCJodHRwOi8vdG9wdGFsLmNvbS9qd3RfY2xhaW1zL2lzX2FkbWluIjp0cnVlLCJjb21wYW55IjoiVG9wdGFsIiwiYXdlc29tZSI6dHJ1ZX0.yRQYnWzskCZUxPwaQupWkiUzKELZ49eM7oWxAQK_ZXw"}),
        status=200,
        mimetype='application/json'
    )

    return response

@app.route('/api/user', methods=['GET', 'POST', 'OPTIONS'])
def getCurrentUser():
    response = app.response_class(
        response=json.dumps({"id":"839",
                            "username":"walid",
                             "email":"walid.ben.chikha01@gmail.com"}),
        status=201,
        mimetype='application/json'
    )

    return response

@app.route('/user/surveys', methods=['GET', 'OPTIONS'])
def getUserSurveys():
    response = app.response_class(
        response=json.dumps([{"id":"860","title":"Another Survey","sub_title":None,"questions":[],"publish_results":False,"receive_results":False,"user":{"id":"839","username":"walid","email":"walid.ben.chikha01@gmail.com"}},{"id":"868","title":"Title of the survey","sub_title":None,"questions":[],"publish_results":False,"receive_results":False,"user":{"id":"839","username":"walid","email":"walid.ben.chikha01@gmail.com"}},{"id":"869","title":"Title of the survey","sub_title":None,"questions":[],"publish_results":False,"receive_results":False,"user":{"id":"839","username":"walid","email":"walid.ben.chikha01@gmail.com"}},{"id":"872","title":"New Title","sub_title":None,"questions":[{"_id":"cjsz6y89e0000325lmz881m60","type":"SINGLE_LINE_TEXT","title":"Untitled","placeholder":""},{"_id":"cjsz6yc5y0001325l4qiwpmzw","type":"MULTI_CHOICE","title":"Question text ?","options":[{"content":"First choice","_id":"cjsz6yc5z0002325lp6w655m7"},{"content":"Second choice","_id":"cjsz6yc5z0003325lzy6pk00w"},{"content":"Third choice","_id":"cjsz6yc5z0004325l37sbasmu"},{"content":"Fourth choice","_id":"cjsz6yxeo0005325l94m0t6jy"}]},{"_id":"cjsz71soh0006325lx7imk81x","type":"MULTI_CHOICE","title":"Select a choice","options":[{"content":"First choice","_id":"cjsz71soh0007325l6j92oty3"},{"content":"Second choice","_id":"cjsz71soh0008325l6hv032xc"},{"content":"Third choice","_id":"cjsz71soh0009325lgw2eeorz"}]}],"publish_results":False,"receive_results":False,"user":{"id":"839","username":"walid","email":"walid.ben.chikha01@gmail.com"}},{"id":"858","title":"Survey","sub_title":None,"questions":[{"_id":"cjstkgvq800042c5v5qo2bcan","type":"MULTI_CHOICE","title":"Best Player","options":[{"content":"Ronaldo","_id":"cjstkgvq800052c5vt590qmpe"},{"content":"Messi","_id":"cjstkgvq800062c5vs4infuoc"},{"content":"Neymar","_id":"cjstkgvq800072c5vob498um6"}]},{"_id":"cjsz77ygu0000325l0aqirgst","type":"SINGLE_LINE_TEXT","title":"Untitled","placeholder":""}],"publish_results":False,"receive_results":False,"user":{"id":"839","username":"walid","email":"walid.ben.chikha01@gmail.com"}}]),
        status=201,
        mimetype='application/json'
    )

    return response

@app.route('/user/surveys', methods=['POST', 'OPTIONS'])
def createSurvey():
    response = app.response_class(
        response=json.dumps({"id":"875","title":"Title of the survey","sub_title":None,"questions":[],"publish_results":False,"receive_results":False,"user":{"id":"839","username":"walid","email":"walid.ben.chikha01@gmail.com"}}),
        status=201,
        mimetype='application/json'
    )

    return response

@app.route('/surveys/875', methods=['PUT', 'OPTIONS'])
def updateSurvey():
    response = app.response_class(
        response=json.dumps({"id":"875","title":"Title of the survey","sub_title":None,"questions":[],"publish_results":False,"receive_results":False,"user":{"id":"839","username":"walid","email":"walid.ben.chikha01@gmail.com"}}),
        status=201,
        mimetype='application/json'
    )

    return response

@app.route('/surveys/875', methods=['GET', 'OPTIONS'])
def getSurvey():
    response = app.response_class(
        response=json.dumps({"id":"875","title":"Survey","sub_title":None,"questions":[{"_id":"cjstkgvq800042c5v5qo2bcan","type":"MULTI_CHOICE","title":"Best Player","options":[{"content":"Ronaldo","_id":"cjstkgvq800052c5vt590qmpe"},{"content":"Messi","_id":"cjstkgvq800062c5vs4infuoc"},{"content":"Neymar","_id":"cjstkgvq800072c5vob498um6"}]},{"_id":"cjsz77ygu0000325l0aqirgst","type":"SINGLE_LINE_TEXT","title":"Untitled","placeholder":""}],"publish_results":False,"receive_results":False,"user":{"id":"839","username":"walid","email":"walid.ben.chikha01@gmail.com"}}),
        status=201,
        mimetype='application/json'
    )

    return response

@app.route('/surveys/875/results', methods=['GET', 'OPTIONS'])
def getResults():
    response = app.response_class(
        response=json.dumps([{"id":571,"result":{"cjstkgvq800042c5v5qo2bcan":"cjstkgvq800052c5vt590qmpe"}}]),
        status=201,
        mimetype='application/json'
    )

    return response

@app.route('/surveys/875/results', methods=['POST', 'OPTIONS'])
def getResults():
    response = app.response_class(
        response=json.dumps([{"id":571,"result":{"cjstkgvq800042c5v5qo2bcan":"cjstkgvq800052c5vt590qmpe"}}]),
        status=201,
        mimetype='application/json'
    )

    return response

def main():
    app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    main()