from flask import render_template

class Visual():
	def default():
		obj = {
			'attribute' : 'Dashboard',
			'title': 'Dashboard View',
            'name': 'Dashboard'
		};
		return render_template("homepage.html", obj = obj);
