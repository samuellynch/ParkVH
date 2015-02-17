from flask import Flask

app = Flask(__name__)
app.config.form_object('config')

from app import views, models, password

