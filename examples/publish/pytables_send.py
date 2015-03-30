#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.20.10'))
channel = connection.channel()

channel.exchange_declare(exchange='ip', type='fanout')
message = ' '.join(sys.argv[1:]) or "10.10.10.10"

channel.basic_publish(exchange='ip', routing_key='', body=message)
print " [x] Sent %r" % (message,)

connection.close()