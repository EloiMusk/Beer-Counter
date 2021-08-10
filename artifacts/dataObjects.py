
class user:
    
    def __init__(self, name, avatar='', uid=None, password=None, role=2):
        self.name = name
        self.avatar = avatar
        self.uid = uid
        self.password = password
        self.role = role

class beverage:
    
    def __init__(self, name, alc=None, price=None):
        self.name = name
        self.alc = alc
        self.price = price

class log:
    
    def __init__(self, timestamp, person_id, beverage_id):
        self.timestamp = timestamp
        self.person_id = person_id
        self.beverage_id = beverage_id
        