from flask import render_template

class Home():
	def home():
		obj = {
		'attribute' : 'home',
		'title' : 'Homepage',
		'paragraph' : 'This is the homepage check best and worst energy users'
		};
		return render_template("homepage.html", obj = obj);
