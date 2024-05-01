from flask import Blueprint, send_file, send_from_directory
import os

WEBAPP = os.getcwd() + "/.."
site = Blueprint('site', __name__)


@site.route('/index')
def serve_index():
    return send_file(WEBAPP + "/static/html/index.html")

@site.route('/')
def serve_slash():
    return serve_index()

@site.route('/login')
def serve_login():
    return send_file(WEBAPP + "/static/html/login.html")

@site.route('/aboutMe')
def serve_aboutMe():
    return send_file(WEBAPP + "/static/html/aboutMe.html")

@site.route('/addPlant')
def serve_addPlant():
    return send_file(WEBAPP + "/static/html/addPlant.html")

@site.route('/newUser')
def serve_newUser():
    return send_file(WEBAPP + "/static/html/newUser.html")

@site.route('/requireLogin')
def serve_requireLogin():
    return send_file(WEBAPP + "/static/html/requireLogin.html")

'''
STATIC FILES
'''
@site.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory(WEBAPP + '/static/css', filename)

@site.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory(WEBAPP + '/static/js', filename)

@site.route('/html/<path:filename>')
def serve_html(filename):
    return send_from_directory(WEBAPP + '/static/html', filename)

@site.route('/views/<path:filename>')
def serve_views(filename):
    return send_from_directory(WEBAPP + '/static/views', filename)