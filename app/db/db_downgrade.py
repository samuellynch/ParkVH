#!flask/bin/python
from migrate.versioning import api
from config import SQLALCHEMY_DATABSE_URI
from config import SQLALCHEMY_MIGRATE_REPO
v = api.db_version(SQLALCHEMY_DATABSE_URI, SQLALCHEMY_MIGRATE_REPO)
api.downgrade(SQLALCHEMY_DATABSE_URI, SQLALCHEMY_MIGRATE_REPO, v - 1)
v = api.db_version(SQLALCHEMY_DATABSE_URI, SQLALCHEMY_MIGRATE_REPO)
print('Current database version: ' + str(v))
