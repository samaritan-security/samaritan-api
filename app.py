from flask import Flask, render_template, request, make_response, redirect
from pymongo import MongoClient
import json


app = Flask(__name__)
# for local testing use of venv is recommended
client: MongoClient = MongoClient("localhost:27017")
db = client.user

"""
initial endpoint for sample application 
all rendered templates need to be put in a templates folder 
"""
@app.route('/')
def index():
    return render_template("index.html")


"""

"""
@app.route('/user', methods=['POST'])
def survey():
    my_dict = {"foo": "bar"}
    result = db.user.insert_one(my_dict)
    # below is a way to create a response and set a cookie
    resp = make_response()
    # resp.set_cookie('id', str(result.inserted_id))
    return resp


@app.route('/allUsers', methods=['GET'])
def get_surveys():
    entries = []
    cursor = db.user.find({})
    for document in cursor:
        document['_id'] = str(document['_id'])
        entries.append(document)
    return json.dumps(entries)

# needs to be fixed
@app.route('/user/<user_id>', methods=['GET'])
def get_survey(user_id: str):
    entries = []
    cursor = db.survey.find({})
    for document in cursor:
        document['_id'] = str(document['_id'])
        if document['_id'] == user_id:
            entries.append(document)
    return json.dumps(entries)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
