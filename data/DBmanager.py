import mongoengine
from data.dataModel import *
from bson.son import SON

class MongoDBmanager:
    def __init__(self, dbName: str):
        mongoengine.register_connection(alias='core', name=dbName)

       
    def addDocument(self,id: int, buildingName: str, dataLogger: str, location = {'Lon': 1.0, 'Lat': 1.0 }):
        #does the document exist
        if (TimeSeriesDataModel.objects(_id = id,buildingName = buildingName,
                                      dataLogger=dataLogger).count() > 0):
            print("document exists")

        else:
            doc = TimeSeriesDataModel(_id = id ); #when adding embedded data add here 
            doc.buildingName = buildingName        #Dont use attribute instance
            doc.dataLogger = dataLogger
            doc.save()
            print("added doc")

    def addDataToDoc(self,id: int, buildingName: str, dataLogger: str, data: SON):

        if (TimeSeriesDataModel.objects(_id = id,buildingName = buildingName,
                                      dataLogger=dataLogger).count() == 1): #only one document must exist
            print("document exists")
            d1 = Data(timeStamp =data['timeStamp'], kvarh = data['kvarh'], kwh = data['kwh'])
            TimeSeriesDataModel.objects(_id = id,buildingName = buildingName,
                                      dataLogger=dataLogger)\
                                .update(push__data=d1)