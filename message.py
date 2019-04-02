import json
import configuration as cf

class messaging:
    def __init__(self, clean_files, files_b4_cleaning, key_uuid, worker_uuid, filename):
        self.clean_files = clean_files
        self.files_b4_cleaning = files_b4_cleaning
        self.key_uuid = key_uuid
        self.worker_uuid = worker_uuid
        self.filename = filename
        self.json_string = None

    def getJson(self):
        jmsg = [self.json_string]
        return jmsg
    def setJson(self, json_string):
        self.json_string = json_string
    
    def report(self, clean_files, files_b4_cleaning):
        file_location1, file_location2 = cf.location()
        #reporting tool. we are picking up the information from the list and comparing the differences. depending on the infomation the following reports an answer.    
        if clean_files==files_b4_cleaning:
            file_result = file_location1
        else:
            file_result = file_location2
        return file_result
    
    def jmsg(self, file_result,  key_uuid, worker_uuid, filename):
        #kafka needs all the information to be converted into bytes. 
        #since there is a large amount of data we break this out into a json message. 
        update_body = {
            "query": {
                "constant_score" : {
                    "filter" : {
                         "bool" : {
                            "must" : [
                                { "terms" : { "UUID" : key_uuid } }, 
                                { "terms" : { "location" : file_result } },
                                { "terms" : { "worker_uuid" : worker_uuid } },
                                { "terms" : { "new filename" : filename } },
                            ]
                        }
                    }
                }
            }
        }
        json_string = json.dumps(update_body)
        self.setJson(json_string)
        return self.getJson()