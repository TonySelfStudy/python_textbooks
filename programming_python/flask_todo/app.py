import os
from flask import Flask
import requests

from models import Schema
from service import ToDoService

os.system('color')
app = Flask(__name__)


@app.route("/")
def hello1():
    return 'Hello World from the root dir!'


@app.route("/<name>")
def hello(name):
    return f'Hello {name}!'


@app.route("/todo", methods=["POST"])
def create_todo():
    return ToDoService().create(request.get_json())


if __name__ == '__main__':
    Schema()
    app.run(debug=True)
