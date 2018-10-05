import mongoengine
import datetime

class Location(mongoengine.EmbeddedDocument):
    Lon = mongoengine.FloatField()
    Lat = mongoengine.FloatField()


class Data(mongoengine.EmbeddedDocument):
    timeStamp = mongoengine.DateTimeField()
    kvarh = mongoengine.FloatField()  #reactive power
    kwh = mongoengine.FloatField()  #real power

    meta = {
        'ordering': ['-timeStamp']
    }
  

class TimeSeriesDataModel(mongoengine.Document):
    _id = mongoengine.IntField(required=True) #format (YYYYMMDD)
    buildingName = mongoengine.StringField(required=True)  #name of the building
    dataLogger = mongoengine.StringField(required=True)    # name of the data logger used
    data = mongoengine.ListField(mongoengine.EmbeddedDocumentField(Data))
    location = mongoengine.EmbeddedDocumentField(Location)

    meta = {
        'db_alias': 'core',
        'collection': 'default',

        'ordering':['-_id']
    }




