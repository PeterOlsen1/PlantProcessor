from flask import Blueprint, send_file
import os

site = Blueprint('site', __name__, url_prefix='/api')
WEBAPP = os.getcwd() + "/.."

@site.route('/login')
def login_page():
    return send_file(WEBAPP + "/static/html/login")