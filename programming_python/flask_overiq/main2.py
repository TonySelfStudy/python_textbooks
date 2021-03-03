# based on:
# https://overiq.com/flask-101/templates-in-flask/
# https://overiq.com/flask-101/serving-static-files-in-flask/


import os
os.system('color')

from flask import Flask, redirect, render_template, \
                  url_for, request, make_response
app = Flask(__name__)

@app.route('/user/<name>')
def user_name(name):
    return render_template('index.html', name=name)

@app.route('/user/')
def user_default():
    return redirect(url_for('user_name', name='jerry'))

@app.route('/example/')
def static_example1():
    txt = url_for('static', filename='jquery.js')
    # print(txt)
    return redirect(url_for('static', filename='example1.html'))

@app.route('/example2/<name>')
def static_example2(name):
    return render_template('index.html', name=name)

@app.route('/login/', methods=['post', 'get'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form.get('username')  # access the data inside
        password = request.form.get('password')

        if username == 'root' and password == 'pass':
            message = "Correct username and password"
        else:
            message = "Wrong username or password"

    return render_template('login.html', message=message)

@app.route('/cookie/')
def cookie():
    res = make_response("Setting a cookie")
    res.set_cookie('foo', 'bar', max_age=60*60*24*365*2)
    return res

@app.route('/cookie2/')
def cookie2():
    if not request.cookies.get('my_key'):
        res = make_response("Setting a cookie")
        res.set_cookie('my_key', 'my_val', max_age=60*60*24*365*2)
    else:
        res = make_response("Value of cookie my_key is {}".format(request.cookies.get('my_key')))
    return res

if __name__ == "__main__":
    app.debug = True
    app.config['SECRET_KEY'] = 'a really really really really long secret key'
    app.run()


"""Map([<Rule '/' (OPTIONS, GET, HEAD) -> index>,
 <Rule '/static/<filename>' (OPTIONS, GET, HEAD) -> static>,
 <Rule '/books/<genre>' (OPTIONS, GET, HEAD) -> books>,
 <Rule '/user/<user_id>' (OPTIONS, GET, HEAD) -> user_profile>])"""