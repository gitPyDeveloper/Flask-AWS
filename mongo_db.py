from pymongo import *
import datetime
from bson.objectid import ObjectId

import sqlite3

import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


#db.dropDatabase()
#db.COLLECTION_NAME.drop()
#show dbs
#use CRT
#use TickerCollection
#db.COLLECTION_NAME.remove({  'title'  :  'MongoDB Overview'  })


#The save() method replaces the existing document with the new document passed in the save() method.
#db.COLLECTION_NAME.save({_id:ObjectId(),NEW_DATA})
#db.tutorialspoint.insert({"name" : "tutorialspoint"})
#db.COLLECTION_NAME.update(SELECTION_CRITERIA, UPDATED_DATA,{multi:true})
#db.COLLECTION_NAME.update(    {'title':'MongoDB Overview'},
#                               { "$set"    :    { 'title'  :  'New MongoDB Tutorial'  }},
#                                {multi:true}    )



#db.createCollection(name, options) - Specify options about memory size and indexing

#1 ascending , -1 descending
#db.COLLECTION_NAME.find({ "db_value" : {"$lte" : 50} }).limit(1).skip(1).sort({"db_value":-1}).pretty()
#db.COLLECTION_NAME.find({ "$and" : [ {key1: value1}, {key2:value2} ] }).pretty()

#db.COLLECTION_NAME.find({ "db_value" : {"$gt" : 10}, 
#                            "$or"    : [  {"by"   : "tutorials point"},
#                                          {"title": "MongoDB Overview"}]    }).pretty()


#Indexes are special data structures, that store a small portion of the data set in an easy-to-traverse form
#db.COLLECTION_NAME.ensureIndex({"title":1})

# Aggregate Functions
#db.COLLECTION_NAME.aggregate(AGGREGATE_OPERATION)
#db.mycol.aggregate([{    "$group" : 
#                                    {  _id           : "$by_user", 
#                                        num_tutorial : { "$avg" : "$likes" }
#                                    }
#                    }])

class cl_mongo_DB():
    
    C_HOST_NAME = "localhost"
    C_USER_NAME = "root"
    C_USER_PASSWORD = ""
    C_DB_NAME = "CRT"      
    C_COLLECT_NAME = "TickerCollection"      
    
    
    def __init__(self):
        client = MongoClient(cl_mongo_DB.C_HOST_NAME, 27017)
        
        # DATABASE NAME
        db = client.CRT
        # Collection Name
        self.collection = db.TickerCollection


    def updateTicker(self, in_ticker, in_field, in_source, in_date, in_value):
        
        UPDATE_FLAG = -1
        KEY_FLAG = False 
        
        key_dict = {"ticker" : in_ticker,
                    "field"  : in_field,
                    "source" : in_source}
        
        query_ = self.collection.find(key_dict) 
        TIME_NOW = datetime.datetime.now()
        
        for record in query_:
            KEY_FLAG = True
            break     
        
        # if record present , update
        if KEY_FLAG == True:
            
            key_dict = {"ticker" : in_ticker,
                        "field"  : in_field,
                        "source" : in_source,
                        'value_dict.db_date': in_date}
            
            data_dict = { '$set' : {'value_dict.$.db_value'   : in_value,
                                    'value_dict.$.last_modify': TIME_NOW}}
            query_ = self.collection.update(key_dict, data_dict)
        
            if query_['updatedExisting'] == False:

                key_dict = {"ticker" : in_ticker,
                            "field"  : in_field,
                            "source" : in_source}
                        
                data_dict = {'$push' : 
                            {'value_dict'   : {
                                    '$each' : [ {'db_value'   : in_value ,
                                                 'db_date'    : in_date,
                                                 'last_modify': TIME_NOW}]
                                            }
                            }
                        }            
            
                query_ = self.collection.update(key_dict, data_dict)
                
            if query_['updatedExisting'] == True:
                UPDATE_FLAG = 1
        
        # if no record found, insert new records
        else:
            
            data_dict = { "ticker" : in_ticker,
                          "field"  : in_field,
                          "source" : in_source,
                          "create_date" : TIME_NOW,
                          "value_dict" : [{'db_date'    : in_date,
                                           'db_value'   : in_value,
                                           'last_modify': TIME_NOW }]                                  
                        }
            
            query_ = self.collection.insert(data_dict).pretty()           
            UPDATE_FLAG = 0
        
        if UPDATE_FLAG == -1:
            logging.debug('Unable to update the record. Please check')
          
        return UPDATE_FLAG




    def findRecord(self,key_dict):
        
        KEY_FLAG    = False 
        record_list = []
        query_      = self.collection.find(key_dict)
        
        for row in query_:
            record_list.append(row)
            
        return record_list
        
        

    def updateRecord(self,key_dict,data_dict):
        pass



in_ticker = 'C_USA_IND'
in_field = 'EXPORT'
in_source = 'USDA'
in_date = '2017-11-30' 
in_value = 99

key_dict = {'field':'EXPORT'}

xObject = cl_mongo_DB()
record_list = xObject.findRecord(key_dict)


for i in range(0,len(record_list)):
    
    for key,value in record_list[i].iteritems():
        print key,value
        
    print '-----------------------------------------------------------'
#xObject.updateTicker(in_ticker, in_field, in_source, in_date, in_value)


        
        
#db.users.find({name: /a/})  //like '%a%'
#db.users.find({name: /^pa/}) //like 'pa%' 
#db.users.find({name: /ro$/}) //like '%ro'    
