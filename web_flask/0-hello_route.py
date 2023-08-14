#!/usr/bin/python3
""" this module start a web app with flask """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """  a hello word page """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
