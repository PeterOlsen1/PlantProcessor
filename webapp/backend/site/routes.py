from flask import Blueprint, send_file, send_from_directory, session, redirect
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
    if session:
        return send_file(WEBAPP + "/static/html/addPlant.html")
    return redirect("/login?destination=addPlant")

@site.route('/newUser')
def serve_newUser():
    return send_file(WEBAPP + "/static/html/newUser.html")

@site.route('/invalidUser')
def serve_invalidUser():
    return send_file(WEBAPP + "/static/html/invalidUser.html")

@site.route('/fail')
def serve_fail():
    return send_file(WEBAPP + "/static/html/fail.html")

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

'''
STATIC FILES WITH STATIC IN PATHNAME
'''

@site.route('/static/css/<path:filename>')
def serve_css_static(filename):
    return send_from_directory(WEBAPP + '/static/css', filename)

@site.route('/static/js/<path:filename>')
def serve_js_static(filename):
    return send_from_directory(WEBAPP + '/static/js', filename)

@site.route('/static/html/<path:filename>')
def serve_html_static(filename):
    return send_from_directory(WEBAPP + '/static/html', filename)

@site.route('/static/views/<path:filename>')
def serve_views_static(filename):
    return send_from_directory(WEBAPP + '/static/views', filename)

'''
UPLOADED FILES
'''
@site.route('/uploads/<path:filename>')
def serve_uploads(filename):
    return send_from_directory(WEBAPP + '/backend/uploads', filename)

@site.route('/backend/uploads/<path:filename>')
def serve_uploads_backend(filename):
    return send_from_directory(WEBAPP + '/backend/uploads', filename)