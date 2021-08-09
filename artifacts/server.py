import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = 1


@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to the beer-counter api.</h1> <p>I wonder how u got here...</p>"


@app.route('/get_uid', methods=['GET'])
def get_uid():
    uid = "Get uid here"
    return uid

@app.route('/set_display', methods=['POST'])
def set_display(text):
    state = False
    # Set display to text and set state true if succeeded
    return state

app.run()
