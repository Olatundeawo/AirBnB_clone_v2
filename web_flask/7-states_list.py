#!/usr/bin/python3
""" A script that remove the current session
    List all states present in a db in a sorted order
"""
from flask import Flask, render_template
from models import storage, State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_context(exception):
    """ remove the current session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state():
    """ display a list of states from a db into a HTML page """
    places = storage.all(state).values()
    return render_template('7-states_list.html', places=places)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
