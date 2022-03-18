from threading import Thread
from Tracker.server.server import Tracker
from Tracker.Queue.QueueThreading import Queue
from pathlib import Path
from Tracker.Database.Creation import CreateDatabase
from Tracker.Database.PeerDetails import PeerDetailsTable
from Tracker.Database.RegisteredPeers import RegisteredPeerTable
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
#Created Registered peers table
createdRegisteredPeers = RegisteredPeerTable()
createdRegisteredPeers.createRegisteredTable()
############################################################################################################
#Automatic liviliness test for the peers
def livelinesstest():
    while True:
       print("Doing Liveliness Test")
       time.sleep(40)
       connectionDetails = createdRegisteredPeers.retrieveRegisteredElements()
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
            createdRegisteredPeers.addRegisteredElements(extractReceivedData)
            connectionDetails = peerDataTable.retrieveElements()
            tracker.sendNewNode(connectionDetails, receivedMessage)

