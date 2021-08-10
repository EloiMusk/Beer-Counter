from dbUtil import dbUtil
from dataObjects import user

db = dbUtil('./../db/beerCounter.db')

# db.setup_beerCounter()

user = user("Person1")

# db.user_exists("Person1")
# db.add_user(user)
db.del_user('Person1')

