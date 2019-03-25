# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 12:57:19 2019

@author: Christopher Green
"""

import psycopg2
import sys
import os
import fs
from fs import open_fs
import gnupg
#import config
import subprocess
import os
import shutil
import tarfile
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Search, UpdateByQuery, Text, Date, Integer , Document, Index, DocType
from kafka import KafkaConsumer
from kafka import KafkaProducer
import signal
import json

class kafka_consumer1:
#clear the key from list after running
    #all information comes in as bytes and must be converted
    
    def bytesToDictionary(b_array):
         try:
             d = dict(toks.split(":") for toks in b_array.decode("utf-8").split(",") if toks)
             #print("Convert")
             return d
         except ValueError as e:
             print(e)
    consumer = KafkaConsumer('test',consumer_timeout_ms=10000)
    #print(type(consumer))
    filepath = []
    key_uuid = []
    filename = []
    worker_uuid = []
    for msg in consumer:
        print(msg)
        d = bytesToDictionary(msg.value)
        s = msg.value.decode("utf-8")
        if 'key_uuid' in s:
            key_uuid.append(d['key_uuid'])
        if 'filepath' in s:
            filepath.append(d['filepath'])
        if 'filename' in s:
            filename.append(d['filename'])
        if 'worker_uuid' in s:
            worker_uuid.append(d['worker_uuid'])
            break
        print(filepath)
        print(filename)
        print(key_uuid)
    filepath = ",".join(filepath)
    filename = ",".join(filename)
    key_uuid = [int(i) for i in key_uuid]
    worker_uuid = ",".join(worker_uuid)
    consumer.close()
        #print(d)
kafka_consumer1()

class postgres_UUID:
    def post_connect():
            conn = psycopg2.connect(database="dvdrental", user = "postgres", password = "pass123", host = "127.0.0.1", port = "5432")

    def querying_data():
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM keys WHERE key_uuid = ANY(%s);", (kafka_consumer1.key_uuid,))
        rows = cur.fetchall()
        public_keyring.clear()
        location_encryped_file.clear()
        passphrase = 'loopyloom.'

        for row in rows:
           public_keyring=(row[0])
        #   location_encryped_file = (row[1])
        #   passphrase=(row[1])
        #   print "SECRET-KEY = ", row[3], 
        #   print "PRIVATE-KEY = ",row [4], "\n"
        print ("Operation done successfully");
        conn.close()

postgres_UUID()

class Decryption:
    if os.path.exists('/home/cgreen/Decryption/Encrypted'):
        print("Decrypted directory already exists")
    else:
        os.mkdir(u"'/home/cgreen/Decryption/Encrypted'")
        print("Created decrypted directory")

    os.chdir('/home/cgreen/Decryption/Encrypted')

        #be sure location of file and keys
    gpg = gnupg.GPG(gnupghome=(str(kafka_consumer1.filepath)))
    #gpg = gnupg.GPG(homedir=(str(kafka_consumer1.filepath)))
                                    #keyring= (str(public_keyring)),
                                    #secring= (str(secret_keyring)))

    #secret key needs to be included here
    #home_fs = open_fs(".")
    #create directory
    files_dir = []
    files_dir_clean = []

    #create seperate path for decryped files to be seperate from encryped files
    if os.path.exists("/home/cgreen/Decryption/decrypted/"):
        print("Decrypted directory already exists")
    else:
        os.mkdir(u"/home/cgreen/Decryption/decrypted/")
        print("Created decrypted directory")
        
    #add files to list (list the uuid for the folder to pick) name of file from kafka
    files = [f for f in os.listdir("/home/cgreen/Decryption/Encrypted") if os.path.isfile(f)]
    for f in files:
        files_dir.append(f)

    #remove the .gpu from the file 
    for x in files_dir:
        length = len(x)
        endLoc = length - 4
        clean_file = x[0:endLoc]
        files_dir_clean.append(clean_file)


    #decryped files.  Be sure the passphrase is properly named. 
    for x in files_dir:
            with open(str(kafka_consumer1.filepath) + "/" + str(kafka_consumer1.filename), 'rb') as f:
                    status = gpg.decrypt_file(f, passphrase= str(postgres_UUID.passphrase), output=files_dir_clean[files_dir.index(x)])
                      #greenzone1
    print( 'ok: ', status.ok)
    print( 'status: ', status.status)
    print( 'stderr: ', status.stderr)
    #os.rename(files_dir_clean[files_dir.index(x)], "decrypted/" + files_dir_clean[files_dir.index(x)])
           
    print("Decryption Complete")
    
    files = [f for f in os.listdir("/home/cgreen/Decryption/Encrypted") if os.path.isfile(f)]
    new_dest = '/home/cgreen/Decryption/decrypted/'
    for f in files:
        if f.endswith('gpg'):
             os.remove(f)
    files = [f for f in os.listdir("/home/cgreen/Decryption/Encrypted") if os.path.isfile(f)]
    for f in files:
        shutil.move(f, new_dest)

    
Decryption()            
    
#be sure you point the unzip/untar to the decrypted folder
def unzip():
    current_wkd = os.getcwd()
    pointed_dir = "/home/cgreen/Decryption/decrypted/"
    try:
        for dirpath, dir, files in os.walk(top=pointed_dir):
            for file in files:
                tar = tarfile.open(os.path.join(dirpath, file))
                tar.extractall(path=pointed_dir)
                tar.close()
    except tarfile.ReadError:
        print("No files to untar, moving on.")
unzip()

files_b4_cleaning = [os.listdir("/home/cgreen/Decryption/decrypted/")]

class malware_scanner:
    clamscan_virus_dir = []
    sophos_virus_dir = []
    clean_files = []
    changes = []
    def malware_location():    
        #create seperate path for files to be seperated
        if os.path.exists("//home//cgreen//Decryption//Json//virus"):
            pass
        else:
            os.mkdir(u"//home//cgreen//Decryption//Json//virus")
        if os.path.exists("//home//cgreen//Decryption//Json//shared-drive1"):
            pass
        else:
            os.mkdir(u"//home//cgreen//Decryption//Json//shared-drive1")    
        #location of files and desingated folders
        source = '//home//cgreen//Decryption//Json'
        dest1 = "//home//cgreen//Decryption//Json//shared-drive1"
        dest3 = "//home//cgreen//Decryption//Json//virus"
        
        files = os.listdir(source)
    def malware_bash():
        #Run command on command line to start the first malware scanner
        bashCommand = "clamscan -r --move=//home//cgreen//Decryption//Json//virus //home//cgreen//Decryption//decrypted//"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        for root, dirs, files in os.walk("//home//cgreen//Decryption//Json//virus"):
              for file in files:
                clamscan_virus_dir.append(file)
        
        bashCommand2 = "sweep /home/cgreen/decrypted --quarantine=//home//cgreen//Decryption//Json//virus" 
        process = subprocess.Popen(bashCommand2.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        for root, dirs, files in os.walk("/virus"):
            for file in files:       
                changes.append(file)
        sophos_virus_dir.append(list(set(changes) - set(clamscan_virus_dir)))
    malware_bash()
malware_scanner()
        #the infected files are alread in quarantine we only need to move the original files 
clean_files = os.listdir("//home//cgreen//Decryption//decrypted//")

def zipit():  
    base_path = "//home//cgreen//Decryption//decrypted//"
    next_path = "//home//cgreen//Decryption//Json//shared-drive1//"
    try:
        for dirpath, dir, files in os.walk(top=base_path):
            for file in files:#, root, dirs:    
                #tar = tarfile.open(os.path.join(dirpath, file))
                tar = tarfile.open(next_path +"/"+ kafka_consumer1.filename + ".tar.gz", "w:gz")
                #tar = tarfile.open("//home//cgreen//Decryption//Json//shared-drive1//" + "sample.tar.gz", "w:gz")
                tar.add(base_path)
                tar.close()
                break
                os.rmdir("//home//cgreen//Decryption//decrypted//")
    except FileNotFoundError as u:
        print (u)
zipit()                
    
if clean_files==files_b4_cleaning:
    file_result = "No malware found. files ziped and sent to shared directory"
else:
    file_result = "Malware found. Some of your files have been Quarantined"



update_body = {
    "query": {
        "constant_score" : {
            "filter" : {
                 "bool" : {
                    "must" : [
                        { "terms" : { "tags" : kafka_consumer1.key_uuid } }, 
                        { "terms" : { "location" : file_result } },
                        { "terms" : { "worker_uuid" : kafka_consumer1.worker_uuid } },
                        { "terms" : { "new filename" : kafka_consumer1.filename } },
                    ]
                }
            }
        }
    }
}


class Kafka_Producer:

    
    # string with encoding 'utf-8'
    json_string = json.dumps(update_body)
    fin_result = bytes(json_string, 'utf-8')
    
    #other producers below
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    #producer2 = KafkaProducer(bootstrap_servers='localhost:9093')
    #producer3 = KafkaProducer(bootstrap_servers='localhost:9094')
    bracket = "{"
    for _ in range(1):
        print(producer.send('test', bytes(fin_result))) 
          
Kafka_Producer()   
 

class ES_Lead(Document):
    lead_UUID = Text()
    lead_creation_date = Date()
    lead_creation_user_UUID = Text()
    Sophos_detected_malware = Text()
    ClamAV_detected_malware = Text()
    Clean_files = Text()
    Location_malware_files = Text()
    location_clean_files = Text()
    lead_creation_user_UUID = Text()

    class Index:
        # Name of the ES Index
        name = "leads10"

class ES_LookUp_Writer:
    def __init__(self):
        self.create_lookup()

     #Build the connection
     #Make the connection to Elastic Search
    def create_connection(self):
        self.conn = connections.create_connection(
                                    hosts=['localhost'])

     #Logic: IF the lookUp name does NOT exist create the lookup and add the values provided
     #       ELSE pass the record to the update lookup function.
    def create_lookup(self):
        self.create_connection()
        result = ES_Lead(lead_UUID=kafka_consumer1.key_uuid , Sophos_detected_malware=malware_scanner.sophos_virus_dir , ClamAV_detected_malware = malware_scanner.clamscan_virus_dir , Clean_files = malware_scanner.clean_files , Location_malware_files="Quarantined", location_clean_files="Shared-Drive1", lead_creation_user_UUID=kafka_consumer1.worker_uuid).save()
       
ES_LookUp_Writer()


