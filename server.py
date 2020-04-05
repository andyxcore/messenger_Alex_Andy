from datetime import datetime
import time
from flask import Flask, request

app = Flask(__name__)
messages = [
    {'username': 'Alex', 'time': time.time(), 'text': 'Hello'}
]
"""Add database"""


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
    return {'messages': messages}


@app.route("/send", methods=['POST'])
def send_view():
    """
    Send message
    input:username: str, text: str
    :return:{"ok": True}
    """
    print(request.json)
    username = request.json['username']
    text = request.json['text']
    messages.append({'username': username, 'time': time.time(), 'text': text})
    # TODO: add method for appending to Mongo
    return {'ok': True}

if __name__  == '__main__':
    app.run()
