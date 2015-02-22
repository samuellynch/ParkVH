from flask import render_template, flash, redirect, url_for
from app import app

@app.route('/')
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