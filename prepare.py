#!usr/bin/env python2

from peewee import *
from models import Person
import random
from datetime import datetime, timedelta

# Monday 2/23/2015 00:00 EST (05:00 UTC)
# start_time = datetime(2015, 02, 23, 0, 5, 0)
start_time = datetime(2015, 02, 22, 0, 22, 10)

# 1 day
# max_seconds = 24 * 60 * 60
max_seconds = 60


if __name__ == '__main__':
    # with open('emails.txt', 'r') as f:
    #     emails = f.read().split(';\n')

    emails = ['dana.r.silver.ug@dartmouth.edu', 'dsilver@middlebury.edu']

    with open('questions.txt', 'r') as f:
        questions = f.read().split('\n')

    for email in emails:
        # Generate a random number of seconds after the start time to send the email
        seconds = random.randint(0, max_seconds)

        # Add the seconds to the start time to get the send time
        send_time = start_time + timedelta(seconds=seconds)

        # Randomly choose a question from our list to email
        question = questions[random.randint(0, len(questions))]

        # Create a person with email and send time
        Person.create(email=email, send_time=send_time, question=question)
