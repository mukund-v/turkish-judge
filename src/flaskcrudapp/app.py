from flask import Flask
from flask_pymongo import PyMongo
from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from bson.json_util import dumps
from bson.objectid import ObjectId

config = json.load("./config.json")
app = Flask(__name__)
app.secret_key="secretkey"
app.config['MONGO_URI']= config["mongo"]
mongo = PyMongo(app)
users_db = mongo.db.users
csvs_db = mongo.db.csvs

@app.route('/add', methods=['POST'])
def add_user():
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['pwd']

    if _name and _email and _password and request.method == 'POST':
        _hashed_password = generate_password_hash(_password)
        id = users_db.insert({"name":_name,"email":_email,"pwd":_hashed_password})

        resp = jsonify('User added successfully')
        resp.status_code = 200
        return resp
    
    else:
        return not_found()

@app.route('/signin', methods=['GET'])
def signin():
    _json = request.json
    _name = _json['name']
    _password = _json['pwd']

    if _name and _password:
        user = users_db.find_one({"name": _name})
        if user and check_password_hash(user["pwd"], _password):
            resp = dumps(user)
            return resp
        else: 
            return not_found()
    else:
        return not_found()

@app.route('/users', methods=['GET'])
def users():
    users = users_db.find()
    resp = dumps(users)
    return resp

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not found' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


if __name__=="__main__":
    app.run(debug=True)

