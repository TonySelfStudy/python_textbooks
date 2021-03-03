# based on:
# https://www.geeksforgeeks.org/python-introduction-to-web-development-using-flask/

import os

# an object of WSGI application
from flask import Flask, redirect, url_for

os.system('color')
app = Flask(__name__)  # Flask constructor


# A decorator used to tell the application
# which URL is associated function
@app.route('/')
def hello():
    return 'HELLO'

# decorator to route URL
@app.route('/hello')
# binding to the function of route
def hello_world():
    return 'hello world'

def hello_world2():
    return 'hello world2'
app.add_url_rule('/hello2', 'hello2', hello_world2)

# routing the decorator function hello_name
@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello {name}!'

@app.route('/blog/<postID>')
def show_blog(postID):
    num = int(postID)
    return f'Blog Number {num}'

@app.route('/rev/<revNo>')
def revision(revNo):
    num = float(revNo)
    return f'Revision Number {num}'

@app.route('/user/<name>')
def hello_guest(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_name', name=name))

@app.route('/hello_admin')
def hello_admin():
    return f'hello master control'


if __name__ == '__main__':
    app.run(debug=True)
