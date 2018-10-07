from flask import Flask, request, render_template, jsonify
from data.DBmanager import MongoDBmanager
from data.dataModel import *
from routes.userRoutes import User
from routes.visualRoutes import Visual
from routes.homeRoutes import Home

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
	return Home.home();
	
@app.route('/visual<int:id>')
def visual(id):
	return Visual.default(id)
	
@app.route('/user')
def user():
	return User.user()
	
if __name__ == "__main__":
    db = MongoDBmanager('codeTest')
    filename = "C:/Users/7240/Desktop/Design - software engineering/webaPP/StitchedData/WITS_3_Jubilee_Road_kVarh/WITS_3_Jubilee_Road_kVarh.csv"
    #db.importCSVtoMongoDB(filename,'Jubilee','sc3', {'timestamp':'ValueTimestamp','value':'WITS_3_Jubilee_Road_kVarh'})
    db.updateDataInDoc(20141212, 'Jubilee', 'sc3',  {'kwh': False, 'kvarh':False, 'value': 100, 'timestamp': '2014-12-12 00:30'})
    print(f"no objects  { TimeSeriesDataModel.objects().count()}")
    app.run(debug = True)