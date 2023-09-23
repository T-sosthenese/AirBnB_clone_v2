#!/usr/bin/python3
"""
A script that starts a flask web application.
Returns 'Hello HBNB' when quried at '/', 'HBNB' when queried at 'hbnb'
Listens at port 5000
"""


from flask import Flask, render_template


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


@app.route("/number/<int:n>", strict_slashes=False)
def Number(n):
    """Tells a user whether a given variable is a number."""
    if type(n) == int:
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def ReturnNumberPage(n):
    """Returns a html page if n is an integer."""
    if type(n) == int:
        return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def OddOrEven(n=None):
    """Diplays a page indicating whether an integer is odd or even."""
    if type(n) == int:
        if n % 2:
            nv = "odd"
        else:
            nv = "even"
        return render_template("6-number_odd_or_even.html", n=n, nv=nv)


if __name__ == '__main__':
    app.run()
