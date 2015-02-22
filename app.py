from flask import Flask, render_template, request, g
from flask.ext.rqify import init_rqify
from flask.ext.rq import job
from dateutil.parser import parse as parsedate
from models import Person, db
import re
import json

app = Flask(__name__)
init_rqify(app)
app.debug = True

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

@job
def parse_email(data):
    from_email = re.search(r'[\w\.-]+@[\w\.-]+', data.get('from')).group(0)
    headers = json.loads(data.get('message-headers'))

    db.connect()

    print data

    person = Person.get(Person.email==from_email)
    person.reply_time = parsedate(headers.get('date'))
    person.response = data.get('body-plain')
    person.save()

    db.close()

@app.route('/incoming', methods=['POST'])
def incoming_mail():
    parse_email.delay(request.form)
    return 'OK', 200
