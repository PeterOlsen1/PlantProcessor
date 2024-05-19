from flask import Flask, send_file, request, session, jsonify, render_template
from os import path, getcwd
from sys import path as syspath
SCRIPT_DIR = path.dirname(path.abspath(__file__))
syspath.append(path.dirname(SCRIPT_DIR))
from backend.site.routes import site
from backend.api.routes import api
from backend.template.routes import template
from db_connect import db

'''
GLOBALS -------------------------------------------------------------------------------------------------------------------------------------

'''
FRONTEND = getcwd() + "/.."
UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__, 
            template_folder='/' + FRONTEND + '/templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.register_blueprint(site)
app.register_blueprint(api)
app.register_blueprint(template)

app.secret_key = 'bob'

'''
APP ROUTES -------------------------------------------------------------------------------------------------------------------------------------

'''

@app.route('/test')
def test():
    if session:
        return render_template('myPlants.html', session=session, login=True)
    else:
        return send_file(FRONTEND + '/staitc/html/requreLogin.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)