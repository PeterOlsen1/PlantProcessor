from flask import Flask, send_file, request, session, jsonify, render_template
import os
# import psycopg2
import bcrypt
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from backend.site.routes import site
from backend.api.routes import api
from db_connect import db

'''
GLOBALS -------------------------------------------------------------------------------------------------------------------------------------

'''
FRONTEND = os.getcwd() + "/.."
UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__, 
            template_folder='/' + FRONTEND + '/templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.register_blueprint(site)
app.register_blueprint(api)

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
    #postgresql password = 12345
    #port : 5432