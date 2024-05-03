from flask import Blueprint, jsonify, session, request, current_app, redirect
import os
import bcrypt
from backend.db_connect import db
from werkzeug.utils import secure_filename

api = Blueprint('api', __name__, url_prefix='/api')
WEBAPP = os.getcwd() + "/.."


@api.route('/login', methods=['POST'])
def validate_login():
    '''
    -> {status : success} || {status : failure}

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
            session['name'] = name['name']
            return jsonify({'status':'success'})
    return jsonify({'status':'failure'})

@api.route('/logout')
def logout():
    '''
    -> {status: success}

    A simple logout function

    This function will clear the session when called and then send back a success.
    Only really used when clicking the nav bar logout button
    '''
    session.clear()
    return jsonify({'status':'success'})

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
    name = body['name']
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    db['users'].insert_one({"username":username, "password":hashed_password.decode('utf-8'), "name":name})
    session['username'] = username
    session['name'] = name
    return jsonify({'status':'success'})

@api.route('/userOverlap')
def user_overlap():
    '''
    -> {status: taken} || {status: open}

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

    First, upload the given file to the uploads folder with a new name.
    Once the file has been uploaded, save the path in a variable associated with the new object.
    Commit data to database and return
    '''
    data = request.form

    #get the picture and change the name so we can find it later
    picture = request.files['picture']
    filename = session['username'] +"_"+ secure_filename(picture.filename)
    picture.filename = filename
    #save the file!
    picture.save(os.path.join(os.getcwd() + "/uploads/", filename))

    #insert the new plant into the database
    insert = {
        "owner":session['username'],
        "name": data['name'],
        "species": data['species'],
        "description": data['description'],
        "lastWatered": data['lastWatered'],
        "fname": filename
    }
    db['plants'].insert_one(insert)
    return redirect('/templates/myPlants')

@api.route('/addWatering')
def add_watering():
    '''
    -> {status: success}

    A simple endpoint to add a new watering for a certain plant in the database

    Use fname to identify the plant since it should always be unique.
    Update the plant's data in the databse
    '''
    return jsonify({'status':'success'})