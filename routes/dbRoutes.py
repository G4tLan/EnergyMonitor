from data.DBmanager import MongoDBmanager
from flask import render_template, jsonify

db = MongoDBmanager('codeTest')

class MongoRoutes:
    def fetchData(buildingName: str, datalogger: str, startDateTime: str, endDateTime: str):
        res = db.fetchData(buildingName, datalogger, startDateTime, endDateTime)
        return jsonify(res);
        # return render_template("main.html", obj = obj);

    def renderData():
        obj = {
			'attribute' : 'visual',
			'title': 'Default view',
			'id': 4,
		};

        return render_template("main.html", obj = obj);
