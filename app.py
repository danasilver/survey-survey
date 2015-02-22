from flask import Flask, render_template, request, g
from rq import Queue, use_connection
from dateutil.parser import parse as parsedate
from models import Person, db
import re
import json

DEBUG = True
SECRET_KEY = 'keep this a secret'

app = Flask(__name__)

use_connection()
q = Queue()

@app.before_request
def before_request():
    g.db = db
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/incoming', methods=['POST'])
def incoming_mail():
    q.enqueue(parse_email, request.data)
    return 'OK', 200

def parse_email(data):
    from_email = re.search(r'[\w\.-]+@[\w\.-]+', data.get('from')).group(0)
    headers = json.loads(data.get('message-headers'))

    db.connect()

    person = Person.get(Person.email==from_email)
    person.reply_time = parsedate(headers.get('date'))
    person.response = data.get('body-plain')
    person.save()

    db.close()
