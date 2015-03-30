#!/usr/bin/env python
import pika
import iptc

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.20.10'))
channel = connection.channel()
channel.exchange_declare(exchange='ip', type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='ip', queue=queue_name)

print ' [*] Waiting for ip. To exit press CTRL+C'


def deny_ip(body):
    chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
    rule = iptc.Rule()
    rule.in_interface = "eth+"
    rule.src = "%r/255.255.255.0" % body
    target = iptc.Target(rule, "DROP")
    rule.target = target
    chain.insert_rule(rule)


def callback(ch, method, properties, body):
    deny_ip(body)
    print " [x] Drop: %r" % (body,)

channel.basic_consume(callback, queue=queue_name, no_ack=True)
channel.start_consuming()