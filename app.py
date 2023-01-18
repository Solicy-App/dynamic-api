# Standard Library Imports
from sys import path as syspath
from os import path as ospath

# Third Party Imports
from flask import Flask, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from director import direct_api

# Failsafe to ensure local imports always work
script_directory = ospath.join(ospath.dirname(ospath.realpath(__file__)))
if script_directory not in syspath:
    syspath.append(script_directory)

# Setup Flask
app = Flask(__name__.split('.')[0])

# Configure Database Connection
# app.config["DEBUG"] = True
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username='root',
    password='root',
    hostname='localhost',
    databasename='db',
)
CORS(app, resources={r"/*": {"origins": "*"}})

# Connect to database.
database = SQLAlchemy(app)

# Variable Initialization
processor = {}


# Main Page.
def index():
    return redirect('https://<User>.pythonanywhere.com/index.html', code=302, Response=None)


# Redirect all unknown
def page_not_found(e):
    return render_template('404.html'), 404


# Default Server Functionality
app.add_url_rule('/', view_func=index)
app.add_url_rule("/", view_func=direct_api(database), methods=['POST'])
app.register_error_handler(404, page_not_found)
