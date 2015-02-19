from flask import Flask

app = Flask(__name__)
assert isinstance(app, object)
app.config.form_object('config')

from app import views, models, password
