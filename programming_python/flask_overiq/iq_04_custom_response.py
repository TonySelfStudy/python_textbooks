# based on:
# https://overiq.com/flask-101/custom-response-and-hook-points-in-flask/

import os
os.system('color')

from flask import Flask, request, session, make_response
app = Flask(__name__)

from tony_util.dir_diagnostics import values

@app.route('/books/<genre>')
def books(genre):
    res = make_response("All Books in {} category".format(genre))
    res.headers['Content-Type'] = 'text/plain'
    res.headers['Server'] = 'Foobar'
    # print(values(res))
    return res


if __name__ == "__main__":
    app.run(debug=True)