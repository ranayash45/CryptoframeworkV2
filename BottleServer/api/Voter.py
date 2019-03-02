import hmac
import json

from bottle import request, response, get, post, hook

from BottleServer.DB.Model.VoterModel import VoterModel
from BottleServer.DB.Model.VoteModel import VoteModel



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

@post('/voter/givevote')
def GiveVOte():
    response.headers['Content-Type']='application/json'
    response.headers['Cache-Control']='no-cache'
    try:
        data = request.json
        vote = bytes(str(data['vote']),'utf-8')
        voterid = data['voterid']
        key = bytes("5675",'utf-8')
        my_hmac = hmac.new(vote,key)

        my_digest = data['digest_value']
        new_digest = my_hmac.hexdigest()
        if my_digest == new_digest :
            objVote = VoteModel()
            objVote.GiveVote(data['vote'],voterid)
    except Exception as e:
        print(e)
        print("")