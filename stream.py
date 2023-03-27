# from kafka import KafkaProducer
# import json

# class MessageProducer:
#     broker = "1003"
#     topic = "Registered_Demo_User"
#     # boostrap_servers = ['localhost:9092']
#     Producer = None

#     def kafaka_cred(self,broker, topic):
#         broker = broker
#         topic = topic
        
#         self.Producer= KafkaProducer(bootstrap_servers=broker,
#             value_serializer = lambda v: json.dumps(v).encode('utf-8'),
#             acks='all',
#             retries = 3)
        

#     def send_msg(msg):
#         print("sending message...")
#         try:
#             future = self.Producer(topic,msg)
#             self.Producer.flush()
#             future.get(timeout=60)
#             print("message sent successfully...")
#             return {'status_code':200, 'error':None}
#         except Exception as ex:
#             return ex


# broker = 'localhost:9092'
# topic = 'test-topic'
# message_producer = MessageProducer(broker,topic)

# data = {'name':'abc', 'email':'abc@example.com'}
# resp = message_producer.send_msg(data)
# print(resp)

