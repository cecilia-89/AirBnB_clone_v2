#!/usr/bin/python3
"""starts a simple flask web app"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """lists all states in alphabetical order"""
    States = storage.all(State).values()
    return render_template("7-states_list.html", States=States)


@app.teardown_appcontext
def tear_Down(exception):
    """closes a db session or reload file storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
