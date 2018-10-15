import mongoengine
import datetime

class Query(mongoengine.EmbeddedDocument):
    buildingName = mongoengine.StringField(required = True)
    dataLogger = mongoengine.StringField(required = True)
    startDate = mongoengine.DateTimeField(required  = True)
    endDate = mongoengine.DateTimeField(required  = True)

class Widget(mongoengine.EmbeddedDocument):
    id = mongoengine.IntField(default = 3) #format (YYYYMMMDDXXX)
    name = mongoengine.StringField()
    typeOfGraph = mongoengine.StringField(required=True)
    dateCreated = mongoengine.DateTimeField(default = datetime.datetime.now())
    url = mongoengine.URLField(required=True)
    priority = mongoengine.IntField(default = 3)
    options = mongoengine.ListField(mongoengine.EmbeddedDocumentField(Query))
    meta = {
        'ordering':['-priority']
    }

class WidgetsModel(mongoengine.Document):
    userEmail = mongoengine.StringField(required=True)
    widgets = mongoengine.ListField(mongoengine.EmbeddedDocumentField(Widget))
    meta = {
        'db_alias': 'core',
        'collection': 'Widgets',

        'ordering':['-_id']
    }


