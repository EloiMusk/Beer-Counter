"""
      .....
  ...'     '... 
 '..:.......:..' 
     '.....'     

By Slowloris-coding
"""

import sqlite3

"""
Ein "headersDict" sollte folgendermassen aussehen:

{
    "<Header-name>": [<argumente>]
}
"""

class dbManager:
    def __init__(self, db):
        self.con = sqlite3.connect(db, check_same_thread=False)
        self.cur = self.con.cursor()

    def createTable(self, tableName, headersDict):
        argsString = '('

        for header in headersDict.keys():
            argsString += str(f"{header}")

            for argument in headersDict[header]:
                argsString += str(f" {argument}")
            
            argsString += ', '

        argsString = argsString[:-2]
        argsString += ')'

        try:
            self.cur.execute('''CREATE TABLE {} {}'''.format(tableName, argsString))
            self.con.commit()
            return True

        except Exception:
            self.con.rollback()
            return False

    def insertInto(self, tableName, values):
        argsString = '(Null'

        for i in values:
            argsString += ', ?'

        argsString += ')'

        try:
            self.cur.execute('''INSERT INTO {} VALUES {}'''.format(tableName, argsString), values)
            self.con.commit()
            return True
        except:
            self.con.rollback()
            return False

    def delete(self, tablename, filterBy, filterCriteria):
        try:
            self.cur.execute('''DELETE FROM {} WHERE {} = ?''',format(tablename, filterBy), [filterCriteria])
            self.con.commit()
            return True
        except Exception:
            self.con.rollback()
            return False

    def select(self, tableName, getWhat, filterBy, filterCriteria):
        try:
            self.cur.execute('''select {} from {} where {} = ?'''.format(getWhat, tableName, filterBy), [filterCriteria])
            return self.cur.fetchone()[0]

        except Exception:
            self.con.rollback()
            return None