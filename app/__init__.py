from flask import Flask
from flask.ext.sqlalchemy import SQLALCHEMY

app = Flask(__name__)
app.config.form_object('config')
db = SQLAlchemy(app)

from app import views, models
