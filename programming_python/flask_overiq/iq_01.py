# based on:
# https://www.geeksforgeeks.org/python-introduction-to-web-development-using-flask/

import os
os.system('color')

# an object of WSGI application
from flask import Flask, redirect, url_for
app = Flask(__name__)

# @app.route('/')
# def index():
#     return "Hello World from iq_01.py's index()"
#
# def index2():
#     return 'Hello World from index2'
# app.add_url_rule('/index2', 'index2', index2)


@app.route('/')
def index():
    print(i)
    return 'Home Page'

@app.route('/career/')
def career():
    return 'Career Page'


@app.route('/contact/')
@app.route('/feedback/')
def feedback():
    return 'Feedback Page'

@app.route('/user/<my_id>')
def user_info(my_id):
    return f'Welcome user {my_id}'

@app.route('/data/<string:my_id>')
def data_str(my_id):
    return f'User specified by string: {my_id}'

@app.route('/data/<int:my_id>')
def data_int(my_id):
    return f'User specified by int: {my_id}'

@app.route('/data/<float:my_id>')
def data_float(my_id):
    return f'User specified by float: {my_id}'

@app.route('/data/<path:my_id>')
def data_path(my_id):
    return f'User specified by path: {my_id}'


if __name__ == "__main__":
    app.run(debug=True)
