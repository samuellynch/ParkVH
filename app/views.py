from flask import render_template, redirect, url_for, request
import json
from app import app


# route for handling login page
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'runner' or request.form['password'] != 'password':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.route('/index')
def index():
    user = {'nickname': 'runner'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)


@app.route("/trainingprogramme", methods=['GET', 'POST'])
def trainingprogramme():
    with open('activity.json', 'r') as f:
        data = json.loads(f.read())
    if request.method == 'POST':
        data.append([request.form['name'], request.form['date'], request.form['activity'], request.form['speed'],
                     request.form['hours']])
        with open('activity.json', 'w') as f:
            f.write(json.dumps(data))
    user = {'nickname': 'runner'}
    return render_template("trainingprogramme.html",
                           title='profile',
                           user=user,
                           training=data)


@app.route("/profile", methods=['GET', 'POST'])
def profile():
    with open('profile.json', 'r') as f:
        data = json.loads(f.read())
    if request.method == 'POST':
        data.append([request.form['name'], request.form['age'], request.form['Gender'], request.form['MedInfo'],
                     request.form['RecentAct']])
        with open('profile.json', 'w') as f:
            f.write(json.dumps(data))
    user = {'nickname': 'runner'}
    return render_template("profile.html",
                           title='profile',
                           user=user,
                           profile=data)


@app.route('/adminlog', methods=['GET', 'POST'])
def adminlog():
    error = None
    if request.method == 'POST':
        if request.form['pin'] != '0000':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('admin'))
    return render_template('adminlog.html', error=error)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    with open('activity.json') as data_file:
        data = json.load(data_file)
        print(data)
    user = {'nickname': 'runner'}
    return render_template("admin.html",
                           title='admin',
                           user=user,
                           training=data)