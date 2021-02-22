"""Views in MVC has responsibility for establishing routes and redering HTML"""
from flask import render_template, request, redirect, url_for
from __init__ import app
import requests

"""Main navigation Section"""


# This section of code is driven by data, review data descriptions for understanding


@app.route('/')
def index():
    return render_template("index.html")
