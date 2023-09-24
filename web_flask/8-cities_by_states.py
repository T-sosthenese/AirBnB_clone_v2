#!/usr/bin/python3
"""
Starts a flask web application that lists cities by state
"""

from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Lists cities depending on the states they are found."""
    s = storage.all(State)
    return render_template("8-cities_by_states.html", s=s)


@app.teardown_appcontext
def teardown(exc):
    """Destroys the current sqlalchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0")
