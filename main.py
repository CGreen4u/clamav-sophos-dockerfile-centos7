import Zip
import bash
import Kfconsumer
import Kfproducer
import postgres
import Decryption
import flow
import jsonmsg
import KfElasticsearch
import os
import message
import configuration


#start kafka consumer
Kfconsumer.kafka_consumer1()
kc = Kfconsumer.kafka_consumer1()
kc.CheckMsg()
uuids = kc.getUUIDS()
key_uuid = uuids[0]
fileinfo = kc.getFILE()
filepath = fileinfo[1]
filename = fileinfo[0]
worker_uuid = fileinfo[2]
#kc.bytesToDictionary()

#start Postgres
postgres.postgres_UUID()
pg = postgres.postgres_UUID(filename, filepath, key_uuid) 
conn = pg.post_connect()
pg.querying_data(key_uuid, conn)
pubkey = pg.getPost()
public_keyring = pubkey[0]
passphrase = pubkey[1]
#passphrase = 'greenzone1'
#filepath = '/home/cgreen/Decryption/Encrypted'
#filename = 'massacre-2018.jpg.gpg'
#public_keyring = 'carl'

#Start Decryption
#Decryption.Decryption()
dc = Decryption.Decryption(public_keyring, filename, filepath, passphrase)
dc.makeDir()
dc.Decrypt(filename, public_keyring, filepath, passphrase)
dc.cleanup()


#untar files
zp = Zip.zipper(filename)
zp.unzip()

#virus scanner
bs = bash.malware_process() #ok
bs.malware_bash() #ok
lists = bs.getBash()
clamscan_virus_dir = lists[0]
sophos_virus_dir = lists[1]
clean_files = lists[2]
changes = lists[3]
files_b4_cleaning = lists[4]

#tar files
zp.zipit(filename)

#prepair messages - configuration can be altered for message to ES
mm = message.messaging(clean_files, files_b4_cleaning, key_uuid, worker_uuid, filename)
file_result = mm.report(clean_files, files_b4_cleaning)
json_string = mm.jmsg(file_result, key_uuid, worker_uuid, filename)

#report to elasticsearch 
es = KfElasticsearch.ES_LookUp_Writer(key_uuid, worker_uuid,sophos_virus_dir, clean_files, clamscan_virus_dir, changes, file_result)
es.create_connection()
es.create_lookup()

#report to Kafka
kp = Kfproducer.Kafka_Producer(json_string)
kp.kf_produce(json_string)

