from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html', utc_dt = datetime.datetime.utcnow())

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/comments/')
def comments():
    # Contents would come from a db in real life
    comments = ['This is the first comment.',
                'second comment.',
                'third comment.',
                'fourth comment.',
                ]
    return render_template('comments.html', comments = comments)