from kafka import KafkaProducer
import json


class Kafka_Producer:

    def __init__(self, json_string):
        self.json_string = json_string
       

    def kf_produce(self, json_string):
        #turn the documnet into a json and then into bytes
        # string with encoding 'utf-8'
        producer = KafkaProducer(bootstrap_servers='PLAINTEXT://localhost:9092')
        producer = KafkaProducer(value_serializer=lambda m: json.dumps(json_string).encode('ascii'))
        future = producer.send('test', {'key': 'value'})

         try:
             record_metadata = future.get(timeout=10)
         except KafkaError:
             # Decide what to do if produce request failed...
             log.exception()
             pass

          # Successful result returns assigned partition and offset
          print (record_metadata.topic)
          print (record_metadata.partition)
          print (record_metadata.offset)
          
