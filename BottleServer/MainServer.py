import json

import bottle
from bottle import hook,response,get

from CryptoFramework.ShortPailler import PaillerCryptoSystem

_allow_origin = '*'
_allow_methods = 'PUT, GET, POST, DELETE, OPTIONS'
_allow_headers = 'Authorization, Origin, Accept, Content-Type, X-Requested-With'
PObj = PaillerCryptoSystem()

@hook('after_request')
def enable_cors():
    '''Add headers to enable CORS'''

    response.headers['Access-Control-Allow-Origin'] = _allow_origin
    response.headers['Access-Control-Allow-Methods'] = _allow_methods
    response.headers['Access-Control-Allow-Headers'] = _allow_headers

enable_cors()

@get("/GetPublicKey")
def GetPublicKey():
    key = { "N":PObj.N,"G":PObj.G}
    return json.dumps(key)

from api import Candidate
from api import Voter
from api import Result
app = application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(host='localhost',port=80)
