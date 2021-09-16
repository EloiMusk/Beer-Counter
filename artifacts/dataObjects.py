
class user:
    
    def __init__(self, name=None, avatar='', uid=None, password=None, role=2):
        if not name == None and not avatar == '' and not uid == None and not password == None and not role == None:
            self.name = name
            self.avatar = avatar
            self.uid = uid
            self.password = password
            self.role = role

        else:
            if name == None:
                ValueError(name)

            if avatar == '':
                ValueError(avatar)

            if uid == None:
                ValueError(uid)

            if password == None:
                ValueError(password)

            if role == None:
                ValueError(role)

class beverage:
    
    def __init__(self, name=None, alc=None, price=None):
        self.name = name
        self.alc = alc
        self.price = price

class log:
    
    def __init__(self, timestamp=None, person_id=None, beverage_id=None):
        self.timestamp = timestamp
        self.person_id = person_id
        self.beverage_id = beverage_id

"""
class nfcTag:
    def __init__(self, uid=None, person_id=None):
        if not uid == None and not person_id = None:
            self.uid = uid
            self.person_id = person_id

        else:
            if uid == None:
                ValueError(uid)

            if person_id == None:
                ValueError(person_id)
"""