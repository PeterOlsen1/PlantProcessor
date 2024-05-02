from flask import Blueprint, render_template, session, redirect, request
import os
from backend.db_connect import db
from datetime import datetime

WEBAPP = os.getcwd() + "/.."
template = Blueprint('template', __name__, url_prefix='/templates')\

def dateDifference(date_str):
    # Initialize both date objects
    current_date = datetime.now()
    year = int(date_str[:4])
    month = int(date_str[5:7])
    day = int(date_str[8:])
    other_date = datetime(year, month, day)

    # Calculate the difference between the two dates
    timedelta = current_date - other_date
    day_difference = timedelta.days
    return day_difference


@template.route('/myPlants')
def templates_myPlants():
    if session:
        plants = list(db['plants'].find({"owner":session['username']}))
        return render_template('myPlants.jinja', 
                               session=session, 
                               plants=plants, 
                               dateDifference=dateDifference)
    else:
        return redirect('/login')

@template.route('/plant')
def templates_plant():
    if session:
        fname = request.args.get('fname')
        print(fname)
        plant = list(db['plants'].find_one({"fname":fname}))
        return render_template('plant.jinja', 
                               session=session, 
                               plant=plant, 
                               dateDifference=dateDifference)
    else:
        return redirect('/login')
    

@template.route('/editPlant')
def templates_editPlant():
    if session:
        plants = list(db['plants'].find({"owner":session['username']}))
        return render_template('editPlant.jinja', 
                               session=session, 
                               plants=plants)
    else:
        return redirect('/login')