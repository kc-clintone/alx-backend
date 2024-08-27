#!/usr/bin/env python3
"""
0-app.py - A basic Flask application.

This app sets up a simple web server with a single route '/'.
When accessed, the route renders an HTML page with the title
"Welcome to Holberton"
and a header "Hello world".
"""


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """
    The index view function that handles requests to the
    root URL ('/').

    This function returns the rendered HTML template
    'index.html', which
    displays a page with the title "Welcome to Holberton" and
    a header "Hello world".
    """
    return render_template('0-index.html')
