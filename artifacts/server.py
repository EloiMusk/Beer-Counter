from random import random
import flask
# from nfcUtil import nfcUtil
from flask import request, jsonify
import dataObjects
from dbUtil import dbUtil

db = dbUtil('./../db/beerCounter.db')
# nfc = nfcUtil()
app = flask.Flask(__name__)
app.config["DEBUG"] = 1


@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to the beer-counter api.</h1> <p>I wonder how u got here...</p>"


@app.route('/get_uid', methods=['GET'])
def get_uid():
    # uid = nfc.get_uid()
    uid = int(random()*1000000)
    # print(uid)
    return jsonify(uid)


@app.route('/set_display', methods=['POST'])
def set_display():
    state = "False"
    print(request.json)
    # TODO Set display to text and set state true if succeeded
    return jsonify(request.json)


@app.route('/create_user', methods=['POST'])
def create_user():
    msg = "Something went wrong."
    user = dataObjects.user(**request.json)
    try:
        if not db.user_exists(user.name) and not user.name is None:
            db.add_user(user)
            state = "True"
            return jsonify(state=state)
        else:
            state = "False"
            msg = "User already exists."
            return jsonify(state=state, msg=msg)
    except:
        state = "False"
        return jsonify(state=state, msg=msg)

@app.route('/delete_user', methods=['DELETE'])
def delete_user():
    return True

@app.route('/get_user', methods=['GET'])
def get_user():
    return True

@app.route('/add_log', methods=['POST'])
def add_log():
    msg = "Something went wrong."
    log = dataObjects.log(**request.json)
    try:
        db.add_log(log)
        state = "True"
        return jsonify(state=state)
    except:
        state = "False"
        return jsonify(state=state, msg=msg)

@app.route('/del_log', methods=['POST'])
def del_log():
    return True

@app.route('/get_log', methods=['GET'])
def get_log():
    return True

@app.route('/get_logs', methods=['GET'])
def get_logs():
    return True

@app.route('/add_beverage', methods=['POST'])
def add_beverage():
    msg = "Something went wrong."
    beverage = dataObjects.beverage(**request.json)
    try:
        if not db.beverage_exists(beverage.name) and not beverage.name is None:
            db.add_beverage(beverage)
            state = "True"
            return jsonify(state=state)
        else:
            state = "False"
            msg = "Beverage already exists."
            return jsonify(state=state, msg=msg)
    except:
        state = "False"
        return jsonify(state=state, msg=msg)


app.run()
