from flask import render_template

class Home():
	def home():
		obj = {
		'attribute' : 'home',
		'title' : 'Homepage',
		'paragraph' : 'This is your dashboard check energy usage, costs and estimate breakeven'
		};
		return render_template("main.html", obj = obj);
