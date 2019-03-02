from ApiCalls.Api import Api


class PublicKey(object):
    apiName = "/GetPublicKey"
    def __init__(self):
        self.api = Api()
    def GetKey(self,successfunction,errorfunction):
        self.api.apiCallWithResult(self.apiName,successfunction,errorfunction)
