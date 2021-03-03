# based on:
# https://overiq.com/flask-101/database-modelling-in-flask/

import os
os.system('color')

from flask import Flask, redirect, render_template, url_for
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

@app.route('/user/<name>')
def user_name(name):
    return render_template('index.html', name=name)


if __name__ == "__main__":
    app.debug = True
    app.config['SECRET_KEY'] = 'a really really really really long secret key'
    app.run()
