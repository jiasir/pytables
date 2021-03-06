#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.20.10'))
channel = connection.channel()
channel.exchange_declare(exchange='ip', type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'

message = ' '.join(sys.argv[2:]) or '10.10.10.10'
channel.basic_publish(exchange='ip', routing_key=routing_key, body=message)
print " [x] Sent %r:%r" % (routing_key, message)

connection.close()