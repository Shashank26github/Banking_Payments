from flask import Flask, render_template, jsonify, redirect, request
import data
from data import db
import json, data, base64
from random import choice
from datetime import datetime
import users
import os, binascii

app = Flask(__name__)
my_database = data.db('root', 'localhost', 'Shashank$26', 'customer_acq')
print(my_database)
logged_in = {}

@app.route("/login", methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
         user = users.users(request.form['username'], request.form['password'])
         if user.authenticated:
             user.session_id = str(binascii.b2a_hex(os.urandom(15)))
             logged_in[user.username] = {"object": user}
             return redirect('/profile/{}/{}'.format(request.form['username'], user.session_id))
         else:
             error = "invalid Username or Passowrd"
    return render_template('Login.htm', error=error)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.htm', title='HOME - Landing Page')
@app.route('/profile/<string:username>/<string:session>', methods=['GET', 'POST'])
def profile(username, session):
    global logged_in

    if username in logged_in and (logged_in[username]['object'].session_id == session):
        user = {
            "username": username,
            "image": "/static/images/user.jpg",
            "api": logged_in[username]["object"].api,
            "session": session,
            "firstname": logged_in[username]["object"].first,
            "lastname": logged_in[username]["object"].last,
            "email": logged_in[username]["object"].email,
            "phone": logged_in[username]["object"].phone,
            "lastlogin": logged_in[username]["object"].last_login,
        }

        devices = [
            {"Dashboard": "device1",
             "deviceID": "ARMS12012"
             }
        ]
        return render_template('profile.htm', title='Customer-acq', user=user, devices=devices)

    else:
        return redirect('/login')

@app.route('/logout/<string:username>/<string:session>', methods=['GET', 'POST'])
def logout(username, session):
    global logged_in

    if username in logged_in and (logged_in[username]['object'].session_id == session):
        logged_in.pop(username)
        # print("logged out")
        return redirect('/')
    else:
        return redirect('/login')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="80", debug=True)