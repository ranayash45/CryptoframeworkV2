import json

from bottle import get,request,response

from BottleServer.DB.Model.CandidateModel import CandidatteModel
from BottleServer.DB.Model.VoteModel import VoteModel
from BottleServer.MainServer import PObj

@get("/result/GetResult")
def GetResult():

    R = VoteModel()
    data = R.GetVoteList()
    print(data[0])
    temp = [ int(value) for value in data[0]]
    for item in range(1,len(data)):
        I1 = int(data[item][1])
        I2 = int(data[item][2])
        I3 = int(data[item][3])
        temp[1] = PObj.Sum(temp[1],I1)
        temp[2] = PObj.Sum(temp[2],I2)
        temp[3] = PObj.Sum(temp[3],I3)
    temp[1] = PObj.Decryption(temp[1])
    temp[2] = PObj.Decryption(temp[2])
    temp[3] = PObj.Decryption(temp[3])
    print(temp)
    V = CandidatteModel()
    candidateList = V.GetPartyList()
    result = {"message":"Successfully Voted"}
    for i in range(0,len(candidateList)):
        result[str(candidateList[i][0])] = temp[i+1]
    result = json.dumps(result)
    return result