#!/usr/bin/python3
"""
Starts a flask application listing cities by the origin states"""


from models import storage
from flask import Flask, render_template
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Cities by their states of origin"""
    states = storage.all(State)
    return render_template("9-states.html", state=states)


@app.route('/states/<id>', strict_slashes=False)
def states_with_id(id):
    """
    Listing states with their respective ids
    """
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """Disconnects the current sqlalchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0")
