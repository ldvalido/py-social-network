import threading

from listener import BasicListener
class ThreadListener:
    def __init__(self, queue_host: str, queue_name: str, callback: any):
        self.queue_host = queue_host
        self.queue_name = queue_name
        self.callback = callback
    
    def listen(self):
        raw_listener = BasicListener(self.queue_host, self.queue_name, self.callback)
        tLhread_listener = threading.Thread(target=raw_listener.listener)
        print("Creating thread")
        tLhread_listener.start()