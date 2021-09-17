"""
      .....
  ...'     '... 
 '..:.......:..' 
     '.....'     

By Slowloris-coding
"""

from dbManager import dbManager

class personsDB:
    def __init__(self, db, table):
        self.manager = dbManager(db)
        self.tableName = table

    def create(self):
        headers = {
            "id": ['INTEGER', 'PRIMARY', 'KEY', 'AUTOINCREMENT'],
            'name': ['text'],
            'avatar': ['text'],
            'uid': ['text'],
            'password': ['text'],
            'role': ['integer']
        }

        return self.manager.createTable(self.tableName, headers)

    def add(self, user):
        return self.manager.insertInto(self.tableName, (user.name, user.avatar, user.uid, user.password, user.role))

    def delete(self, name):
        try:
            self.manager.delete('logs', 'person_id', self.manager.select(self.tableName, 'id', 'name', name))
            self.manager.delete(self.tableName, 'name', name)

            return True
        except Exception:
            return False

    def exists(self, name):
        if name == self.manager.select(self.tableName, 'name', 'name', name):
            return True
        else:
            return False

class logsDB:
    def __init__(self, db, table):
        self.manager = dbManager(db)
        self.tableName = table

    def create(self):
        headers = {
            "id": ['INTEGER', 'PRIMARY', 'KEY'],
            "timestamp": ['text'],
            "person_id": ['integer'],
            "beverage_id": ['integer']
        }

        return self.manager.createTable(self.tableName, headers)

    def add(self, log):
        return self.manager.insertInto(self.tableName, [log.timestamp, log.person_id, log.beverage_id])

    def delete(self, id):
        return self.manager.delete(self.tableName, 'id', id)

class beveragesDB:
    def __init__(self, db, table):
        self.manager = dbManager(db)
        self.tableName = table

    def create(self):
        headers = {
            "id": ['INTEGER', 'PRIMARY', 'KEY'],
            "name": ['text'],
            "alc": ['real'],
            "price": ['real']
        }

        return self.manager.createTable(self.tableName, headers)

    def add(self, beverage):
        return self.manager.insertInto(self.tableName, [beverage.name, beverage.alc, beverage.price])

    def delete(self, id):
        return self.manager.delete(self.tableName, 'id', id)

    def exists(self, name):
        if name == self.manager.select(self.tableName, 'name', 'name', name):
            return True
        else:
            return False

"""
class nfcTagDB:
    def __init__(self, db, table):
        self.manager = dbManager(db)
        self.tableName = table

    def create(self):
        headers = {
            "id": ['INTEGER', 'PRIMARY', 'KEY'],
            "uid": ['text'],
            "person_id": ['integer']
        }

        return self.manager.createTable(self.tableName, headers)

    def add(self, nfcTag):
        return self.manager.insertInto(self.tableName, [nfcTag.uid, nfcTag.person_id])

    def delete(self, id):
        return self.manager.delete(self.tableName, 'id', id)

    def exists(self, uid):
        if uid == self.manager.select(self.tableName, 'uid', 'uid', uid):
            return True
        else:
            return False
"""