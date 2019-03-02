import sqlite3

class DBRecords(object):
    def __init__(self,ClearDb=False):
       self.connection = sqlite3.connect('./DB/File/MyDb.db')
       #self.connection = sqlite3.connect('https://sqliteonline.com/#fiddle-5c7a3de7e78a9g7ujsr81dh1')

       self.row_factory = sqlite3.Row
    def Execute(self,query_string):
        try:
            self.connection.execute(query_string)
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def GetCursor(self):
        self.cursor = self.connection.cursor()
        self.command = []

    def AddScript(self,query):
        self.command.append(query)

    def ExecuteTransaction(self):
        query = ";\n".join(map(str,self.command))
        print(query)
        try:
            self.cursor.executescript(query)
            return True
        except Exception as e:
            print(e)
            return  False

    def SaveTransaction(self):
        if self.connection.commit():
            return True
        else:
            return  False

    def Query(self,query_string):
        result = []
        try:
            result = self.connection.execute(query_string)
            result = result.fetchone()
            if result == None :
                result = []
        except Exception as e:
            print(e)
            result = False
        return result

    def QueryAll(self,query_string):
        result = []
        try:
            result = self.connection.execute(query_string)
            result = result.fetchall()
            if result == None :
                result = []
        except Exception as e:
            print(e)
            result = False
        return result
