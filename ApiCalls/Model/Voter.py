import json

from ApiCalls.Api import Api


class Voter(object):
    apiName = "/voter"
    def __init__(self):
        self.api = Api()
    def CheckAuthentication(self,adharcard,fingureprint=None,success=None,fail=None,error=None):
        self.data = {"adharcardno":adharcard, "fingureprintdata":fingureprint}
        self.data = json.dumps(self.data)
        self.api.apiCallWithData(self.apiName+'/authenticate',self.data,success,fail,error)

    def GiveVote(self,votedata,voterid,auth_data,digest_value,success=None,fail=None,error=None):
        self.data = {"vote":votedata,"voterid":voterid,"auth_data":auth_data,"digest_value":digest_value}
        self.data = json.dumps(self.data)
        self.api.apiCallWithData(self.apiName+'/givevote',self.data,success,fail,error)