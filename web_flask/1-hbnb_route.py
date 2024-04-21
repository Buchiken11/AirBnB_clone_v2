#!/usr/bin/python3

'''a script that starts a Flask web application'''

from flask import Flask

app = Flask(__name__)
# Define the url for the root route "/Hello HBNB!"
app.route('/Hello HBNB', strict_slashes=False)
def hello_hbnb1():

    '''Disply Hello HBNB'''

    return "Hello HBNB!"

# Define the url route
app.route('/hbnb', strict_slashes=False)
def hbnb():

    '''Display HBNB'''

    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
