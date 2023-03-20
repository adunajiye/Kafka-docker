from faker import Faker
Fake = Faker()
import time
from kafka import KafkaProducer
import zookeeper
import random
import json


def get_registered_user():
    registered_users = {
        "name":Fake.name(),
        "address":Fake.address(),
        "created_at":Fake.year(),
        "price":random.randint(50000,1000000),
        "address":Fake.address(),
        "email":Fake.email(),
        "credit_no":Fake.credit_card_number()
    }
    return registered_users



if __name__ == "__main__":
    while 1 == 1:
        print(get_registered_user())
        time.sleep(2)
        
        
