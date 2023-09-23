#!/usr/bin/python3
"""
A script that starts a flask web application.
Returns 'Hello HBNB' when quried at '/', 'HBNB' when queried at 'hbnb'
Listens at port 5000
"""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return ("Hello HBNB")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns hbnb when queried at hbnb"""
    return ("hbnb")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=None)
