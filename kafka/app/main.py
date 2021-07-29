from pykafka import KafkaClient


# client = KafkaClient(hosts="127.0.0.1:9092")
client = KafkaClient(hosts="kafka:9092")
print(client)
topic = client.topics['my.test']
producer = topic.get_sync_producer()
producer.produce('test message'.encode('ascii'))
print('')


consumer = topic.get_simple_consumer()
for message in consumer:
    if message is not None:
        print(message.offset, message.value)