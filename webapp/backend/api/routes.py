from flask import Blueprint, send_file
import os

api = Blueprint('site', __name__, url_prefix='/api')
WEBAPP = os.getcwd() + "/.."

