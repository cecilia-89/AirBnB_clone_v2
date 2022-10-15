#!/usr/bin/python3
"""starts a simple flask web app"""
from flask import Flask

app = Flask(__name__)
@app.route('/', strict_slashes=False)
def hello_HBNB():
    """displays Hello HBNB! on port 5000jjjjjjjjjjj"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
