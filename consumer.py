# -*- coding: utf-8 -*-

from kafka import KafkaConsumer
consumer = KafkaConsumer('test')
for message in consumer:
    print(message.value)
    if message.value.lower() == b'quit':
        break