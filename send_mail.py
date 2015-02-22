#!usr/bin/env python2

import requests
from models import Person
from prepare import start_time, max_seconds
import threading
from datetime import datetime, timedelta
import os

def send_mail():
    now = datetime.now().replace(microsecond=0)

    if now < start_time + timedelta(seconds=(max_seconds + 60)):
        threading.Timer(1.0, send_mail).start()

    people = Person.select().where(Person.send_time=now)
    for person in people:
        question = person.question
        requests.post(
            'https://api.mailgun.net/v2/govt10.danasilver.org/messages',
            auth=('api', os.environ.get('MAILGUN_API_KEY')),
            data={'from': 'Dana Silver <dana.r.silver.ug@dartmouth.edu>',
                  'to': [person.email],
                  'subject': 'One Question GOVT10 Survey',
                  'text': '''Hi! Help us out by answering our survey.
                  Just reply to this email with your answer.\n\n%s''' %
                  (person.question,)})

        person.send_time_actual = datetime.now().replace(microsecond=0)
        person.save()

send_mail()
