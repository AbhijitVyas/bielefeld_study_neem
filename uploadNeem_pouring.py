#!/usr/bin/env python
import os
import sys
from pymongo import MongoClient
from datetime import datetime
import subprocess

MONGO_HOST = 'neem-3.informatik.uni-bremen.de'
MONGO_PORT = 28015
MONGO_DB = 'admin'
MONGO_USER = 'PLEASE ASK NEEM Hub Manager for user'
MONGO_PASS = 'PLEASE ASK NEEM Hub Manager for Pass'
FROM_PREFIX = '5fd78ff7525332aa81235858'
# Alternativly fix path here
PATH_TO_NEEM = '/home/user/catkin_init_ws/src/bielefeld_study_neem/NEEMs/PouringNEEMs'

# remote mongo client connection
# uri = "mongodb://user:password@example.com/?authSource=the_database&authMechanism=SCRAM-SHA-256"
uri = "mongodb://"+ MONGO_USER + ":" + MONGO_PASS + @neem-3.informatik.uni-bremen.de:28015/?authSource=admin&authMechanism=SCRAM-SHA-1"

connection = MongoClient(uri)
mongoDbClient = connection['neems']
#mongoDbClient.authenticate(MONGO_USER, MONGO_PASS, source='admin')




# Fill the meta data
metaCol = mongoDbClient['meta']

currentTime = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00");

mydict = {
    "description" : "The pouring neem in IAI apartment lab performed by human in Uneal engine.",
    "image" : "https://raw.githubusercontent.com/AbhijitVyas/Images/master/Pouring_apartment.png",
    "repo" : "pouring-unreal-vr-demonstration",
    "model_version" : "0.1",
    "keywords" : [ 
        "pouring demonstration"
    ],
    "projects" : [ 
        {
            "url" : "https://ease-crc.org/",
            "name" : "EASE"
        }
    ],
    "visibility": True,
    "name" : "Pouring VR demonstration in new apartment lab",
    "url" : "https://neemgit.informatik.uni-bremen.de/neems/pouring-simulation-unreal",
    "created_at" : currentTime,
    "created_by" : "Abhijit Vyas",
    "environment" : "Apartment",
    "mail" : "avyas@uni-bremen.de"
}
 


insertion_obj = metaCol.insert_one(mydict)
print(insertion_obj.inserted_id)

# remember the new prefix
TO_PREFIX = str(insertion_obj.inserted_id)
print(TO_PREFIX)

# Upload neem
cmd_prefix = "mongorestore --host=neem-3.informatik.uni-bremen.de --port=28015 --username= --password= --authenticationDatabase=admin -d neems -c "

triples_cmd = cmd_prefix + TO_PREFIX + "_triples " + PATH_TO_NEEM + "/triples/roslog/triples.bson"
#inferred_cmd = cmd_prefix + TO_PREFIX + "_inferred " + PATH_TO_NEEM + "/Pouring_inferred/roslog/Pouring_inferred.bson"
#one_cmd = cmd_prefix + "one" + PATH_TO_NEEM + "/one/roslog/one.bson"
annotations_cmd = cmd_prefix + TO_PREFIX + "_annotations " + PATH_TO_NEEM + "/annotations/roslog/annotations.bson"
tf_cmd = cmd_prefix + TO_PREFIX + "_tf " + PATH_TO_NEEM + "/tf/roslog/tf.bson"

print(subprocess.check_output(triples_cmd,stderr=subprocess.STDOUT,shell=True))
print(subprocess.check_output(annotations_cmd,stderr=subprocess.STDOUT,shell=True))
print(subprocess.check_output(tf_cmd,stderr=subprocess.STDOUT,shell=True))

# copy indices
for name, index_info in mongoDbClient[FROM_PREFIX + '_triples'].index_information().items():
    print(name)
    mongoDbClient[TO_PREFIX + '_triples'].create_index(keys=index_info['key'], name=name)


#for name, index_info in mongoDbClient[FROM_PREFIX + '_inferred'].index_information().items():
#   print(name)
#   mongoDbClient[TO_PREFIX + '_inferred'].create_index(keys=index_info['key'], name=name)

#for name, index_info in mongoDbClient[FROM_PREFIX + 'one'].index_information().items():
#    print(name)
#    mongoDbClient[TO_PREFIX + 'one'].create_index(keys=index_info['key'], name=name)


for name, index_info in mongoDbClient[FROM_PREFIX + '_annotations'].index_information().items():
    print(name)
    mongoDbClient[TO_PREFIX + '_annotations'].create_index(keys=index_info['key'], name=name)

for name, index_info in mongoDbClient[FROM_PREFIX + '_tf'].index_information().items():
    print(name)
    mongoDbClient[TO_PREFIX + '_tf'].create_index(keys=index_info['key'], name=name)
