from elasticsearch import Elasticsearch
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Search, UpdateByQuery, Text, Date, Integer , Document, Index, DocType
 

class ES_Lead(Document):
    lead_UUID = Text()
    lead_creation_date = Date()
    lead_creation_user_UUID = Text()
    Sophos_detected_malware = Text()
    ClamAV_detected_malware = Text()
    Clean_files = Text()
    Location_of_files = Text()
    location_clean_files = Text()
    lead_creation_user_UUID = Text()
    Error_found_in_kafka_message = Text()

    class Index:
        # Name of the ES Index
        name = "leads10"
#the listss that need to report to ES have been moved to the main script. You need to pull them 
class ES_LookUp_Writer:
    def __init__(self, key_uuid, worker_uuid, sophos_virus_dir, clean_files, clamscan_virus_dir, changes, file_result):
        self.key_uuid = key_uuid
        self.worker_uuid = worker_uuid
        self.sophos_virus_dir = sophos_virus_dir
        self.clean_files = clean_files
        self.clamscan_virus_dir = clamscan_virus_dir
        self.changes = changes
        self.file_result = file_result
        #print(self.key_uuid)
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
        kuid = self.key_uuid
        wuid = self.worker_uuid
        soph = self.sophos_virus_dir 
        clfl = self.clean_files 
        clvd = self.clamscan_virus_dir 
        chgs = self.changes 
        flrs = self.file_result

        result = ES_Lead(lead_UUID=kuid, Sophos_detected_malware=soph , ClamAV_detected_malware = clvd , Clean_files = clfl , Location_of_files=flrs, lead_creation_user_UUID=wuid).save()

class Error_ES_LookUp_Writer:
    def __init__(self, missing_element):
        self.missing_element = missing_element
        self.create_lookup()

     #Build the connection
     #Make the connection to Elastic Search
    def create_connection(self):
        self.conn = connections.create_connection(
                                    hosts=['localhost'])

     #Logic: IF the lookUp name does NOT exist create the lookup and add the values provided
     #       ELSE pass the record to the update lookup function.
    def create_lookup(self):
        msel = self.missing_element
        self.create_connection()
        Error_results = ES_Lead(Error_found_in_kafka_message = msel).save()
            
#Error_ES_LookUp_Writer()              
#ES_LookUp_Writer()
