import mongoengine
import time
import dateutil
import pandas as pd
import json
import os
import hashlib
from passlib.hash import sha256_crypt
from mongoengine.queryset.visitor import Q
from mongoengine.queryset import QuerySet
from data.dataModel import *
from data.WidgetsModel import *
from bson.son import SON



class MongoDBmanager:
    def __init__(self, dbName: str):
        mongoengine.register_connection(alias='core', name=dbName)

       
    def addDocument(self,id: int, buildingName: str, dataLogger: str, location = {'Lon': None, 'Lat': None }):
        #does the document exist
        if (TimeSeriesDataModel.objects(_id = id,buildingName = buildingName,
                                      dataLogger=dataLogger).count() > 0):
            print("document exists")

        else:
            doc = TimeSeriesDataModel(_id = id, location = location ); #when adding embedded data add here 
            doc.buildingName = buildingName        #Dont use attribute instance
            doc.dataLogger = dataLogger
            doc.switch_collection(buildingName)
            doc.save()
            print("added doc")

    def addDataToDoc(self, id: int, buildingName: str, dataLogger: str, data: SON):
        collection = TimeSeriesDataModel.switch_collection(TimeSeriesDataModel(),buildingName)
        object = QuerySet(TimeSeriesDataModel,collection._get_collection())
        if (object.filter(Q(_id = id) & Q(buildingName = buildingName) &
                                      Q(dataLogger=dataLogger)).count() == 1): #only one document must exist
            print("document data exists")
            d1 = Data(timeStamp =data['timeStamp'], kvarh = data['kvarh'], kwh = data['kwh'])
            object(_id = id,buildingName = buildingName,
                                      dataLogger=dataLogger)\
                                .update(push__data=d1)
        else:
            self.addDocument(id,buildingName,dataLogger)
            self.addDataToDoc(id,buildingName,dataLogger,data)


    def updateDataInDoc(self, id: int, buildingName: str, dataLogger: str, data = {'kwh': False, 'kvarh':False, 'value': -1, 'timestamp': 0}):
        collection = TimeSeriesDataModel.switch_collection(TimeSeriesDataModel(),buildingName)
        object = QuerySet(TimeSeriesDataModel,collection._get_collection())
        iso = time.strptime(data['timestamp'], "%Y-%m-%d %H:%M")
     
        if (object.filter(Q(_id = id) & Q(buildingName = buildingName) & Q(dataLogger=dataLogger) & Q(data__timeStamp = datetime.datetime(iso.tm_year,iso.tm_mon, iso.tm_mday, iso.tm_hour, iso.tm_min,iso.tm_sec))).count() > 0):
            if data['kwh'] and not data['kvarh']:
                object.filter(Q(_id = id) & Q(buildingName = buildingName) & Q(dataLogger=dataLogger) & Q(data__timeStamp = datetime.datetime(iso.tm_year,iso.tm_mon, iso.tm_mday, iso.tm_hour, iso.tm_min,iso.tm_sec))).update(set__data__S__kwh = data['value'])
            if not data['kwh'] and data['kvarh']:
                object.filter(Q(_id = id) & Q(buildingName = buildingName) & Q(dataLogger=dataLogger) & Q(data__timeStamp = datetime.datetime(iso.tm_year,iso.tm_mon, iso.tm_mday, iso.tm_hour, iso.tm_min,iso.tm_sec))).update(set__data__S__kvarh = data['value'])
    



    def dateToID(self,date: str, fm = '/') -> int:
        ID = None
        dt = None
        if fm == '/':
            dt = time.strptime(date, "%Y/%m/%d %I:%M:%S %p")
        elif fm == '-':
            dt = time.strptime(date, "%Y-%m-%d %H:%M")
        ID = dt.tm_year*10000 + dt.tm_mon*100+dt.tm_mday
        print(ID)
        return ID

    def importCSVtoMongoDB(self,filepath: str, buildingName: str, dataLogger: str, options = {'timestamp':None,'value1': None, 'value2': None, 'kvarh':False, 'kwh':False, 'update':False}, recurssion= False):
       
        cdir = os.path.dirname(__file__)
        file_res = os.path.join(cdir, filepath)
        data = pd.read_csv(file_res)
        
        data  = data.drop(data[data[options['value1']] == -1].index)
      
        data_json = json.loads(data.to_json(orient='records'))
        tempTime = None
        dataObjs = []
        for point in data_json:
            id = self.dateToID(point[options['timestamp']] , '-')
            if options['update']:
                print(point[options['value1']])
                self.updateDataInDoc(id, buildingName, dataLogger, {'kwh': options['kwh'], 'kvarh': options['kvarh'], 'value': point[options['value1']], 'timestamp': point[options['timestamp']]})
            else:
                if options['kwh'] and options['kvarh']:
                    dataObjs=( {'timeStamp':point[options['timestamp']],
                                'kvarh': point[options['value1']],
                                'kwh': point[options['value2']]
                                })
                elif not options['kwh'] and options['kvarh']:
                    dataObjs=( {'timeStamp':point[options['timestamp']],
                                'kvarh': point[options['value1']],
                                'kwh': options['value2']
                                })
                elif options['kwh'] and not options['kvarh']:
                    dataObjs=( {'timeStamp':point[options['timestamp']],
                                'kvarh': options['value1'],
                                'kwh': point[options['value2']]
                                })
                self.addDataToDoc(id, buildingName, dataLogger, dataObjs)
                
    def fetchData(self, buildingName: str, startDateTime: str, endDateTime: str):
        collection = TimeSeriesDataModel.switch_collection(TimeSeriesDataModel(),buildingName)
        object = QuerySet(TimeSeriesDataModel,collection._get_collection())  
        
        
        iso = time.strptime(startDateTime, "%Y-%m-%d %H:%M")
        startDateTime = datetime.datetime(iso.tm_year,iso.tm_mon, iso.tm_mday, iso.tm_hour, iso.tm_min,iso.tm_sec)
        iso = time.strptime(endDateTime, "%Y-%m-%d %H:%M")
        endDateTime = datetime.datetime(iso.tm_year,iso.tm_mon, iso.tm_mday, iso.tm_hour, iso.tm_min,iso.tm_sec)
        
        results = object.aggregate(*[{'$match': { 'data.timeStamp' :
                                    {'$gte':startDateTime,
                                    '$lte':endDateTime}}}])
        res = []
        for doc in results:
            for data in doc['data']:
                if  data['timeStamp'] >= startDateTime and data['timeStamp'] <= endDateTime:
                    res.append(data)

        return res
    #To implement
    def fetchBuildings(self):
        db = mongoengine.connection.get_db('core')
        res = []
        for c in db.list_collection_names():
            if not (c == 'Widgets' or c == 'Users'):
                res.append(c)
 
        return res

    def getWorstBestBuildings(self):
        buildings = self.fetchBuildings()

        res = []
        for b in buildings:
            #data = self.fetchData(b,datetime.datetime.today().strftime('%Y-%m-%d') +' 00:00', datetime.datetime.today().strftime('%Y-%m-%d %H:%M'))
            data = self.fetchData(b,'2018-07-03 00:00', '2018-07-04 00:00')
            dataString = json.dumps(data, default=str)
            a = pd.read_json(dataString)
            if len(a.index) == 0:
                continue
            newA = a.drop(a[a['kwh'] == -1].index)
            avg = newA['kwh'].mean()
            res.append({'building':b,'average':round(avg,2)})

        if len(res) == 0:
            return {'Worst': [], 'Best': []}

        
        y = json.dumps(res)
        a = pd.read_json(y)
        
        orderedData = a.sort_values('average')

        jsonObj = {'Worst': [], 'Best': []}
        if len(orderedData.index) <= 6:
            for index in range(0,len(orderedData.index)):
                if(index < 3):
                    jsonObj['Worst'].append(orderedData.iloc[index].to_dict())

                else:
                    jsonObj['Best'].append(orderedData.iloc[index].to_dict())
        else:
            for index in range(0,3):
                jsonObj['Best'].append(orderedData.iloc[index].to_dict())

            for index in range(len(orderedData.index) - 1,len(orderedData.index) - 4,-1):
                jsonObj['Worst'].append(orderedData.iloc[index].to_dict())

        return jsonObj


    def fetchUserWidgets(emailAddress: str):
        #return all user widgets
        pass

    def createWidget(emailAddress: str, widget: Widget):
        #Queries database then appends widget
        pass

    def updateWidget(emailAddress: str, id: int, obj = {'typeOfGraph':None, 'url':None, 'priority':3, 'buildingName': None, 'dataLogger':None, 'startSDate':None, 'endDate':None}):
        #Query for widget
        #update attibutes
        pass

    def deleteWidget(emailAddress: str, id: int):
        #query then delete
        pass
    def verifyUser(username: str, password:str):
        #Query DB and check user existence
        passwordHash = sha256_crypt.encrypt(password)
        pass

    def createNewPassword(emailAddress: str):
        #generate a random string and send to user
        #update password hash in DB
        pass

    def changePassword(username: str, oldPassword:str, newPassWord: str):
        #verify user first
        #set new password
        pass

    def checkUser():
        pass