from kafka import KafkaConsumer
import json
if __name__ == "__main__":
    Consumer = KafkaConsumer("Dataa",
                             bootstrap_servers='localhost:9092',
                             auto_offset_reset = 'earliest',
                             group_id = "consumer_group_demo")
print("Starting the Consumer")
for msg in Consumer:
    print("Registered User = {}".format(json.loads(msg.value)))
    