from flask import render_template

class Visual():
	def default(id):
		obj = {
			'attribute' : 'visual',
			'title': 'Default view',
			'id': id
		};
		return render_template("main.html", obj = obj);
