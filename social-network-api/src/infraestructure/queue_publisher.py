import pika
class QueuePublisher():
    def __init__(self, hostname, queue_name):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(hostname))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name)

    def publish(self, queue_name, message):
        self.channel.basic_publish(exchange='', body=message, routing_key=queue_name)
        self.connection.close()