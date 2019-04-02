from kafka import KafkaProducer
import json


class Kafka_Producer:

    def __init__(self, json_string):
        self.json_string = json_string
       

    def kf_produce(self, json_string):
        #turn the documnet into a json and then into bytes
        # string with encoding 'utf-8'
        json_string = json.dumps(json_string)
        fin_result = bytes(json_string, 'utf-8')
    
        #other producers below
        #producer = KafkaProducer(bootstrap_servers='localhost:9092'
        #plaintext used for docker
        producer = KafkaProducer(bootstrap_servers='PLAINTEXT://localhost:9092')
        #extras host if needed
        #producer2 = KafkaProducer(bootstrap_servers='localhost:9093')
        #producer3 = KafkaProducer(bootstrap_servers='localhost:9094')
        bracket = "{"
        for _ in range(1):
            print(producer.send('test', bytes(fin_result))) 
          