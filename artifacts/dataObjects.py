
class user:
    
    def __init__(self, name=None, avatar='', password=None, role=2):
        if not name == None and not avatar == '' and not password == None and not role == None:
            self.name = name
            self.avatar = avatar
            #self.uid = uid
            self.password = password
            self.role = role

        else:
            ErrorParameter = []
            ErrorString = "Initialisieren der Klasse 'user' nicht möglich ->"

            if name == None:
                ErrorParameter += ['name']

            if avatar == '':
                ErrorParameter += ['avatar']

            """
            if uid == None:
                ErrorParameter += ['uid']
            """

            if password == None:
               ErrorParameter += ['uid']

            if role == None:
                ErrorParameter += ['role']

            ErrorString += ErrorParameter[0]

            if not len(ErrorParameter) == 1:
                for EP in ErrorParameter:
                    ErrorString += str(',{}'.format(EP))
                
            ErrorString += "-parameter = None !"

            raise Exception(ErrorString)

class beverage:
    
    def __init__(self, name=None, alc=None, price=None):
        if not name == None and not alc == None and not price == None:
            self.name = name
            self.alc = alc
            self.price = price

        else:
            ErrorParameter = []
            ErrorString = "Initialisieren der Klasse 'beverage' nicht möglich ->"

            if name == None:
                ErrorParameter += ['name']

            if alc == None:
                ErrorParameter += ['alc']

            if price == None:
                ErrorParameter += ['price']

            ErrorString += ErrorParameter[0]

            if not len(ErrorParameter) == 1:
                for EP in ErrorParameter:
                    ErrorString += str(',{}'.format(EP))
                
            ErrorString += "-parameter = None !"
            
            raise Exception(ErrorString)

class log:
    
    def __init__(self, timestamp=None, person_id=None, beverage_id=None):
        if not timestamp == None and not person_id == None and not beverage_id == None:
            self.timestamp = timestamp
            self.person_id = person_id
            self.beverage_id = beverage_id

        else:
            ErrorParameter = []
            ErrorString = "Initialisieren der Klasse 'log' nicht möglich ->"

            if timestamp == None:
                ErrorParameter += ['timestamp']

            if person_id == None:
                ErrorParameter += ['person_id']

            if beverage_id == None:
                ErrorParameter += ['beverage_id']

            ErrorString += ErrorParameter[0]

            if not len(ErrorParameter) == 1:
                for EP in ErrorParameter:
                    ErrorString += str(',{}'.format(EP))
                
            ErrorString += "-parameter = None !"
            
            raise Exception(ErrorString)


class nfcTag:
    def __init__(self, uid=None, person_id=None):
        if not uid == None and not person_id == None:
            self.uid = uid
            self.person_id = person_id

        else:
            ErrorParameter = []
            ErrorString = "Initialisieren der Klasse 'nfcTag' nicht möglich ->"

            if uid == None:
                ErrorParameter += ['uid']

            if person_id == None:
                ErrorParameter += ['person_id']

            ErrorString += ErrorParameter[0]

            if not len(ErrorParameter) == 1:
                for EP in ErrorParameter:
                    ErrorString += str(',{}'.format(EP))
                
            ErrorString += "-parameter = None !"
            
            raise Exception(ErrorString)
