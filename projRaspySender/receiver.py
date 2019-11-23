#!/usr/bin/env python
import pika
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='comm_channel')


def callback(ch, method, properties, body):
    print(body)
    message = json.loads(body)
    msg_id = message['MESSAGE_ID']
    timestamp = message['TIMESTAMP']
    content = message['CONTENT']
    print(f'  [x] Received message [{msg_id}] at [{timestamp}]: {content}')


channel.basic_consume(
    queue='comm_channel', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()