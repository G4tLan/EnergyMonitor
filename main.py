from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
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
	return Visual.default(id);
	
@app.route('/user')
def user():
	return User.user();
	
if __name__ == "__main__":
	app.run(debug = True)