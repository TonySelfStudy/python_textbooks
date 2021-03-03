# based on:
# https://www.geeksforgeeks.org/python-introduction-to-web-development-using-flask/

import os
os.system('color')

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/user/<int:user_id>/')
def user_profile(user_id):
    return "Profile page of user #{}".format(user_id)

@app.route('/books/<genre>/')
def books(genre):
    return "All Books in {} category".format(genre)

if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)