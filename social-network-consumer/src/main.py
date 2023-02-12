import sys
import os
from thread_listener import ThreadListener

QUEUE_NAME_SOCIAL_NETWORK = "socialnetwork_posts"
QUEUE_NAME_FOLLOWERS = "socialnetwork_follower"
QUEUE_HOST = "localhost"

def callback_post(body):
    print(f" [x] Done Post: {body}")

def callback_follower(body):
    print(f" [x] Done Follower: {body}")

def main(argv):
    print(f"PID: {os.getpid()}")
    tFollow = ThreadListener(QUEUE_HOST, QUEUE_NAME_FOLLOWERS, callback_follower)
    tPost = ThreadListener(QUEUE_HOST, QUEUE_NAME_SOCIAL_NETWORK, callback_post)
    tFollow.listen()
    tPost.listen()
    print("Listening")
        
if __name__ == "__main__":
    main(sys.argv)