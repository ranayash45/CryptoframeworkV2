import json

from bottle import request, response, get, post, hook

from BottleServer.DB.Model.VoterModel import VoterModel



@post('/voter/authenticate')
def AuthenticateUser():
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    try:
        data = request.json
        obj = VoterModel()
        record = obj.Authenticate(data['adharcardno'],None)
        if record == None :
            return json.dumps({'person':'Person Not Found'})
        else:
            return json.dumps(record)

    except Exception as e:
        print(e)
        return json.dumps({'error':'Something Went Wrong'})