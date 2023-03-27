from kafka import KafkaProducer
from json import loads,dumps
import json 
import time
from Data import get_registered_user
import zookeeper
import pandas as pd
from faker import Faker
from datetime import datetime
Fake = Faker()
import random




# Single Broker  1 Partition

# Messages will be serialized as JSON 
def serializer(message):
    return json.dumps(message)
Broker = '1001'
bootstrap_server = Broker

# function produce_msgs starts producing messages with Faker
# def produce_msgs(hostname='localhost',
#                  port='9092',
topic_name='Kafka-demo'   
Port = 'PLAINTEXT:9092'      
#                  nr_messages=2,                     # Number of messages to produce (0 for unlimited)
#                  max_waiting_time_in_sec=5):
def get_partition(key,all,available): # Sending the data to only one partition in the broker 
    return 0
Producer = KafkaProducer(bootstrap_servers = ['localhost:9092' ],
                            # Broker = '1001',
                            value_serializer = lambda x:json.dumps(x).encode('utf-8'),
                            partitioner = get_partition,
                            acks='all',
                            retries = 'restart'
                            )
if __name__ == "__main__":
        while 1 == 1:
            Registered_users = get_registered_user()
            data = Registered_users
            print(data)

#             print("sending message...")

#             future = Producer(topic_name,data)
#             Producer.flush()
#             future.get(timeout=60)
#             print("message sent successfully...")
# # return {'status_code':200, 'error':None}

            print(f'Producing message @{datetime.now()}| Dataa = str{(data)}')
            # print("Sending Messages In:")
            Producer.send('Dataa',data)
            time.sleep(2.2)
            Producer.flush()
            # Producer.close()
           

    

# Kafka Producer to single topic with two partitions
