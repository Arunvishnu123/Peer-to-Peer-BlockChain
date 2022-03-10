import threading
from BlockChain.Network.RequestType.ReceiveMessage import Receiver
from mainactions import *
reciever = Receiver(('192.168.0.13',4000))

while True:
    t = threading.Thread(target = reciever.receiveMessagePost)
    t.start()
