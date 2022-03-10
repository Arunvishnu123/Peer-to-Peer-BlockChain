from threading import Thread
from BlockChain.Network.RequestType.ReceiveMessage import Receiver
from BlockChain.Queue.Queue import Queue
reciever = Receiver(('192.168.0.13',4001))


while True:
    # recieve new Node details
    recieveNewNodeQueue =Queue()
    recieveNewNode = Thread(target = reciever.receiveMessagePost,args=(recieveNewNodeQueue ,))
    recieveNewNode.start()
    recieveNewNode.join()
    receivedMessage = recieveNewNodeQueue.dequeue()











