"""
      .....
  ...'     '... 
 '..:.......:..' 
     '.....'     

By Slowloris-coding
"""

import sqlite3
from activityLogger import activityLogger

logger = activityLogger()

"""
Ein "headersDict" sollte folgendermassen aussehen:

{
    "<Header-name>": [<argumente>]
}
"""

class dbManager:
    """
    Class to manage the Data-Base, without hardcoding inputs.
    """
    def __init__(self, db):
        try:
            self.con = sqlite3.connect(db, check_same_thread=False)
            self.cur = self.con.cursor()
        except Exception:
            logger.log_error(str(f'Cannot initialize class "dbManager" of db: {db} !'))

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
            logger.log_failure(str(f'Failed to create Table {tableName} - Error while executing SQL-Command!'))
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
        except Exception:
            self.con.rollback()
            logger.log_failure(str(f'Failed to insert Value: {values} in Table: {tableName}!'))
            return False

    def delete(self, tablename, filterBy, filterCriteria):
        try:
            self.cur.execute('''DELETE FROM {} WHERE {} = ?''',format(tablename, filterBy), [filterCriteria])
            self.con.commit()
            return True
        except Exception:
            self.con.rollback()
            logger.log_failure(str(f'Failed to delete Entry where {filterBy} like {filterCriteria} in table: {tablename}!'))
            return False

    def select(self, tableName, getWhat, filterBy, filterCriteria):
        try:
            self.cur.execute('''select {} from {} where {} = ?'''.format(getWhat, tableName, filterBy), [filterCriteria])
            return self.cur.fetchone()[0]

        except Exception:
            self.con.rollback()
            logger.log_failure(str(f'Failed to get {filterBy} like {filterCriteria} in table: {tableName}!'))
            return None