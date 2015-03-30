# pytables
Deny IPs from queues

## Introduction
pytables always waiting queues from RabbitMQ, the IP will be dropped when got it from queue.

## Getting Started

### Installation

#### Clone the source code using `git`
    

    git clone https://github.com/jiasir/pytables.git


#### Install pytables


    sudo python setup.py install


#### Run the pytables as a background


    sudo nohup pytables > /dev/null 2>&1 &


## Build a Testing Environment
Using Vagrant to build a testing environment, see Vagrantfile to got the testing node IPs.

To building a RabbitMQ Server and pytables Server


    cd examples
    vagrant up
    

## Some Utils
You can using the flowing script to test your environment.

 * examples/publish/    # Publish/Subscribe: Sending messages to many consumers at once.
 * examples/topics/      # Topics: Receiving messages based on a pattern.

