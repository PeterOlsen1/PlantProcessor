from flask import Flask, send_file, send_from_directory, request, session
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

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)



'''
APP APIs -------------------------------------------------------------------------------------------------------------------------------------

'''
@app.route('/newUser', methods=['POST'])
def new_user():
    body =  request.json
    password = body['password']
    username = body['username']
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    query("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password.decode('utf-8')))
    #bcrypt.checkpw(password.encode('utf-8'), res.encode('utf-8'))




if __name__ == '__main__':
    app.run(debug=True)
    #postgresql password = 12345
    #port : 5432