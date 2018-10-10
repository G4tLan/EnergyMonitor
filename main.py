from flask import Flask, request, render_template, jsonify
from data.DBmanager import MongoDBmanager
from data.dataModel import *
from routes.userRoutes import User
from routes.visualRoutes import Visual
from routes.homeRoutes import Home
from routes.dbRoutes import MongoRoutes

app = Flask(__name__)
db = MongoDBmanager('codeTest')

@app.route('/')
@app.route('/home')
def index():
	return Home.home();
	
@app.route('/visual')
def visual():
	return Visual.default()
	
@app.route('/user')
def user():
	return User.user()

@app.route('/fetch')
def fetch():
#def fetch(buildingName: str, datalogger: str, startDateTime: str, endDateTime: str):
    return MongoRoutes.fetchData('Jubilee', 'sc3', '2018-03-01 14:30', '2018-03-01 20:00')

@app.route('/renderData')
def renderD():
    return MongoRoutes.renderData()


if __name__ == "__main__":
    filename = "C:/Users/7240/Desktop/Design - software engineering/webaPP/StitchedData/WITS_3_Jubilee_Road_kWh/WITS_3_Jubilee_Road_kWh.csv"
    #db.importCSVtoMongoDB(filename,'Jubilee','sc3', {'timestamp':'ValueTimestamp','value1':'WITS_3_Jubilee_Road_kWh','kwh':True,'kvarh':False,'update':True})
    #db.updateDataInDoc(20141212, 'Jubilee', 'sc3',  {'kwh': True, 'kvarh':False, 'value': 43, 'timestamp': '2014-12-12 00:30'})
    print(f"no objects  { TimeSeriesDataModel.objects().count()}")
    app.run(debug = True)