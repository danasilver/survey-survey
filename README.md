# GOVT 10 Final Project
## Tools for conducting a survey about surveys

### Commands

Prefix with `heroku run` to run on server.

#### Create the db

```
python models.py
```

#### Prepare the database to send

```
python prepare.py
```

### Sending

Set up task on Heroku to run `python send_mail.py` at 2015-02-23 05:00:00 +0000.

### Survey Process

1. Randomly assign a number between 0 and 172,800 (2 days in seconds) to each
of the Dartmouth undergraduate student emails.

2. Randomly assign a survey question to each student.

3. Email each student at the number of seconds after a chosen 0-hour. The email
should contain the survey question and a request that the student respond by
replying to the email.

### Definitions

Unless otherwise noted, "random" refers to a uniform random distribution.
Internally randomness is generated using a
[Mersenne twister](http://en.wikipedia.org/wiki/Mersenne_twister).