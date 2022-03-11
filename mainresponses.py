from threading import Thread
import mainactions
from BlockChain.Network.RequestType.ReceiveMessage import Receiver
from BlockChain.Queue.Queue import Queue
from BlockChain.Network.MessageType.Join import DataExtraction as joinNewPeerDetails
from BlockChain.Database.PeerDetails import PeerDetailsTable
peerDataTable = PeerDetailsTable()
reciever = Receiver(('192.168.0.13',4001))
peerList = [ ]

while True:
    # recieve new Node details
    recieveNewNodeQueue =Queue()
    recieveNewNode = Thread(target = reciever.receiveMessagePost,args=(recieveNewNodeQueue ,))
    recieveNewNode.start()
    recieveNewNode.join()
    receivedMessage = recieveNewNodeQueue.dequeue()
    print(type(receivedMessage))
    if(receivedMessage[4] == "J"):
         extractedData = joinNewPeerDetails(receivedMessage,peerList)
         print("Data Extracted from the recieved message:",extractedData.finalDataExtraction())
         peerDataTable.addElements(extractedData.finalDataExtraction())
















