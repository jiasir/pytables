#!/usr/bin/env python
__author__ = 'jiasir'
import pika
import subprocess
import logging


connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.20.10'))
channel = connection.channel()
channel.exchange_declare(exchange='ip_exchange', type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='ip_exchange', queue=queue_name)

logger = logging.getLogger('pytables')
logging.basicConfig(filename='/var/log/pytables.log', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

print ' [*] Waiting for ip. To exit press CTRL+C'


def deny_ip(body):
    subprocess.call(["iptables", "-I", "INPUT", "-s", body, "-j" "DROP"])


d = {}


def callback(ch, method, properties, body):
    if body not in d:
        deny_ip(body)
        d[body] = 1
        logger.info(" [x] Drop: %r" % (body,))


channel.basic_consume(callback, queue=queue_name, no_ack=True)
channel.start_consuming()
