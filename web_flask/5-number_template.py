#!/usr/bin/python3
"""
Task 5: script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def print_int(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def displays_html():
    


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
