import json

from ApiCalls.Api import Api


class Admin(object):
    apiName = "/Admin"
    def __init__(self):
        self.api = Api()

    def AddAdmin(self,username,password,successfunction,errorfunction,failfunction=None):
        data = {'username':username,'password':password}
        data = json.dumps(data)
        self.api.apiCallWithData(self.apiName+'/AddNew',data,successfunction,errorfunction,failfunction)