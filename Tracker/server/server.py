# server program to receive data from other peers
import json
import socket
class Tracker:
    def __init__(self, connectionDetails, totalNodesSocket):
        self.connectionDetails = connectionDetails
        self.totalNodesSocket = totalNodesSocket
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.connectionDetails)
        self.server.listen(5)
        print("Tracker server listening at the IP:", self.connectionDetails[0], "and Port Number:",
              self.connectionDetails[1])
        self.recievedMessage = 'ee'

    def receiveNewNode(self):
        client, address = self.server.accept()
        self.recievedMessage = client.recv(1024).decode('utf-8')
        print(self.recievedMessage)
        if (self.recievedMessage[1] == "P"):
            print(self.recievedMessage[1])
            tuple = (client, self.recievedMessage)
            print("##########", tuple)
            self.totalNodesSocket.append(tuple)
            print("recieved message is ", self.recievedMessage)
            client.send("Succeed".encode('utf-8'))
        self.extractIP()
        ##self.sendNewNode(receivedMessage=)
        self.sendNewNode()

    def extractIP(self):
      extracted =  json.loads(self.recievedMessage[7:-1])
      print("Port is ",extracted['port'])
      print("IP address is ",extracted['ipaddress'])
      connectionDetails = (extracted['ipaddress'],int(extracted['port']))
      print(connectionDetails)
      print(self.recievedMessage)
      self.sendNewNode(connectionDetails,self.recievedMessage)
      return connectionDetails

    def sendNewNode(self,connectionDetails,message):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(connectionDetails)
        client.send(message.encode())
        u  = client.recv(1024).decode('utf-8')
        print(u)

    def liveness(self):
        for node in self.totalNodesSocket:
            try:
                node[0].sendall("200".encode('utf-8'))
                node[0].recv(1024).decode('utf-8')
            except:
                print(node[1], " is desconnected from the network")
                continue
