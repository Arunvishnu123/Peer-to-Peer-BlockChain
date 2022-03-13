from threading import Thread
from Tracker.server.server import Tracker
from Tracker.Queue.QueueThreading import Queue
from pathlib import Path
from Tracker.Database.Creation import CreateDatabase
from Tracker.Database.PeerDetails import PeerDetailsTable

####################################################################################################
# tracker connection details
ip = "192.168.0.13"
port = 7070
connection = (ip, port)
####################################################################################################
if Path('./Tracker/DatabaseSource/Tracker.db').is_file():
    print("DataBaseAlreadyCreated")

else:
    dataBaseCreation = CreateDatabase()

peerDataTable = PeerDetailsTable()

if __name__ == "__main__":
    tracker = Tracker(connection)
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
