#server program to receive data from other peers

import socket

class Tracker:
    def __init__(self,connectionDetails,totalNodesSocket):
        self.connectionDetails = connectionDetails
        self.totalNodesSocket = totalNodesSocket

    def serverCreation(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(self.connectionDetails)
        server.listen()
        print("peer listening at the IP:",self.connectionDetails[0],"and Port Number:",self.connectionDetails[1])
        return server

    def receiveNewNode(self):
        client, address = self.serverCreation().accept()
        recievedMessage = client.recv(1024).decode('utf-8')
        tuple = (self.totalNodesSocket, recievedMessage)
        self.totalNodesSocket.append(tuple)
        print("recieved message" , recievedMessage)
        client.send("Succeed".encode('utf-8'))

    def sendNewNode(self):
        for node in self.totalNodesSocket:
          try:
              pass
          except:
              continue

    def liveness(self):
        for node in self.totalNodesSocket:
            try:
                pass
            except:
                continue