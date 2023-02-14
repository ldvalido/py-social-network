import sys
import os
from thread_listener import ThreadListener

QUEUE_NAME_SOCIAL_NETWORK = "socialnetwork_posts"
QUEUE_NAME_FOLLOWERS = "socialnetwork_follower"

def callback_post(body):
    print(f" [x] Done Post: {body}")

def callback_follower(body):
    print(f" [x] Done Follower: {body}")

def main(argv):
    print(f"PID: {os.getpid()}")
    queue_host = os.getenv("QUEUE_HOST")
    tFollow = ThreadListener(queue_host, QUEUE_NAME_FOLLOWERS, callback_follower)
    tPost = ThreadListener(queue_host, QUEUE_NAME_SOCIAL_NETWORK, callback_post)
    tFollow.listen()
    tPost.listen()
    print("Listening")
        
if __name__ == "__main__":
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
