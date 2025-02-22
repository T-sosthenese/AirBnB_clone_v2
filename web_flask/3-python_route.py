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
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def C_text(text):
    """Returns a message with a variable passed in the url route"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def PythonText(text="is cool"):
    """Returns Python followed by text passed as a variable."""
    return "Python {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=None)
