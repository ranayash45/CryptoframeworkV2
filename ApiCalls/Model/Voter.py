from ApiCalls.Api import Api


class Voter(object):
    apiName = "/voter"
    def __init__(self):
        self.api = Api()
    def CheckAuthentication(self,adharcard,fingureprint=None,success=None,fail=None,error=None):
        self.data = {"adharcardno":adharcard, "fingureprintdata":fingureprint}
        self.api.apiCallWithData(self.apiName+'/authenticate',self.data,success,fail,error)