from flask import render_template, redirect, url_for, request
from app import app

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin''user' or request.form['password'] != 'admin''password':
            
            error = 'Invalid Credentials. Please try again.'
        else:

            return redirect(url_for('index'))
    return render_template('index.html', error=error) # need to change dis stuff soon 

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
