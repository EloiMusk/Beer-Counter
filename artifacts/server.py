import flask
from nfcUtil import nfcUtil
from dbUtil import dbUtil

db = dbUtil('./../db/beerCounter.db')
nfc = nfcUtil()
app = flask.Flask(__name__)
app.config["DEBUG"] = 1


@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to the beer-counter api.</h1> <p>I wonder how u got here...</p>"


@app.route('/get_uid', methods=['GET'])
def get_uid():
    uid = nfc.get_uid()
    print(uid)
    return uid

@app.route('/set_display', methods=['POST'])
def set_display(text):
    state = False
    #TODO Set display to text and set state true if succeeded
    return state

@app.route('/create_user', methods=['POST'])
def create_user(json):
    #TODO: Create User
    return True

@app.route('/add_log', method=['POST'])
def add_log(json):
    #TODO: Add Log
    return True

@app.route('/add_beverage', method=['POST'])
def add_beverage(json):
    #TODO: Add Beverage
    return True



app.run()
