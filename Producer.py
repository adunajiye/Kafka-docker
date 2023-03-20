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
Broker = "1003"
bootstrap_server = Broker

# function produce_msgs starts producing messages with Faker
# def produce_msgs(hostname='localhost',
#                  port='9092',
topic_name='Registered_Demo_User'         
#                  nr_messages=2,                     # Number of messages to produce (0 for unlimited)
#                  max_waiting_time_in_sec=5):

Producer = KafkaProducer(bootstrap_servers = ['localhost:9092'],
                            #  topic = ['Registered_Demo_User'],
                            value_serializer = lambda x:json.dumps(x).encode('utf-8')
                            )
if __name__ == "__main__":
        while 1 == 1:
            Registered_users = get_registered_user()
            data = Registered_users
            # print(data)
            print("Sending Messages In:")
            Producer.send("Registered_Demo_User",data)
            time.sleep(2.2)
# produce_msgs()
        # print("Message Sent",Registered_users)
    

# Kafka Producer to single topic with two partitions
