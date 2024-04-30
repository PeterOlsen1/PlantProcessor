from flask import Blueprint, send_file
import os

site = Blueprint('site', __name__)
WEBAPP = os.getcwd() + "/.."

@site.route('/login')
def login_page():
    return send_file(os.getcwd() + "/../static/html/login")