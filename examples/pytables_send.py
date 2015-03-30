#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.20.10'))
channel = connection.channel()

channel.queue_declare(queue='ip')

channel.basic_publish(exchange='',
                      routing_key='ip',
                      body='10.10.10.10')
print " [x] Sent '10.10.10.10'"

connection.close()