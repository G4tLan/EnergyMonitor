from flask import Flask, redirect, render_template, request, session,jsonify
import os
from data.DBmanager import MongoDBmanager
from data.dataModel import *
from routes.userRoutes import User
from routes.visualRoutes import Visual
from routes.homeRoutes import Home
from routes.dbRoutes import MongoRoutes
from routes.adminRoutes import Admin
from constants import *

app = Flask(__name__)
db = MongoDBmanager('codeTest')


@app.route('/')
@app.route('/home')
def index():
    session['logged_in'] = False
    return Home.home();

#administrator routes
@app.route('/login/<int:id>')
@app.route('/login', defaults={'id': 0})
def login(id):
    session['logged_in'] = False
    return Admin.login(id);

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return Admin.logout()

@app.route('/analytics')
def analytics():
    return Admin.analytics()

@app.route('/resetpassword/<int:id>')
@app.route('/resetpassword', defaults={'id': 0})
def reset(id):
    session['logged_in'] = False
    return Admin.resetPassword(id);

@app.route('/sendpassword', methods=['POST'])
def sendPassword():
    session['logged_in'] = False
    return Admin.sendPassword();

@app.route('/verify', methods=['POST'])
def verify():
    session['logged_in'] = False
    return Admin.verifyUser();

@app.route('/widget')
def widget():
    return Admin.widget()

#DB routes
@app.route('/fetch')
def fetch():
#def fetch(buildingName: str, datalogger: str, startDateTime: str, endDateTime: str):
    return MongoRoutes.fetchData('Jubilee', 'sc3', '2018-03-01 14:30', '2018-03-01 20:00')

@app.route('/fetchBuildings')
def buildings():
    return jsonify(db.fetchBuildings())

#Misc JSON objetcs routes
@app.route('/fetchGraphTypes')
def graphTypes():
    return jsonify(chartTypes)




if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    filename = "C:/Users/7240/Desktop/Design - software engineering/webaPP/StitchedData/WITS_3_Jubilee_Road_kWh/WITS_3_Jubilee_Road_kWh.csv"
    #db.importCSVtoMongoDB(filename,'Jubilee','sc3', {'timestamp':'ValueTimestamp','value1':'WITS_3_Jubilee_Road_kWh','kwh':True,'kvarh':False,'update':True})
    #db.updateDataInDoc(20141212, 'Jubilee', 'sc3',  {'kwh': True, 'kvarh':False, 'value': 43, 'timestamp': '2014-12-12 00:30'})
    print(f"no objects  { TimeSeriesDataModel.objects().count()}")
    app.run(debug = True)