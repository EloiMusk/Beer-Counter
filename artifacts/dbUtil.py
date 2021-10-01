"""
      .....
  ...'     '... 
 '..:.......:..' 
     '.....'     
By Slowloris-coding
"""

from DBManager import dbManager

class personsDB(dbManager):
    def __init__(self, db, table):
        super().__init__(db)
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

        return (bool(super().createTable(self.tableName, headers)))

    def add(self, user):
        return (bool(super().insertInto(self.tableName, [user.name, user.avatar, user.password, user.role])))

    def delete(self, name):
        try:
            super().delete('logs', 'person_id', super().select(self.tableName, 'id', 'name', name))
            super().delete(self.tableName, 'name', name)

            return True

        except Exception:
            return False

    def exists(self, name):
        return (bool(name == super().select(self.tableName, 'name', 'name', name)))

class logsDB(dbManager):
    def __init__(self, db, table):
        super().__init__(db)
        self.tableName = table

    def create(self):
        headers = {
            "id": ['INTEGER', 'PRIMARY', 'KEY'],
            "timestamp": ['text'],
            "person_id": ['integer'],
            "beverage_id": ['integer']
        }

        return (bool(super().createTable(self.tableName, headers)))

    def add(self, log):
        return (bool(super().insertInto(self.tableName, [log.timestamp, log.person_id, log.beverage_id])))

    def delete(self, id):
        return (bool(super().delete(self.tableName, 'id', id)))

class beveragesDB(dbManager):
    def __init__(self, db, table):
        super().__init__(db)
        self.tableName = table

    def create(self):
        headers = {
            "id": ['INTEGER', 'PRIMARY', 'KEY'],
            "name": ['text'],
            "alc": ['real'],
            "price": ['real']
        }

        return (bool(super().createTable(self.tableName, headers)))

    def add(self, beverage):
        return (bool(super().insertInto(self.tableName, [beverage.name, beverage.alc, beverage.price])))

    def delete(self, id):
        return (bool(super().delete(self.tableName, 'id', id)))

    def exists(self, name):
        return (bool(name == super().select(self.tableName, 'name', 'name', name)))

class nfcTagsDB(dbManager):
    def __init__(self, db, table):
        super().__init__(db)
        self.tableName = table

    def create(self):
        headers = {
            "id": ['INTEGER', 'PRIMARY', 'KEY'],
            "uid": ['text'],
            "person_id": ['integer']
        }

        return (bool(super().createTable(self.tableName, headers)))

    def add(self, nfcTag):
        return (bool(super().insertInto(self.tableName, [nfcTag.uid, nfcTag.person_id])))

    def delete(self, id):
        return (bool(super().delete(self.tableName, 'id', id)))

    def exists(self, uid):
        return (bool(uid == super().select(self.tableName, 'uid', 'uid', uid)))


class Database:
    """
    tables-Parameter erwartet eine list().
    Mögliche Listen-Objekte: 'persons', 'logs', 'beverages', 'nfcTags'
    """
    def __init__(self, db, tables):
        if 'persons' in tables:
            self.persons = personsDB(db, 'persons')

        if 'logs' in tables:
            self.logs = logsDB(db, 'logs')

        if 'beverages' in tables:
            self.beverages = beveragesDB(db, 'beverages')

        if 'nfcTags' in tables:
            self.nfcTags = nfcTagsDB(db, 'nfcTags')
