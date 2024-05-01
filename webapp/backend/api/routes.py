from flask import Blueprint, send_file, jsonify, session, request
import os
import bcrypt
from backend.db_connect import db
from backend.server import ALLOWED_EXTENSIONS, UPLOAD_FOLDER

api = Blueprint('api', __name__, url_prefix='/api')
WEBAPP = os.getcwd() + "/.."


@api.route('/login', methods=['POST'])
def validate_login():
    '''
    -> {status : success} | {status : failure}

    Select all of the given name from the databse. If password matches, return success

    Select all names from the database that correspond to the given one.
    Loop through all names found, and bcrypt compare the passwords.
    If there is a match, immediatley return a success and stop.
    Otherwise, return a failure.
    '''
    body = request.json
    password = body['password']
    username = body['username']
    names = db['users'].find({"username":username})
    for name in names:
        print(name)
        if (bcrypt.checkpw(password.encode('utf-8'), name['password'].encode('utf-8'))):
            session['username'] = name['username']
            return jsonify({'status':'success'})
    return jsonify({'status':'failure'})


@api.route('/addUser', methods=['POST'])
def add_user():
    '''
    -> {status : success}

    This function will add a new user to the databse

    Hashes the uploaded username and then inserts into the users database the username and hashed password
    Will return status success when done
    '''
    body =  request.json
    password = body['password']
    username = body['username']
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    db['users'].insert_one({"username":username, "password":hashed_password.decode('utf-8')})
    session['username'] = username
    return jsonify({'status':'success'})

@api.route('/userOverlap')
def user_overlap():
    '''
    -> {status: taken} | {status: open}

    Function to check if the given username exists in the database

    First, query the database.
    Upon completion, transform the results into a list of objects.
    If the list is nonempty, the username is taken and the status "taken" will be returned.
    If empty, there are no users in the database with the same name, and "open" will be returned
    '''
    name = request.args.get('username')
    result = db['users'].find({"username":name})
    lst = list(result)
    if lst:
        return jsonify({"status":"taken"})
    else:
        return jsonify({"status":"open"})

@api.route('/addPlant', methods=["POST"])
def post_addPlant():
    '''
    ->

    API endpoint to add a plant to the database, still a work in progress

    First, upload the given file to memory.
    Once the file has been uploaded, save the path in a variable associated with the new object.
    Commit data to database and return
    '''
    data = request.form
    picture = request.files['picture']
    picture.save('/../uploads')
    # query("INSERT INTO plants (user_id, name, species, description, watered, picture) VALUES (%s, %s, %s, %s, %s, %s)", (session['id'], data.name, data.species, data.description, data.watered, filepath))
    return jsonify({'dope':'dope'})#render_template('myPlants.html', session=session)