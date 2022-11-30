#!/usr/bin/python3
"""
Task 8: script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext(strict_slashes=False)
def teardown_db(exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    return render_template('7-states_list.html',
                            states=storage.all('State').values())


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
