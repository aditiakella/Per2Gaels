"""__init__.py is used to define app and all blueprints"""
from flask import Flask
app = Flask(__name__)

""" blue prints """

from pythondb import pythondb_bp

app.register_blueprint(pythondb_bp, url_prefix='/pythondb')
