# based on:
# https://overiq.com/flask-101/form-handling-in-flask/

import os
os.system('color')

from flask import Flask, redirect, render_template, url_for
app = Flask(__name__)

@app.route('/user/<name>')
def user_name(name):
    return render_template('index.html', name=name)


if __name__ == "__main__":
    app.run(debug=True)