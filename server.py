from datetime import datetime
import time
from flask import Flask, request
#from pymongo import MongoClient


app = Flask(__name__)
messages = [
    {'username': 'Alex', 'time': time.time(), 'text': 'Hello'}
]
"""Add database"""

users = {
    "Alex": "12345",
    "Andy": "54321"
}


@app.route("/")
def hello_view():
    return "hello"


@app.route("/status")
def status_view():
    return {
        'status': True,
        'time': datetime.now()
    }


@app.route("/messages")
def messages_view():
    print(request.args)
    after = float(request.args['after'])
    filtered_messages = []
    for message in messages:
        if message['time'] > after:
            filtered_messages.append(message)
    return {'messages': filtered_messages}


@app.route("/send", methods=['POST'])
def send_view():
    """
    Send message
    input:{"username": str, "password":str, "text": str}
    :return:{"ok": True}
    """
    print(request.json)
    username = request.json['username']
    password = request.json['password']
    text = request.json['text']

    if username not in users or users[username] != password:
        return{'ok': False}

    messages.append({'username': username, 'time': time.time(), 'text': text})
    # TODO: add method for appending to Mongo
    return {'ok': True}


@app.route("/login", methods=['POST'])
def login_view():
    """
    Checks if user in users and password is ok
    input:{"username": str, "password":str, "text": str}
    :return:{"ok": True}
    """
    print(request.json)
    username = request.json['username']
    password = request.json['password']
    if username not in users:
        users[username] = password
        return {'ok': True}
    elif users[username] == password:
        return {'ok': True}
    else:
        return {'ok': False}


if __name__  == '__main__':
    app.run()
