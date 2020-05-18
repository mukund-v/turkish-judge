from flask import Flask, jsonify, redirect, request, render_template, send_from_directory, session, url_for, redirect
from flask_pymongo import PyMongo
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
from bson.json_util import dumps
from bson.objectid import ObjectId
from utils import *
import os
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
    if session.get('logged_in'):
        return redirect(url_for('requester'))
    return (render_template('index.html', signupsuccess=request.args.get('signupsuccess'),
            appealsuccess=request.args.get('appealsuccess'), appealId=request.args.get('appealId'),
            signinerror=request.args.get('signinerror'), appealerror=request.args.get('appealerror')))

'''
Signin route.
'''
@app.route('/signin', methods=['POST'])
def signin():
    _form = request.form
    _email = _form['email']
    _password = _form['pwd']

    if _email and _password:
        user = users_db.find_one({"email": _email})
        if user and check_password_hash(user["pwd"], _password):
            session['username'] = user['name']
            session['logged_in'] = True
            resp = dumps(user)
            return redirect(url_for('requester'))
        else:
            return (redirect(url_for('index', signinerror=True)))
    else:
        return not_found()


'''
Signout route.
'''
@app.route('/signout', methods=['GET'])
def signout():
    session.clear()
    return redirect(url_for('index'))


'''
Account signup page.
'''
@app.route('/signup', methods=['GET'])
def signup():
    return (render_template('signUp.html', signuperror=request.args.get('signuperror')))


'''
Add a requester as a user in database and redirects to requester page.
'''
@app.route('/add', methods=['POST'])
def add_user():
    _form = request.form

    _name = _form['name']
    _email = _form['email']
    _password = _form['pwd']
    _reqid = _form['reqID']

    if users_db.find_one({"email" : _email}) or users_db.find_one({"reqID" : _reqid}):
        return redirect(url_for('signup', signuperror=True))
        return not_found('user with that email / requester id already exists!')
    
    if _name and _email and _password and request.method == 'POST':
        _hashed_password = generate_password_hash(_password)
        id = users_db.insert({"name":_name, "req_id":_reqid, "email":_email, "pwd":_hashed_password, "hits": []})

        session['username'] = _name

        resp = jsonify('User added successfully')
        resp.status_code = 200
        return (redirect(url_for('index', signupsuccess=True)))
    
    else:
        return not_found()


'''
Looks up appeal info in databse and redirects Turker to appeal page.
'''
@app.route('/appeal', methods=['POST'])
def appeal():
    _form = request.form 
    _worker_id = _form["turkerId"]
    _HIT_id = _form["HITId"]
    result = csvs_db.find_one({"WorkerId":_worker_id, "HITId":_HIT_id})

    if not result:
        return (redirect(url_for('index', appealerror=True)))

    sandbox_link = result["sandboxLink"]
    hit_data = {
        'HITId' : _HIT_id,
        'WorkerId' : _worker_id,
        'sandboxLink' : sandbox_link
    }
    session["sandboxLink"] = sandbox_link
    return (render_template('appeal.html', hit_data=hit_data))


'''
Submitting appeal
'''
@app.route('/makeappeal', methods=['POST'])
def make_appeal():
    _form = request.form 
    _explanation = _form["explanation"]
    hit_id = create_appeal(sandbox_link=session["sandboxLink"], explanation=_explanation)
    csvs_db.update_one({"sandboxLink": session["sandboxLink"]}, {"$set": {"Status":"Appealed", "AppealId":hit_id}})
    return redirect(url_for('index', appealsuccess=True, appealId=hit_id))

'''
Requester page.
'''
@app.route('/requester')
def requester():
    if session.get('logged_in'):
        return (render_template('requester.html', username=session.get('username')))
    return redirect(url_for('index'))

'''
Upload csv data to database.
'''
@app.route("/upload", methods=["POST"])
def upload():
    file = request.files['inputFile']
    filename = file.filename
    csvs_db.delete_many({})
    if '.' in filename and filename.split(".")[-1] in ALLOWED_EXTENSIONS:
        rejected = parse_csv(input=file)
        csvs_db.insert(rejected)
        batch_ids = set()
        for reject in rejected:
            batch_ids.add(reject["HITId"])
        current_hits = users_db.find_one({"name":session["username"]})["hits"]
        current_hits.extend(batch_ids)
        users_db.update_one({"name":session["username"]}, {"$set":{"hits":current_hits}}) 
        resp = jsonify("File upload accepted!")
        resp.status_code = 202  # 202 is that the request has been accepted for processing but not yet completed
        return resp
    else:
        return unsupported_media_type()


'''
Get users of database for testing.
'''
@app.route('/users', methods=['GET'])
def users():
    users = users_db.find()
    resp = dumps(users)
    return resp


'''
Route to get tab icon.
'''
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')


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

