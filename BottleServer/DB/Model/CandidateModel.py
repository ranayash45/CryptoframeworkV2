from BottleServer.DB.DBRecords import DBRecords


class CandidatteModel(object):
    def __init__(self):
        self.__db = DBRecords()
        if(self.__db.Execute("Create Table if not exists CandidateTbl(CandidateId Integer primary key autoincrement not null,CandidateName varchar(100),PartyName varchar(100))")):
            print("Successfully Executed Object")
        else:
            print("Failed to Execute the Object")
    def GetList(self):
        records = []
        records = self.__db.QueryAll("Select * from CandidateTbl")

        return records

    def GetPartyList(self):
        records = []
        records = self.__db.QueryAll("Select PartyName from CandidateTbl")
        return records