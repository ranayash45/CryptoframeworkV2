import json
from urllib.parse import *

from kivy.network.urlrequest import UrlRequest


class Api(object):

    def __init__(self):
        self.url = "http://localhost"

    def apiCallWithResult(self,apiString,successfunction,errorfunction,failfunction):
        apiUrl = self.url + apiString

        req = UrlRequest(apiUrl,on_success=successfunction,on_error=errorfunction,on_failure=failfunction)

    def apiCallWithData(self,apiString,data:dict,successfunction,errorfunction,failfunction):
        apiUrl = self.url + apiString
        params = data
        #headers = {'Content-Type':'application/json'}
        headers = {'Content-type': 'application/json'}
        req = UrlRequest(apiUrl,on_success=successfunction,on_error=errorfunction,on_failure=failfunction,req_body=params,req_headers=headers,)
