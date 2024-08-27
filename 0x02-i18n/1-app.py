#!/usr/bin/env python3
"""
0-app.py - A basic Flask application with Babel for
internationalization.

This app sets up a simple web server with a single route '/'.
When accessed, the route renders an HTML page with the title
"Welcome to Holberton"
and a header "Hello world".

Babel is configured to support English ('en') and French ('fr')
languages
"""

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """
    Config class to hold the configuration for the Flask app and Babel.

    LANGUAGES: List of supported languages.
    BABEL_DEFAULT_LOCALE: The default locale for the application.
    BABEL_DEFAULT_TIMEZONE: The default timezone for the application.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """
    The index view function that handles requests to the root
    URL ('/').

    This function returns the rendered HTML template 'index.html',
    which displays a page with the title "Welcome to Holberton"
    and a header "Hello world".
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
