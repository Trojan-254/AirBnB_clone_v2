#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)
app.config['STRICT_SLASHES'] = False

@app.route('/')
def helloHBNB():
    """displays Hello HBNB!"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
