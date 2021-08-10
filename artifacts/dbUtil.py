import sqlite3


class dbUtil:

    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()

    def setup_beerCounter(self):
        try:
            self.cur.execute('''CREATE TABLE persons
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, avatar text, uid text, password text, role integer)''')
            self.cur.execute('''CREATE TABLE beverages
                            (id INTEGER PRIMARY KEY, name text, alc real, price real)''')
            self.cur.execute('''CREATE TABLE logs
                            (timestamp text, person_id integer, beverage_id integer)''')
            self.con.commit()
        except:
            return False

    def add_user(self, user):
        try:
            self.cur.execute('''INSERT INTO persons VALUES
                             (NULL ,?, ?, ?, ?, ?)''', (user.name, user.avatar, user.uid, user.password, user.role))
            self.con.commit()
        except:
            return False

    def del_user(self, name):
        try:
            self.cur.execute('''select id from persons where name = ?''', [name])
            id = self.cur.fetchone()[0]
            self.cur.execute('''DELETE FROM persons WHERE name = ?''', [name])
            self.cur.execute('''DELETE FROM logs WHERE person_id = ?''', [id])
            self.con.commit()
        except:
            return False
    def user_exists(self, name):
        try:
            self.cur.execute('''select name from persons where name = ?''', [name])
            req = self.cur.fetchone()[0]
            print(req)
            if req == name:
                print(True)
                return True
            else:
                print(False)
                return False
        except:
            return False

