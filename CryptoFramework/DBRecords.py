import sqlite3

class DBRecords(object):
    def __init__(self,ClearDb=False):
        self.connection = sqlite3.connect('MyDb.db')
        try:
            self.connection.execute("create table if not exists VoterTbl(VoterId integer primary key autoincrement,adhar_no varchar(12),Name varchar(50),Description varchar(255))");
            print("Voter Table is accessible")
        except Exception as e:
            print("Failed To Create Table",str(e))

    def ClearEverything(self):
        self.connection.execute("drop table VoterTbl ")

    def Query(self,query_string):
        result = self.connection.execute(query_string)
        result = result.fetchone()
        return result

    def QueryAll(self,query_string):
        result = self.connection.execute(query_string)
        return result.fetchall()
