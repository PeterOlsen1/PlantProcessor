from flask import Flask, send_file, send_from_directory, request, session, jsonify, render_template
import os
import psycopg2
from psycopg2 import pool
import bcrypt
import json

'''
GLOBALS -------------------------------------------------------------------------------------------------------------------------------------

'''
CWD = os.getcwd()
app = Flask(__name__, '/' + CWD + '/static')
app.secret_key = 'bob'

def query(query, params=None):
    '''
    A function to make querying easier.
    Makes queries a few lines shorter by automating the connection/cursor part of PostgreSQL
    If the query was a select, return all data that came from it, otherwise do nothing
    '''
    connection = psycopg2.connect(database="plants", user="postgres", password="12345", host="localhost", port="5432") 
    cursor = connection.cursor()
    cursor.execute(query, params)
    connection.commit()
    if "SELECT" in query.upper():
        return cursor.fetchall()


'''
APP ROUTES -------------------------------------------------------------------------------------------------------------------------------------

'''
@app.route('/')
def welcome():
    return send_file(CWD + '/static/html/index.html')

@app.route('/test')
def test():
    return render_template('myPlants.html', session=session)

@app.route('/addPlant', methods=["POST"])
def post_addPlant():
    data = request.form
    picture = request.files['picture']
    path = 'uploads'
    picture.save('/uploads')
    # query("INSERT INTO users (user_id, name, species, description, watered, picture) VALUES (%s, %s, %s, %s, %s, %s)", (session['id'], data.name, data.species, data.description, data.watered, filepath))
    return jsonify({'dope':'dope'})#render_template('myPlants.html', session=session)

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)



'''
APP APIs -------------------------------------------------------------------------------------------------------------------------------------

'''

@app.route('/validate-login', methods=['POST'])
def validate_login():
    '''
    Select all of the given name from the databse. If password matches, return success
    '''
    body = request.json
    password = body['password']
    username = body['username']
    names = query("SELECT * FROM users WHERE username = %s", (username,))
    for name in names:
        if (bcrypt.checkpw(password.encode('utf-8'), name[2].encode('utf-8'))):
            session['username'] = name[1]
            session['id'] = name[0]
            return jsonify({'status':'success'})
    return jsonify({'status':'failure'})


@app.route('/addUser', methods=['POST'])
def add_user():
    '''
    This function will add a new user to the databse
    '''
    body =  request.json
    password = body['password']
    username = body['username']
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    query("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password.decode('utf-8')))
    session['username'] = username
    session['id'] = (query("SELECT * FROM users WHERE username = %s", (username,)))[0]
    return jsonify({'status':'success'})

@app.route('/userOverlap')
def user_overlap():
    '''
    Function to check if the given username exists in the database
    '''
    name = request.args.get('username')
    result = query("SELECT * FROM users WHERE username = %s", (name,))
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
    #postgresql password = 12345
    #port : 5432