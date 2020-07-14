# Turkish Judge
Implementation of a crowd-based adjudication platform for Amazon Mechanical Turk as a Flask application. This application manages and stores Requester csv uploads and worker grievance submissions in MongoDB.

## Running the application
First create a virtual environment using virtualenv, e.g.:
```
virtualenv venv
```

Then, activate the environment:
```
source venv/bin/activate
```

To install dependencies, run:
```
pip install -r src/flaskcrudapp/requirements.txt
```

To run the flask application on a local server, run:
```
python src/flaskcrudapp/app.py
```
