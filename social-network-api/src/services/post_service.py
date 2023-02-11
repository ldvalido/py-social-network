from src.infraestructure.queue_publisher import QueuePublisher
import json

class PostService:
    QUEUE_NAME = "socialnetwork_posts"
    QUEUE_HOST = "localhost"
    def __init__(self):
        pass
    def publish_post(self, post_message):
        publisher = QueuePublisher(self.QUEUE_HOST, self.QUEUE_NAME)
        
        msg = json.dumps(post_message.dict())
        publisher.publish(queue_name = self.QUEUE_NAME, message = msg)

