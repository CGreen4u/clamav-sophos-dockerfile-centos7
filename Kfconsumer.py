from kafka import KafkaConsumer
import sys
import threading
from threading import Thread
from KfElasticsearch import ES_Lead, ES_LookUp_Writer, Error_ES_LookUp_Writer

class kafka_consumer1:
    def __init__(self):
        self.key_uuid = None
        self.worker_uuid = None
        self.filename = None
        self.filepath = None
        self.missing_element = None
    #clear the key from list after running
    #all information comes in as bytes and must be converted
    def getUUIDS(self):
        uuids = [self.key_uuid]
        return uuids
    def setUUIDS(self, key_uuid):
        self.key_uuid = key_uuid
    def getFILE(self):
        file = [self.filename, self.filepath, self.worker_uuid, self.missing_element]
        return file
    def setFILE(self, filename, filepath, worker_uuid, missing_element):
        self.filename = filename
        self.filepath = filepath
        self.worker_uuid = worker_uuid
        self.missing_element = missing_element
    def bytesToDictionary(self, b_array):
         try:
             d = dict(toks.split(":") for toks in b_array.decode("utf-8").split(",") if toks)
             #print("Convert")
             return d
         except (ValueError, KeyError, TypeError) as e:
             print(e)
    def CheckMsg(self):
        #the consumer is on a timer. The program needs to shut off for the process to continue. The code has two methods of disconnect
        #one method being a timer and the other being the fulfillment of the list items. 
        consumer = KafkaConsumer('test',consumer_timeout_ms=10000)
        #print(type(consumer))
        filepath = []
        key_uuid = []
        filename = []
        worker_uuid = []
        missing_element = ''
        for msg in consumer:
            print(msg)
            #the message come in with specifics listed. Here we take those specifics and pull the needed files after converting.
            d = self.bytesToDictionary(msg.value)
            s = msg.value.decode("utf-8")
            if 'key_uuid' in s:
                key_uuid.append(d['key_uuid'])
            if 'filepath' in s:
                filepath.append(d['filepath'])
            if 'filename' in s:
                filename.append(d['filename'])
            if 'worker_uuid' in s:
                worker_uuid.append(d['worker_uuid'])
                #break   
            print(filepath)
            print(filename)
            print(key_uuid)
        consumer.close()
        while True:
            if not filepath: #, key_uuid, filename, worker_uuid:
                missing_element='the filepath is missing from the Kafka message.'
                Error_ES_LookUp_Writer(missing_element)
                sys.exit(missing_element)
                break
            elif not key_uuid:
                missing_element='the key_uuid is missing from the kafka message.'
                Error_ES_LookUp_Writer(missing_element)
                sys.exit(missing_element)
                break
            elif not filename:
                missing_element='the filename is missing from the kafka message.'
                Error_ES_LookUp_Writer(missing_element)
                sys.exit(missing_element)
                break
            elif not worker_uuid:
                missing_element='the worker_uuid is missing from the kafka message.'
                Error_ES_LookUp_Writer(missing_element)
                sys.exit(missing_element)
                break
            else:
                break
        #the files need to be converted into different types as they are recieved as bytes.    
        filepath = ",".join(filepath)
        filename = ",".join(filename)
        key_uuid = [int(i) for i in key_uuid]
        worker_uuid = ",".join(worker_uuid)
        #consumer.close()
        self.setFILE(filename, filepath, worker_uuid, missing_element)
        self.setUUIDS(key_uuid)
        #fileInfo = [filename, filepath]
        return self.getFILE(), self.getUUIDS()
            #print(d)
   
#kafka_consumer1()

 