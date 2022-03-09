#server program to receive data from other peers

import socket

class Receiver:
    def __init__(self,connection):
        self.connection = connection

    def serverCreation(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(self.connection)
        server.listen()
        print("peer listening at the IP:",self.connection[0],"and Port Number:",self.connection[1])
        return server

    def receiveMessagePost(self):
        client, address = self.serverCreation().accept()
        recievedMessage = client.recv(1024).decode('utf-8')
        print("recieved message" , recievedMessage)
        client.send("Succeed".encode('utf-8'))
        return recievedMessage

    def receiveMessageGet(self):
        pass
