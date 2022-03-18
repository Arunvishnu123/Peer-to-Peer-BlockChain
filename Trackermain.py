from threading import Thread
from Tracker.server.server import Tracker
from Tracker.Queue.QueueThreading import Queue
from pathlib import Path
from Tracker.Database.Creation import CreateDatabase
from Tracker.Database.PeerDetails import PeerDetailsTable
import time
import socket

####################################################################################################
# tracker connection details
ip = socket.gethostbyname(socket.gethostname())
port = 7070
connection = (ip, port)
####################################################################################################
if Path('./Tracker/DatabaseSource/Tracker.db').is_file():
    print("DataBaseAlreadyCreated")

else:
    dataBaseCreation = CreateDatabase()

peerDataTable = PeerDetailsTable()
peerDataTable.createTable()
tracker = Tracker(connection)
############################################################################################################
#Automatic liviliness test for the peers
def livelinesstest():
    while True:
       print("Doing Liveliness Test")
       time.sleep(10)
       connectionDetails = peerDataTable.retrieveElements()
       print("Connected peers list:",connectionDetails)
       y = tracker.liveness(connectionDetails,"00000")
       print("unconnected peers list:", y)
       print("succeed")
#liviliness test
livelinessTest = Thread(target=livelinesstest)
livelinessTest.start()
if __name__ == "__main__":

    while True:
        trackerReceiverQueue = Queue()
        receiveData = Thread(target=tracker.receiveNewNode, args=(trackerReceiverQueue,))
        receiveData.start()
        receiveData.join()
        receivedMessage = trackerReceiverQueue.dequeue()
        print(type(receivedMessage))
        print(receivedMessage)
        if receivedMessage[4] == "J":
            extractReceivedData = tracker.extractIP()
            print(extractReceivedData)
            peerDataTable.addElements(extractReceivedData)
            connectionDetails = peerDataTable.retrieveElements()
            tracker.sendNewNode(connectionDetails, receivedMessage)

