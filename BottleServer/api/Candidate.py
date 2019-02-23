import json

from bottle import response,request
from bottle import post,get,put,delete

from BottleServer.DB.Model import CandidateModel


@get('/candidate')
def listing_handler():
    obj = CandidateModel.CandidatteModel()
    candidates = obj.GetList()
    if candidates != False :
        response.headers['Content-Type'] = 'application/json'
        response.headers['Cache-Control'] = 'no-cache'
        return json.dumps({'candidates':candidates})
    else:
        return json.dumps({'error':'Something Went Wrong'})
