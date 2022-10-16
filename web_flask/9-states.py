#!/usr/bin/python3
"""starts a simple flask web app"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
@app.route('/states/', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def list_states(id=""):
    """lists all cities in alphabetical order"""
    Storage = storage.all(State)
    for state in Storage.values():
        if state.id == id:
            return render_template("9-states.html", States=state)
        elif id == "":
            return render_template("9-states.html", States=Storage)
    return render_template("9-states.html")


@app.teardown_appcontext
def tear_Down(exception):
    """closes a db session or reload file storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
