from flask import Flask, jsonify, request, render_template, session
from flask_pymongo import PyMongo
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
from bson.json_util import dumps
from bson.objectid import ObjectId
from utils import *
import pandas as pd
import json

with open('./config.json', 'r') as input:
    config = json.load(input)

ALLOWED_EXTENSIONS = {"csv", "tsv"}
app = Flask(__name__)
# Bootstrap(app)
app.secret_key="secretkey"
app.config['MONGO_URI']= config["mongo"]
mongo = PyMongo(app)
users_db = mongo.db.users
csvs_db = mongo.db.csvs


@app.route('/')
def index():
    if 'username' in session:
        print('you are logged in as: {}'.format(session['username']))
    return (render_template('index.html'))


@app.route('/signin', methods=['POST'])
def signin():
    _form = request.form
    _email = _form['email']
    _password = _form['pwd']

    if _email and _password:
        user = users_db.find_one({"email": _email})
        if user and check_password_hash(user["pwd"], _password):
            session['username'] = user['name']
            resp = dumps(user)
            return (render_template('requester.html'))
        else: 
            return not_found()
    else:
        return not_found()


@app.route('/signup', methods=['GET'])
def signup():
    return (render_template('signUp.html'))


@app.route('/add', methods=['POST'])
def add_user():
    _form = request.form
    _name = _form['name']
    _email = _form['email']
    _password = _form['pwd']
    _reqid = _form['reqID']

    if users_db.find_one({"email" : _email}):# or users_db.find_one({"reqID" : r})
        return not_found('user with that email already exists!')
    
    if _name and _email and _password and request.method == 'POST':
        _hashed_password = generate_password_hash(_password)
        id = users_db.insert({"name":_name,"email":_email,"pwd":_hashed_password})

        session['username'] = _name

        resp = jsonify('User added successfully')
        resp.status_code = 200
        return render_template('index.html')
    
    else:
        return not_found()


@app.route('/appeal', methods=['POST'])
def appeal():
    return (render_template('appeal.html'))


@app.route('/requester', methods=['POST'])
def requester():
    return (render_template('requester.html'))


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files['inputFile']
    filename = file.filename
    csvs_db.delete_many({})
    if '.' in filename and filename.split(".")[-1] in ALLOWED_EXTENSIONS:
        rejected = parse_csv(input=file)
        csvs_db.insert(rejected)
        resp = jsonify("File upload accepted!")
        resp.status_code = 202  # 202 is that the request has been accepted for processing but not yet completed
        return resp
    else:
        return unsupported_media_type()


@app.route('/users', methods=['GET'])
def users():
    users = users_db.find()
    resp = dumps(users)
    return resp


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not found' + request.url,
        'error message' : error
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

@app.errorhandler(415)
def unsupported_media_type(error=None):
    message = {
        'status': 415,
        'message': 'Unsupported Media Type: {}.\n Files can only be a csv or tsv'.format(request.files['inputFile'].filename)
    }
    resp = jsonify(message)
    resp.status_code = 415
    return resp

if __name__=="__main__":
    app.run(debug=True)

