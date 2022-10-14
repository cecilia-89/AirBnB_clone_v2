#!/usr/bin/python3
"""starts a simple flask web app"""
from flask import Flask

app = Flask(__name__)
@app.route('/', strict_slashes=False)
def hello_HBNB():
    """returns Hello HBNB on port 5000"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns hbnb on port 5000"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
