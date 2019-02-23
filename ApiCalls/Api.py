from kivy.network.urlrequest import UrlRequest


class Api(object):

    def __init__(self):
        self.url = "http://localhost"

    def apiCallWithResult(self,apiString,successfunction,errorfunction,failfunction):
        apiUrl = self.url + apiString

        req = UrlRequest(apiUrl,on_success=successfunction,on_error=errorfunction,on_failure=failfunction)
