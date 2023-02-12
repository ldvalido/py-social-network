import pika
class BasicListener:
    def __init__(self, queue_host: str, queue_name: str, callback: any):
        self.queue_host = queue_host
        self.queue_name = queue_name
        self.callback = callback
        pass

    def basic_callback(self, ch, method, properties, body):
        print(" [x] Received %r" % body)
        self.callback(body)
        ch.basic_ack(delivery_tag=method.delivery_tag)
    
    def listener(self):
        
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host = self.queue_host))
        
        channel = connection.channel()

        channel.queue_declare(queue = self.queue_name)
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue = self.queue_name, on_message_callback = self.basic_callback)
        channel.start_consuming()
