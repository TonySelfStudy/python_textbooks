# based on:
# https://overiq.com/flask-101/contexts-in-flask/

import os
os.system('color')

from flask import Flask, request, session
app = Flask(__name__)

from tony_util.dir_diagnostics import values

@app.route('/')
def request_data():
    txt = f'Hello!<br>Your IP is: {request.remote_addr}<br>' \
          f'Your agent is: {request.user_agent}<br>'
    return txt

@app.route('/details')
def details():
    txt = f'Details on session object<br>'
    txt += values(session, mode='html', print_=False)
    txt += f'<hr><hr>Details on request object<br>'
    txt += values(request, mode='html', print_=False)
    return txt


if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)