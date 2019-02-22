import sqlite3

from CryptoUi.CryptoFramework.DBRecords import DBRecords


class Authentication(object):
    tbl_name="VoterTbl"
    def __init__(self,ClearDb=False):
        self.Db = DBRecords(ClearDb)

    def CheckUser(self,adharNo,FingurePrint):
     #   print("select * from {} where adhar_no='{}'".format(self.tbl_name,adharNo))
        Data = self.Db.Query("select * from {} where adhar_no='{}'".format(self.tbl_name,adharNo))
        return Data
