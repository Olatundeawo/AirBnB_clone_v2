#!/usr/bin/python3
""" a script that starts a Flask web application """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ displays Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ displays HBNB """
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def text(text):
    """ displays c + text """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python/", defaults={"text": "is cool"})
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text):
    """ displays Python + text """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ display an integer """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ display a HTML page """
    return render_template('5-number.html',n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
