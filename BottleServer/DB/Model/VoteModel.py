from BottleServer.DB.DBRecords import DBRecords
from BottleServer.DB.Model.CandidateModel import CandidatteModel


class VoteModel(object):
    def __init__(self):
        self.dbcon = DBRecords()
        self.candidate = CandidatteModel()
        self.fieldstring = ""
        self.candidatelist = self.candidate.GetList()
        for candidate in self.candidatelist:
            self.fieldstring = self.fieldstring+"{} varchar(255),".format(candidate[2])
        self.fieldstring = self.fieldstring.strip(',')
        query = "Create table if not exists VoteTbl(VoteId integer primary key autoincrement not null,{},VoterId Integer Not null,FOREIGN key(VoterId) References VoterTbl(VoterId))".format(self.fieldstring)
        if(self.dbcon.Execute(query)):
            print("Successfully Created Voting Table")
        else:
            print("Failed To Create Table")
    def GiveVote(self,value,voterid):
        self.fieldstring = ""

        for votevalue in value:
            self.fieldstring = self.fieldstring+"{},".format(votevalue)
        self.fieldstring = self.fieldstring.strip(',')
        qurey = "insert into VoteTbl values(null,{},{})".format(self.fieldstring,voterid)
        self.dbcon.GetCursor()
        self.dbcon.AddScript(qurey)
        self.dbcon.AddScript("Update VoterTbl set VoteStatus=1 where VoterId={}".format(voterid))
        if self.dbcon.ExecuteTransaction() == True:
            self.dbcon.SaveTransaction()
            return True
        else:
            self.dbcon.cursor.close()
            return False

    def GetVoteList(self):
        data = self.dbcon.QueryAll("select * from VoteTbl")
        return data