from ApiCalls.Api import Api


class Candidate(object):
    apiName = "/candidate"
    def __init__(self):
        self.api = Api()

    def GetList(self,successfunction,errorfunction=None,failfunction=None):
        self.api.apiCallWithResult(self.apiName,successfunction,errorfunction,failfunction)
