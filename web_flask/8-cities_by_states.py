#!/usr/bin/python3
"""
Task 9. script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Removes the current SQLAlchemy Session"""
    storage.close()
    

@app.route('/cities_by_states', strict_slashes=False)
def state_cities():
    """Renders all cities of each state"""
    return render_template(
        '8-cities_by_states.html', states=storage.all("State").values()
        )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)