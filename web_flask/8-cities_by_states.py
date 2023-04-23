#!/usr/bin/python3
""" a script that load all cities in states from a db """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_context(exception):
    """ closes all session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities():
    """ list all the cities in a state """
    places = storage.all(State).values()
    return render_template('8-cities_by_states.html', places=places)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
