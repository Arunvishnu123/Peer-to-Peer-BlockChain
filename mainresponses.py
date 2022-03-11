from threading import Thread
import mainactions
from BlockChain.Network.RequestType.ReceiveMessage import Receiver
from BlockChain.Queue.Queue import Queue
from BlockChain.Network.MessageType.Join import DataExtraction
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
    extractedData = DataExtraction(receivedMessage,peerList)
    print(extractedData.finalDataExtraction())
    mainactions.peerList = extractedData.finalDataExtraction()
    print("peerlist",mainactions.peerList )














