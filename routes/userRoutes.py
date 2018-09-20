from flask import render_template

class User():
	def user():
		obj = {
			'attribute' : 'user',
			'name' : 'Gift',
			'title': 'Profile'
		};
		return render_template("main.html", obj = obj);
