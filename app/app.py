import os
from flask import Flask
import socket

app = Flask(__name__)


@app.route("/hostname")
def get_host_name():
    return f"<h1>{socket.gethostname()}</h1>"


@app.route("/author")
def get_author():
    return f"<h1>{os.environ.get('AUTHOR')}</h1>"


@app.route("/id")
def get_uuid():
    return f"<h1>{os.environ.get('UUID')}</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
