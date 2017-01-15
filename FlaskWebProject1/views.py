"""
Routes and views for the flask application.
"""
import os
from datetime import datetime
from flask import render_template, request
from FlaskWebProject1 import app


@app.route('/')
def form():
    return render_template('form_submit.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is
# accepting: POST requests in this case
@app.route('/hello/', methods=['POST'])
def hello():
    name=request.form['yourname']
    email=request.form['youremail']
    lol = os.popen("python3 wiki.py " + name).read()
    return render_template('form_action.html', name=lol, email=email)

# @app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/kalol')
def kalol():
    """Renders the about page."""
    return render_template(
        'kalol.html',
        title='kalol'
    )
