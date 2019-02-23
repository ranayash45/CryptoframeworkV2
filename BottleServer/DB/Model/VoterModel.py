from BottleServer.DB.DBRecords import DBRecords


class VoterModel(object):
    def __init__(self):
        self.__db = DBRecords()
        if (self.__db.Execute("Create Table if not exists VoterTbl(VoterId integer primary key autoincrement not null,AdharCard varchar(12),VoterName varchar(100),FingurePrintData varchar(230),VoteStatus integer)")):
            print("Successfully Executed Object")
        else:
            print("Failed to Execute the Object")

    def Authenticate(self,AdharcardNo,FingurePrint):
        record = []
        record = self.__db.Query("select * from VoterTbl where AdharCard ='{}'".format(AdharcardNo))
        return record