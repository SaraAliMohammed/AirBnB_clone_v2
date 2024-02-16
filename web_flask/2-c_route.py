#!/usr/bin/python3
''' Script that starts a Flask web application '''
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ hello home page """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ HBNB page """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ Display 'C ' followed by the value of the text variable
    (replace underscore _ symbols with a space  """
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
