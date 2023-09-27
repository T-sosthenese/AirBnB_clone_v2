#!/usr/bin/python3
"""
Starts a flask app listing cities by state
"""

from models import storage
from flask import Flask, render_template
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Displays hbnb filters"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """Disconnects the current sqlalchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0")
