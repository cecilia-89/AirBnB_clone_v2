#!/usr/bin/python3
"""starts a simple flask web app"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """displays all the states"""
    Storage = storage.all(State)
    return render_template("9-states.html", States=Storage)


@app.route('/states/<id>', strict_slashes=False)
def list_states(id):
    """lists all cities in alphabetical order"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", States=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def tear_Down(exception):
    """closes a db session or reload file storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
