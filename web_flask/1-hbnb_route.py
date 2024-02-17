#!/usr/bin/python3
"""
starts a web application and displays HBNB
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def helloHBNB():
    """displays Hello HBNB!"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hello():
   """displays hbnb"""
   return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
