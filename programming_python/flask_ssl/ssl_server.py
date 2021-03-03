# Based on examples from
# https://realpython.com/python-https/#how-does-cryptography-help

import os
# an object of WSGI application
from flask import Flask, request
from tony_util.dir_diagnostics import values


os.system('color')
app = Flask(__name__)  # Flask constructor

SECRET_MESSAGE = "fluffy tail"


@app.route("/")
def get_secret_message():
    return SECRET_MESSAGE


@app.route('/details')
def details():
    # print(f'{type(request)=}')

    txt = f"Hello! Your IP is {request.remote_addr} <hr>"
    txt += f"You are using {request.user_agent} <hr>"

    txt += "Detailed request information:<br>"
    vals = values(request, mode='html', print_=False)
    txt += vals

    return txt


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5150)
