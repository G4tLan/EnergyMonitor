import mongoengine
import time
import pandas as pd
import json
import os
from mongoengine.queryset.visitor import Q
from mongoengine.queryset import QuerySet
from data.dataModel import *
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

    def addDataToDoc(self, buildingName: str, dataLogger: str, data: SON):
        collection = TimeSeriesDataModel.switch_collection(TimeSeriesDataModel(),buildingName)
        object = QuerySet(TimeSeriesDataModel,collection._get_collection())
        
        if (object.filter(Q(_id = self.dateToID(data['timeStamp'])) & Q(buildingName = buildingName) &
                                      Q(dataLogger=dataLogger)).count() == 1): #only one document must exist
            print("document data exists")
            d1 = Data(timeStamp =data['timeStamp'], kvarh = data['kvarh'], kwh = data['kwh'])
            object(_id = self.dateToID(data['timeStamp']),buildingName = buildingName,
                                      dataLogger=dataLogger)\
                                .update(push__data=d1)
        else:
            self.addDocument(self.dateToID(data['timeStamp']),buildingName,dataLogger)
            self.addDataToDoc(buildingName,dataLogger,data)

    def dateToID(self,date: str) -> int:
        ID = None
        dt = time.strptime(date, "%Y/%m/%d %I:%M:%S %p")
        ID = dt.tm_year*10000 + dt.tm_mon*100+dt.tm_mday
        print(ID)
        return ID

    def importCSVtoMongoDB(self,filepath: str):
        cdir = os.path.dirname(__file__)
        file_res = os.path.join(cdir, filepath)
        data = pd.read_csv(file_res)
        data_json = json.loads(data.to_json(orient='records'))