from flask import render_template, redirect, url_for, request
from app import app
from .forms import LoginForm

# route for handling login page
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'user1' or request.form['password'] != 'password':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/index')
def index():
    user = {'nickname': 'samuel'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)

@app.route("/trainingprogramme")
def trainingprogramme():
    user = {'nickname': 'samuel'}
    return render_template("trainingprogramme.html",
                           title='trainingprogramme',
                           user=user)

@app.route("/trainingprogress")
def trainingprogress():
    user = {'nickname': 'samuel'}
    return render_template("trainingprogress.html",
                           title='trainingprogress',
                           user=user)

@app.route("/personalbest")
def personalbest():
    user = {'nickname': 'samuel'}
    return render_template("personalbest.html",
                           title='personalbest',
                           user=user)

@app.route("/profile")
def profile():
    user = {'nickname': 'samuel'}
    return render_template("profile.html",
                           title='profile',
                           user=user)

@app.route('/admin', methods=['GET', 'POST'])
def adminlog():
    error = None
    if request.method == 'POST':
        if request.form['pin'] != '0000':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('admin'))
    return render_template('adminlog.html', error=error)

@app.route('/admin')
def admin():
    user = {'nickname': 'samuel'}
    return render_template("admin.html",
                           title='admin',
                           user=user)