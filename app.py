from flask import Flask, render_template
from models import Person

DEBUG = True
SECRET_KEY = 'keep this a secret'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
