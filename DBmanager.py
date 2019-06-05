import pymongo
from Entities import Target,Adversary,Event
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["cybrain"]
events = db['events']

def getTheLastEvent(filter:dict={}):
    """return the last reported event (by filter)"""
    return events.find(filter).sort(key_or_list='event_id',direction=-1).limit(1)[0]

def getAllEvents(filter:dict={}):
    """return all the reported event (by filter)"""
    return events.find(filter).sort(key_or_list='event_id', direction=1)

def updateEvent(event_id:int, values:dict):
    """updating event fields by the event id
        return the event after the update"""
    after_event = events.find_one_and_update({'event_id':event_id},{'$set':values},return_document=pymongo.ReturnDocument.BEFORE)
    return after_event

def insertNewEvent(new_event:Event):
    """insert new event into data base
        return if the event was insert successfully"""
    new_event['event_id'] = getNewId()
    inserted = events.insert_one(new_event.toDict())
    return  inserted.acknowledged

def getNewId():
    last_event = getTheLastEvent()
    return last_event['event_id']+1


#adversary = Adversary(organization='לא ידוע')
for i,event in enumerate(getAllEvents({'status':'Report'})):
    print(i+1,')',event)