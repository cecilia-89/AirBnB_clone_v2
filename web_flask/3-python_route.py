#!/usr/bin/python3
"""starts a simple flask web app"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)
@app.route('/', strict_slashes=False)
def hello_HBNB():
	return "Hello HBNB!\n"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
	return "HBNB\n"

@app.route('/c/<text>', strict_slashes=False)
def c_is(text):
	"""returns C is <text>"""

	return f"C {text}\n"

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is(text="is cool"):
	"""returns Python is <text>"""
	
	text = text.replace('_', ' ')
	return f"Python {text}\n"

if __name__ == "__main__":
	app.run(host="0.0.0.0")