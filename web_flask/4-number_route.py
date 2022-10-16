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


@app.route('/c/<text>', strict_slashes=False)
def c_is(text):
    """returns C <text>"""
    text = text.replace("_", " ")
    print(text)
    return "C {}".format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is(text="is cool"):
    """returns Python is <text>"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_num(n):
    """returns C is <text>"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
