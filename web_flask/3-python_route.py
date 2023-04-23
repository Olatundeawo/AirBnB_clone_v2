#!/usr/bin/python3
""" a Script using flask for web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ return 'Hello HBNB!' """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ display 'HBNB' """
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def text(text):
    """ display 'C followed by the value of text' """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text):
    """ display python followed by value of text """
    return 'python {}'.format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
