from dbUtil import dbUtil
from dataObjects import user, log
from datetime import datetime

db = dbUtil('./../db/beerCounter.db')

# db.setup_beerCounter()

user = user("Person1")
log = log(datetime.now().isoformat(), 1, 1)

# db.user_exists("Person1")
# db.add_user(user)
# db.del_user('Person1')
# db.add_log(log)
db.del_log(1)
