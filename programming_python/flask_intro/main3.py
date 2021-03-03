# Based on examples from
# https://overiq.com/flask-101/contexts-in-flask/

import os
# an object of WSGI application
from flask import Flask, request


os.system('color')
app = Flask(__name__)  # Flask constructor

@app.route('/')
def requestdata():
    txt = f"Hello! Your IP is {request.remote_addr} <hr>"
    txt += f"You are using {request.user_agent}"
    return txt


@app.route('/details')
def details():
    # print(f'{type(request)=}')

    txt = f"Hello! Your IP is {request.remote_addr} <hr>"
    txt += f"You are using {request.user_agent} <hr>"

    for i in dir(request):
        txt += f'{i} = {getattr(request, i)}<hr>'
    return txt

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    # app.run()
