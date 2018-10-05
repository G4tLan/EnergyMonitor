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
    db.addDataToDoc(20180912,'Mansion','log', {'timeStamp': "2019/04/03 08:19:00 PM", 'kvarh':10,'kwh':1});
    print(f"no objects  { TimeSeriesDataModel.objects().count()}")
    app.run(debug = True)