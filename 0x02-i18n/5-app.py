#!/usr/bin/env python3
"""
Task 4 module
"""

from typing import Dict, Union
from flask import Flask, render_template, request, g
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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
    Get user based on user_id.
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """
    Basic operations
    """

    g.user = get_user()


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
    Default raute
    """
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run()
