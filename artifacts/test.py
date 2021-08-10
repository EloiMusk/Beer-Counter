from dbUtil import dbUtil
from dataObjects import user

db = dbUtil('./../db/beerCounter.db')

db.setup_beerCounter()

# user = user("Person1")

# db.add_user(user)

