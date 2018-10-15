from flask import Flask, redirect, render_template, request, session,jsonify
import os
from data.DBmanager import MongoDBmanager
from data.dataModel import *
from routes.userRoutes import User
from routes.visualRoutes import Visual
from routes.homeRoutes import Home
from routes.dbRoutes import MongoRoutes
from routes.adminRoutes import Admin
from constants import *

app = Flask(__name__)
db = MongoDBmanager('codeTest')


@app.route('/')
@app.route('/home')
def index():
    session['logged_in'] = False
    return Home.home();

#administrator routes
@app.route('/login/<int:id>')
@app.route('/login', defaults={'id': 0})
def login(id):
    session['logged_in'] = False
    return Admin.login(id);

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return Admin.logout()

@app.route('/analytics')
def analytics():
    return Admin.analytics()

@app.route('/resetpassword/<int:id>')
@app.route('/resetpassword', defaults={'id': 0})
def reset(id):
    session['logged_in'] = False
    return Admin.resetPassword(id);

@app.route('/sendpassword', methods=['POST'])
def sendPassword():
    session['logged_in'] = False
    return Admin.sendPassword();

@app.route('/verify', methods=['POST'])
def verify():
    session['logged_in'] = False
    return Admin.verifyUser();

@app.route('/widget')
def widget():
    return Admin.widget()

#DB routes
@app.route('/fetch/<building>/<start>/<end>')
def fetch(building,start,end):
    return MongoRoutes.fetchData(building, start, end)

@app.route('/fetchBuildings')
def buildings():
     try:
        if session['logged_in']:
            return jsonify(db.fetchBuildings())
    
        return redirect('/home')
     except KeyError:
        return redirect('/home')
    

@app.route('/ranking')
def ranking():
    return jsonify(db.getWorstBestBuildings())



#Misc JSON objetcs routes
@app.route('/fetchGraphTypes')
def graphTypes():
    return jsonify(chartTypes)

def proc():
    #girton Hall
    #initial
    filename = "C:/Users/7240/Desktop/Design - software engineering/webaPP/StitchedData/WITS_PEC_Residence_Girton_Hall_kVarh/WITS_PEC_Residence_Girton_Hall_kVarh.csv"
    db.importCSVtoMongoDB(filename,'Girton','sc3', {'timestamp':'ValueTimestamp','value1':'WITS_PEC_Residence_Girton_Hall_kVarh', 'value2':None,'kwh':False,'kvarh':True,'update':False})
    
    #update
    filename = "C:/Users/7240/Desktop/Design - software engineering/webaPP/StitchedData/WITS_PEC_Residence_Girton_Hall_kWh/WITS_PEC_Residence_Girton_Hall_kWh.csv"
    db.importCSVtoMongoDB(filename,'Girton','sc3', {'timestamp':'ValueTimestamp','value1':'WITS_PEC_Residence_Girton_Hall_kWh','kwh':True,'kvarh':False,'update':True})
    
    #Medhurst Hall
    #initial
    filename = "C:/Users/7240/Desktop/Design - software engineering/webaPP/StitchedData/WITS_PEC_Residence_Medhurst_Hall_kVarh/WITS_PEC_Residence_Medhurst_Hall_kVarh.csv"
    db.importCSVtoMongoDB(filename,'Medhurst','sc3', {'timestamp':'ValueTimestamp','value1':'WITS_PEC_Residence_Medhurst_Hall_kVarh', 'value2':None,'kwh':False,'kvarh':True,'update':False})
    
    #update
    filename = "C:/Users/7240/Desktop/Design - software engineering/webaPP/StitchedData/WITS_PEC_Residence_Medhurst_Hall_kWh/WITS_PEC_Residence_Medhurst_Hall_kWh.csv"
    db.importCSVtoMongoDB(filename,'Medhurst','sc3', {'timestamp':'ValueTimestamp','value1':'WITS_PEC_Residence_Medhurst_Hall_kWh','kwh':True,'kvarh':False,'update':True})

    #Reith Hall
    #initial
    filename = "C:/Users/7240/Desktop/Design - software engineering/webaPP/StitchedData/WITS_PEC_Residence_Reith_Hall_kVarh/WITS_PEC_Residence_Reith_Hall_kVarh.csv"
    db.importCSVtoMongoDB(filename,'Reith','sc3', {'timestamp':'ValueTimestamp','value1':'WITS_PEC_Residence_Reith_Hall_kVarh', 'value2':None,'kwh':False,'kvarh':True,'update':False})
    
    #update
    filename = "C:/Users/7240/Desktop/Design - software engineering/webaPP/StitchedData/WITS_PEC_Residence_Reith_Hall_kWh/WITS_PEC_Residence_Reith_Hall_kWh.csv"
    db.importCSVtoMongoDB(filename,'Reith','sc3', {'timestamp':'ValueTimestamp','value1':'WITS_PEC_Residence_Reith_Hall_kWh','kwh':True,'kvarh':False,'update':True})

    #EOH res 1
    #initial
    filename = "C:/Users/7240/Desktop/Design - software engineering/webaPP/StitchedData/WITS_WBS_EOH_Residence_1_kVarh/WITS_WBS_EOH_Residence_1_kVarh.csv"
    db.importCSVtoMongoDB(filename,'EOH-Res-1','sc3', {'timestamp':'ValueTimestamp','value1':'WITS_WBS_EOH_Residence_1_kVarh', 'value2':None,'kwh':False,'kvarh':True,'update':False})
    
    #update
    filename = "C:/Users/7240/Desktop/Design - software engineering/webaPP/StitchedData/WITS_WBS_EOH_Residence_1_kWh/WITS_WBS_EOH_Residence_1_kWh.csv"
    db.importCSVtoMongoDB(filename,'EOH-Res-1','sc3', {'timestamp':'ValueTimestamp','value1':'WITS_WBS_EOH_Residence_1_kWh','kwh':True,'kvarh':False,'update':True})
    
    #EOH res 2
    #initial
    filename = "C:/Users/7240/Desktop/Design - software engineering/webaPP/StitchedData/WITS_WBS_EOH_Residence_2_kVarh/WITS_WBS_EOH_Residence_2_kVarh.csv"
    db.importCSVtoMongoDB(filename,'EOH-Res-2','sc3', {'timestamp':'ValueTimestamp','value1':'WITS_WBS_EOH_Residence_2_kVarh', 'value2':None,'kwh':False,'kvarh':True,'update':False})
    
    #update
    filename = "C:/Users/7240/Desktop/Design - software engineering/webaPP/StitchedData/WITS_WBS_EOH_Residence_2_kWh/WITS_WBS_EOH_Residence_2_kWh.csv"
    db.importCSVtoMongoDB(filename,'EOH-Res-2','sc3', {'timestamp':'ValueTimestamp','value1':'WITS_WBS_EOH_Residence_2_kWh','kwh':True,'kvarh':False,'update':True})
    
    #Partown Village
    #initial
    filename = "C:/Users/7240/Desktop/Design - software engineering/webaPP/StitchedData/WITS_WBS_Parktown_Village_kVarh/WITS_WBS_Parktown_Village_kVarh.csv"
    db.importCSVtoMongoDB(filename,'Parktown-Village','sc3', {'timestamp':'ValueTimestamp','value1':'WITS_WBS_Parktown_Village_kVarh', 'value2':None,'kwh':False,'kvarh':True,'update':False})
    
    #update
    filename = "C:/Users/7240/Desktop/Design - software engineering/webaPP/StitchedData/WITS_WBS_Parktown_Village_kWh/WITS_WBS_Parktown_Village_kWh.csv"
    db.importCSVtoMongoDB(filename,'Parktown-village','sc3', {'timestamp':'ValueTimestamp','value1':'WITS_WBS_Parktown_Village_kWh','kwh':True,'kvarh':False,'update':True})
    
    #WC campus Student village unit A
    #initial
    filename = "C:/Users/7240/Desktop/Design - software engineering/webaPP/StitchedData/WITS_WC_Stdnts_Village_Unit_A_kVarh/WITS_WC_Stdnts_Village_Unit_A_kVarh.csv"
    db.importCSVtoMongoDB(filename,'WC-student-village-unit-A','sc3', {'timestamp':'ValueTimestamp','value1':'WITS_WC_Stdnts_Village_Unit_A_kVarh', 'value2':None,'kwh':False,'kvarh':True,'update':False})
    
    #update
    filename = "C:/Users/7240/Desktop/Design - software engineering/webaPP/StitchedData/WITS_WC_Stdnts_Village_Unit_A_kWh/WITS_WC_Stdnts_Village_Unit_A_kWh.csv"
    db.importCSVtoMongoDB(filename,'WC-student-village-unit-B','sc3', {'timestamp':'ValueTimestamp','value1':'WITS_WC_Stdnts_Village_Unit_A_kWh','kwh':True,'kvarh':False,'update':True})
    
    #WC campus Student village unit B
    #initial
    filename = "C:/Users/7240/Desktop/Design - software engineering/webaPP/StitchedData/WITS_WC_Stdnts_Village_Unit_B_kVarh/WITS_WC_Stdnts_Village_Unit_B_kVarh.csv"
    db.importCSVtoMongoDB(filename,'WC-student-village-unit-B','sc3', {'timestamp':'ValueTimestamp','value1':'WITS_WC_Stdnts_Village_Unit_B_kVarh', 'value2':None,'kwh':False,'kvarh':True,'update':False})
    
    #update
    filename = "C:/Users/7240/Desktop/Design - software engineering/webaPP/StitchedData/WITS_WC_Stdnts_Village_Unit_B_kWh/WITS_WC_Stdnts_Village_Unit_B_kWh.csv"
    db.importCSVtoMongoDB(filename,'WC-student-village-unit-B','sc3', {'timestamp':'ValueTimestamp','value1':'WITS_WC_Stdnts_Village_Unit_B_kWh','kwh':True,'kvarh':False,'update':True})
    
    #WC campus Student village unit C
    #initial
    filename = "C:/Users/7240/Desktop/Design - software engineering/webaPP/StitchedData/WITS_WC_Stdnts_Village_Unit_C_kVarh/WITS_WC_Stdnts_Village_Unit_C_kVarh.csv"
    db.importCSVtoMongoDB(filename,'WC-student-village-unit-C','sc3', {'timestamp':'ValueTimestamp','value1':'WITS_WC_Stdnts_Village_Unit_C_kVarh', 'value2':None,'kwh':False,'kvarh':True,'update':False})
    
    #update
    filename = "C:/Users/7240/Desktop/Design - software engineering/webaPP/StitchedData/WITS_WC_Stdnts_Village_Unit_C_kWh/WITS_WC_Stdnts_Village_Unit_C_kWh.csv"
    db.importCSVtoMongoDB(filename,'WC-student-village-unit-C','sc3', {'timestamp':'ValueTimestamp','value1':'WITS_WC_Stdnts_Village_Unit_C_kWh','kwh':True,'kvarh':False,'update':True})

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    #db.importCSVtoMongoDB(filename,'Jubilee','sc3', {'timestamp':'ValueTimestamp','value1':'WITS_3_Jubilee_Road_kWh','kwh':True,'kvarh':False,'update':True})
    print(f"no objects  { TimeSeriesDataModel.objects().count()}")

    app.run(debug = True)