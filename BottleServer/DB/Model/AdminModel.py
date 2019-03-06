from BottleServer.DB.DBRecords import DBRecords


class AdminModel(object):

    def __init__(self):
        super(AdminModel, self).__init__()
        self.con = DBRecords()
        if self.con.Execute("Create table if not exists AdminTbl(AdminId integer primary key autoincrement not null,Username varchar(255) not null,password varchar(255) not null)"):
            print("Admin Table Created")
        else:
            print("Not Created Admin Table")

    def Login(self,username,password):
        result = self.con.Query("select * from AdminTbl where username = '{}' and password = '{}'".format(username,password))
        return result

    def AddAdmin(self,username,password):
        result = self.con.Execute("Insert into AdminTbl values(null,{},{})".format(username,password))
        return result

    def AddCandidate(self,CandidateName,PartyName):
        pass
    def UpdateCandidate(self,CandidateId,CandidateName,PartyName):
        pass

    def UpdateVoter(self,VoterId,AdharCard,FingurePrintData,VoterName):
        pass

    def AddVoter(self,AdharCard,VoterName,FingurePrintData):
        pass

