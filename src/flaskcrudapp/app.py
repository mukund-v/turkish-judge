from flask import Flask, jsonify, redirect, request, render_template, send_from_directory, session, url_for, redirect
from flask_pymongo import PyMongo
from apscheduler.scheduler import Scheduler
from werkzeug.security import generate_password_hash, check_password_hash
from bson.json_util import dumps
from bson.objectid import ObjectId
from time import sleep
from collections import Counter
from utils import *
import os
import pandas as pd
import json
import atexit 



with open('./config.json', 'r') as input:
    config = json.load(input)

ALLOWED_EXTENSIONS = {"csv", "tsv"}
app = Flask(__name__)
app.secret_key="secretkey"
app.config['MONGO_URI']= config["mongo"]
mongo = PyMongo(app)
users_db = mongo.db.users
csvs_db = mongo.db.csvs

cron = Scheduler(daemon=True)
cron.start()

@cron.interval_schedule(hours=1)
def update_HIT_statuses():
    appeals = csvs_db.find({"Status" : "Under review"})
    for appeal in appeals:
        appeal_id = appeal["AppealId"]
        appeal_results = get_results(appeal_id)
        if not appeal_results.empty:
            fair  = appeal_results[appeal_results['judgement']=='fair']['judgement'].count()
            unfair = appeal_results[appeal_results['judgement']=='unfair']['judgement'].count()
            csvs_db.update_one({"AppealId":appeal_id}, {"$inc": {"Fair": int(fair), "Unfair": int(unfair)}})
    csvs_db.update({"Fair": {"$gte":2}}, {"$set": {"Status": "Rejection confirmed"}}) 
    csvs_db.update({"Unfair": {"$gte":2}}, { "$set": {"Status": "Rejection overturned"}})


# Shutdown the cron thread when the web process is stopped
atexit.register(lambda: cron.shutdown(wait=False))


@app.route('/', methods=['GET', 'POST'])
def index():
    if session.get('logged_in'):
        return redirect(url_for('requester'))

    if request.method == 'POST':
        signupsuccess = session['signupsuccess'] if 'signupsuccess' in session else None
        signinerror = session['signinerror'] if 'signinerror' in session else None
        
        appealsuccess = session['appealsuccess'] if 'appealsuccess' in session else None
        appealerror = session['appealerror'] if 'appealerror' in session else None

        emailsuccess = session['emailsuccess'] if 'emailsuccess' in session else None
        
        HITId = session['HITId'] if 'HITId' in session else None
        worker_email = session['WorkerEmail'] if 'WorkerEmail' in session else None

        session.clear()

        return (render_template('index.html',
            signupsuccess=signupsuccess, signinerror=signinerror,
            appealsuccess=appealsuccess, appealerror=appealerror,
            emailsuccess=emailsuccess,
            HITId=HITId, worker_email=worker_email
        ))
    
    else:
        return(render_template('index.html'))
    

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
            session['req_id'] = user['req_id']
            session['username'] = user['name']
            session['logged_in'] = True
            return redirect(url_for('requester'))
        else:
            session['signinerror'] = True
            return (redirect(url_for('index'), code=307))
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
    
    if _name and _email and _password and request.method == 'POST':
        _hashed_password = generate_password_hash(_password)
        id = users_db.insert({"name":_name, "req_id":_reqid, "email":_email, "pwd":_hashed_password, "batches": []})

        session['username'] = _name
        session['req_id'] = _reqid
        session['logged_in'] = True

        resp = jsonify('User added successfully')
        resp.status_code = 200
        return (redirect(url_for('index')))
    
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
        session['appealerror'] = True
        return (redirect(url_for('index'), code=307))
    
    sandbox_link = result['sandboxLink']
    status = result['Status']
    
    try:
        worker_email = result['WorkerEmail'] 
    except:
        worker_email = ''
    
    hit_data = {
        'HITId' : _HIT_id,
        'WorkerId' : _worker_id,
        'sandboxLink' : sandbox_link,
        'WorkerEmail' : worker_email,
        'Status' : status
    }

    session["sandboxLink"] = sandbox_link
    session["WorkerEmail"] = worker_email
    session["WorkerId"] = _worker_id
    session["HITId"] = _HIT_id

    return (render_template('appeal.html', hit_data=hit_data))


'''
Submitting appeal
'''
@app.route('/makeappeal', methods=['POST'])
def make_appeal():

    # TODO: make sure this is called after the '/appeal' route or check that session vars are set

    _form = request.form
    _email = _form["email"] if _form["email"] else session['WorkerEmail']
    _worker_id = session["WorkerId"]
    _HIT_id = session["HITId"]

    hit_data = csvs_db.find_one({"WorkerId":_worker_id, "HITId":_HIT_id})

    if hit_data["Status"] == "NA":
        _explanation = _form["explanation"]
        appeal_id = create_appeal(sandbox_link=session["sandboxLink"], explanation=_explanation)

        csvs_db.update_one(
            {
                "WorkerId" : _worker_id,
                "HITId" : _HIT_id
            }, 
            {
                "$set": {
                    "Status":"Under review",
                    "AppealId":appeal_id, 
                    "WorkerEmail":_email,
                    "Explanation":_explanation,
                    "Fair": 0,
                    "Unfair": 0
                }
            }
        )

        session['appealsuccess'] = True

        return redirect(url_for('index'), code=307)

    else:
        csvs_db.update_one(
            {
                "WorkerId" : _worker_id,
                "HITId" : _HIT_id
            }, 
            {
                "$set": {
                    "WorkerEmail":_email,
                }
            }
        )

        session['emailsuccess'] = True
        session['WorkerEmail'] = _email

        return redirect(url_for('index'), code=307)


'''
Requester page.
'''
@app.route('/requester')
def requester():
    if session.get('logged_in'):
        requester_info = users_db.find_one({
            "req_id" : session["req_id"]
        })
        return (render_template('requester.html', username=session.get('username'), 
                batch_name_error=request.args.get('batch_name_error'), batches=requester_info['batches']))
    return redirect(url_for('index'))


'''
'''
@app.route('/batch/<batch_name>')
def batch_page(batch_name):
    #TODO case when we don't find HITs
    hits = list(csvs_db.find(
        {
            "req_id" : session["req_id"],
            "batch_name" : batch_name
        }, 
        {   
            "_id" : 1,
            "HITId":1, 
            "Status":1,
            "sandboxLink":1,    # only want these fields from the db
            "Explanation":1,
            "WorkerId":1
        }
    ))
    batch_stats = make_batch_stats(hits)
    if hits:
        return (render_template('batch.html', batch_name=batch_name, hits=hits, batch_stats=batch_stats))

'''
Helper function to make batch stats
Arg: list of HITs in the batch
'''
def make_batch_stats(hits):
    num_appealed = 0    # keep track of how many appealed in Batch
    num_overturned = 0  # how many overturned out of the appeals
    num_confirmed = 0   # how many rejections confirmed out of the appeals
    workers = set()
    appealing_workers = Counter()
    for hit in hits:
        worker = hit["WorkerId"]
        workers.add(worker)
        appealing_workers[worker] += 1
        if hit["Status"] != "NA":
            num_appealed += 1
        if hit["Status"] == "Rejection confirmed":
            num_confirmed += 1
        elif hit["Status"] == "Rejection overturned":
            num_overturned += 1
    return {
        "num_appealed": num_appealed,
        "num_overturned": num_overturned,
        "num_confirmed": num_confirmed,
        "total": len(hits),
        "num_workers": len(workers),

    }

'''
Upload csv data to database.
'''
@app.route("/upload", methods=["POST"])
def upload():
    file = request.files['inputFile']
    filename = file.filename
    batch_name = request.form['batch_name']
    requester_info = users_db.find_one({"req_id":session["req_id"]})
    if csvs_db.find_one({"batch_name":batch_name, "req_id":session["req_id"]}):
        return redirect(url_for('requester', batch_name_error=True))
    
    if '.' in filename and filename.split(".")[-1] in ALLOWED_EXTENSIONS:
        rejected = parse_csv(input=file)

        for reject in rejected:
            reject["req_id"] = requester_info["req_id"]
            reject["batch_name"] = batch_name
            reject["Explanation"] = ""

        csvs_db.insert(rejected)
        users_db.update_one({"req_id":session["req_id"]}, {"$addToSet":{"batches":batch_name}})

        return redirect(url_for('requester'))

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
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.png')


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