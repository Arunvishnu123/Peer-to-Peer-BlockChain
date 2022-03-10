import threading
from Tracker.server.server import Tracker
####################################################################################################
node = []
ip = "161.3.59.100"
port  = 7070
connection = (ip,port)
if __name__ == "__main__":
    tracker = Tracker(connection, node)
    while True:
        tracker.receiveNewNode()

