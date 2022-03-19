# post request to the multiple peers
import socket

class BroadCastMulitple:
    def __init__(self,connectedList,message):
        #connectedList is list of all connected nodes in the network and
        # also each index in the list is a tuple which contain IP address and port number
        self.connectedList  = connectedList
        #message to be transmitted throughout thre network
        self.message = message

    def mPeer(self):
        for node in self.connectedList:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(1)
            try:
              client.connect(node)
              client.settimeout(None)
              client.send(self.message)
              status = client.recv(1024).decode('utf-8')
              print("Status of the message to each client",node,status)
            except:
                return node
                continue



