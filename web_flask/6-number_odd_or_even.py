#!/usr/bin/python3
"""starts a simple flask web app"""
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/', strict_slashes=False)
def hello_HBNB():
	"""returns Hello HBNB on port 5000"""

	return "Hello HBNB!\n"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
	"""returns hbnb on port 5000"""

	return "HBNB\n"

@app.route('/c/<text>', strict_slashes=False)
def c_is(text):
	"""returns `C <text>`"""
	return f"C {text}\n"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is(text="is cool"):
	"""returns `Python is <text>`"""
	text = text.replace('_', ' ')
	return f"Python {text}\n"


@app.route('/number/<int:n>', strict_slashes=False)
def is_num(n):
	"""returns n if `n` is a number"""
	return f"{n} is a number\n"

@app.route('/number_template/<int:n>', strict_slashes=False)
def render_if_num(n):
	"""returns html page if n isnum"""
	return render_template('5-number.html', value=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
	"""returns html page if n isnum"""
	return render_template('6-number_odd_or_even.html', value=n)



if __name__ == "__main__":
	app.run(host="0.0.0.0")