# server program to receive data from other peers

import socket


class Tracker:
    def __init__(self, connectionDetails, totalNodesSocket):
        self.connectionDetails = connectionDetails
        self.totalNodesSocket = totalNodesSocket
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def serverCreation(self):

        self.server.bind(self.connectionDetails)
        self. server.listen(5)
        print("Tracker server listening at the IP:", self.connectionDetails[0], "and Port Number:",
              self.connectionDetails[1])


    def receiveNewNode(self):
        client, address = self.server.accept()
        recievedMessage = client.recv(1024).decode('utf-8')
        print(recievedMessage)
        if (recievedMessage[1] == "P"):
            print(recievedMessage[1])
            tuple = (client, recievedMessage)
            print("##########", tuple)
            self.totalNodesSocket.append(tuple)
            print("recieved message is ", recievedMessage)
            client.send("Succeed".encode('utf-8'))
            for node in self.totalNodesSocket:
                try:
                    node[0].sendall(recievedMessage)
                    receive = node[0].recv(1024).decode('utf-8')
                    print("New Node Successfully add is ", receive)
                except:
                    continue


    def sendNewNode(self, receivedMessage):
      pass

    def liveness(self):
        for node in self.totalNodesSocket:
            try:
                node[0].sendall("200".encode('utf-8'))
                node[0].recv(1024).decode('utf-8')
            except:
                print(node[1], " is desconnected from the network")
                continue
