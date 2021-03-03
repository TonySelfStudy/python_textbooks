# Based on examples from
# https://www.geeksforgeeks.org/python-introduction-to-web-development-using-flask/

import os
# an object of WSGI application
from flask import Flask

os.system('color')
app = Flask(__name__)  # Flask constructor


# # A decorator used to tell the application
# # which URL is associated function
# @app.route('/')
# def hello():
#     print('In hello()')
#     txt = 'Route=/, func=hello'
#     print(f'Return Text: {txt}')
#     return txt
#
#
# # decorator to route URL
# @app.route('/hello')
# def hello_world():
#     print('In hello_world()')
#     txt = 'Route=/hello, func=hello_world'
#     return txt
#
#
# # routing the decorator function hello_name
# @app.route('/hello/<name>')
# def hello_name(name):
#     return f'Hello {name}!'
#
#
# @app.route('/blog/<postID>')
# def show_blog(postID):
#     return f'Blog Number {postID}'
#
#
# @app.route('/rev/<revNo>')
# def revision(revNo):
#     return f'Revision Number {revNo}'
#
#
def hello2():
    print('In hello2()')
    txt = 'Route=/test/hello2, func=hello2'
    print(txt)
    return txt
app.add_url_rule('/test/hello2/', 'hello2', hello2)

def index():
    return 'Hello World from index()'
app.add_url_rule('/', 'index', index)


if __name__ == '__main__':
    # app.run(debug=True, port=80)
    app.run(port=80)
