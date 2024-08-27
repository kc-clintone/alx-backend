#!/usr/bin/env python3
"""
A basic Flask application with Babel for internationalization.

This app sets up a simple web server with a single route '/'.
When accessed, the route renders an HTML page with the title "Welcome to Holberton"
and a header "Hello world".

Babel is configured to support English ('en') and French ('fr') languages.
The default locale is set to English ('en') and the default timezone is UTC.
The best matching locale is determined based on the client's Accept-Language header or
a 'locale' parameter in the URL.

To test the language feature, visit:
- http://127.0.0.1:5000/?locale=fr for French
- http://127.0.0.1:5000/?locale=en for English (or default)
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Config class to hold the configuration for the Flask app and Babel.

    LANGUAGES: List of supported languages.
    BABEL_DEFAULT_LOCALE: The default locale for the application.
    BABEL_DEFAULT_TIMEZONE: The default timezone for the application.
    """

    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match for supported languages based on the client's request.

    This function first checks if the 'locale' parameter is present in the request URL
    and if it's a valid supported locale. If so, it returns that locale.
    Otherwise, it uses the client's Accept-Language header to find the best match
    among the supported languages ('en' and 'fr'). If no match is found, the default
    locale ('en') is used.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    The index view function that handles requests to the root URL
    ('/').

    This function returns the rendered HTML template 'index.html',
    which displays a page with the title "Welcome to Holberton"
    and a header "Hello world".
    """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()
