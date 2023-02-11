from src.model.user_relationship import UserRelationship
from src.infraestructure.queue_publisher import QueuePublisher
import json

class FollowerService:
    QUEUE_NAME = "socialnetwork_follower"
    QUEUE_HOST = "localhost"

    def __init__(self):
        pass

    def publish(self, user_relationship: UserRelationship):
        publisher = QueuePublisher(self.QUEUE_HOST, self.QUEUE_NAME)
        
        msg = json.dumps(user_relationship.dict())
        publisher.publish(queue_name=self.QUEUE_NAME, message = msg)
        