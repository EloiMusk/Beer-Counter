from os import stat
from random import random
import flask
# from nfcUtil import nfcUtil
from flask import request, jsonify
import dataObjects
from dbUtil import Database


# nfc = nfcUtil()
db = Database('./../db/beerCounter.db', ['persons', 'logs', 'beverages', 'nfcTags'])

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
    user = dataObjects.user(**request.json)
    try:
        if not db.persons.exists(user.name) and not user.name is None:
            db.persons.add(user)
            state = "True"
            msg = str(f"Successfully created user {user.name}")

        else:
            state = "False"
            msg = str(f"User {user.name} already exists.")
            
    except:
        state = "False"
        msg = "Something went wrong."

    finally:
        return jsonify(state=state, msg=msg)

@app.route('/delete_user', methods=['DELETE'])
def delete_user():
    user = dataObjects.user(**request.json)

    try:
        if db.persons.exists(user.name) and not user.name is None:

            db.persons.delete(user.name)
            state = "True"
            msg = str(f"Successfully removed user {user.name}")

        else:
            state = "False"
            msg = str(f"User {user.name} already not there.")

    except Exception:
        state = "False"
        msg = "Something went wrong."

    finally:
        return jsonify(state=state, msg=msg)

@app.route('/get_user', methods=['GET'])
def get_user():
    return True

@app.route('/add_log', methods=['POST'])
def add_log():
    log = dataObjects.log(**request.json)
    try:
        db.logs.add(log)
        state = "True"
        return jsonify(state=state)
    except:
        state = "False"
        msg = "Something went wrong."
        return jsonify(state=state, msg=msg)

@app.route('/delete_log', methods=['POST'])
def delete_log():
    log = dataObjects.log(**request.json)
    try:
        db.logs.delete(log.id)
        state = "True"
        return jsonify(state=state)
    except:
        state = "False"
        msg = "Something went wrong."
        return jsonify(state=state, msg=msg)

@app.route('/get_log', methods=['GET'])
def get_log():
    return True

@app.route('/get_logs', methods=['GET'])
def get_logs():
    return True

@app.route('/add_beverage', methods=['POST'])
def add_beverage():
    beverage = dataObjects.beverage(**request.json)
    try:
        if not db.beverages.exists(beverage.name) and not beverage.name is None:
            db.beverages.add(beverage)
            state = "True"
            msg = str(f"Successfully added beverage {beverage.name}")

        else:
            state = "False"
            msg = str(f"Beverage {beverage.name} already exists.")
            
    except:
        state = "False"
        msg = "Something went wrong."

    finally:
        return jsonify(state=state, msg=msg)

@app.route('/delete_beverage', methods=['DELETE'])
def delete_beverage():
    beverage = dataObjects.beverage(**request.json)
    try:
        if db.beverages.exists(beverage.name) and not beverage.name is None:
            db.beverages.delete(beverage.name)
            state = "True"
            msg = str(f"Successfully delete beverage {beverage.name}")

        else:
            state = "False"
            msg = str(f"Beverage {beverage.name} already not existent")
            
    except:
        state = "False"
        msg = "Something went wrong."

    finally:
        return jsonify(state=state, msg=msg)

@app.route('/add_nfcTag', methods=['POST'])
def add_nfcTag():
    nfcTag = dataObjects.nfcTag(**request.json)
    try:
        if not db.nfcTags.exists(nfcTag.uid) and not nfcTag.uid is None:
            db.nfcTags.add(nfcTag)
            state = "True"
            msg = str(f"Successfully added nfcTag {nfcTag.uid} for person witdh ID: {nfcTag.person_id}")

        else:
            state = "False"
            msg = str(f"Beverage {nfcTag.uid} already exists.")
            
    except:
        state = "False"
        msg = "Something went wrong."

    finally:
        return jsonify(state=state, msg=msg)

@app.route('/delete_nfcTag', methods=['DELETE'])
def delete_nfcTag():
    nfcTag = dataObjects.nfcTag(**request.json)
    try:
        if db.nfcTags.exists(nfcTag.uid) and not nfcTag.uid is None:
            db.nfcTags.delete(nfcTag.uid)
            state = "True"
            msg = str(f"Successfully delete nfcTag {nfcTag.uid}")

        else:
            state = "False"
            msg = str(f"NFC-Tag {nfcTag.uid} already not existent")
            
    except:
        state = "False"
        msg = "Something went wrong."

    finally:
        return jsonify(state=state, msg=msg)

@app.route('/get_nfcTag', methods=['GET'])
def get_nfcTag():
    return True

app.run()