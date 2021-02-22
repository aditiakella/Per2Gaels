"""Views in MVC has responsibility for establishing routes and redering HTML"""
from flask import render_template
from control import app
from views.pythondb import pythondb_bp
"""Defining routes"""
app.register_blueprint(pythondb_bp, url_prefix='/pythondb')

"""Main navigation section"""

@app.route('/')
def index():
    return render_template("base.html")