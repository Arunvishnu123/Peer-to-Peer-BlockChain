# server program to receive data from other peers
import json
import socket
from Tracker.Database.PeerDetails import PeerDetailsTable

class Tracker:
    def __init__(self, connectionDetails):
        self.connectionDetails = connectionDetails
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.connectionDetails)
        self.server.listen(5)
        print("Tracker server listening at the IP:", self.connectionDetails[0], "and Port Number:",
              self.connectionDetails[1])
        self.recievedMessage = ''

    def receiveNewNode(self,queue):
        print("running")
        client, address = self.server.accept()
        self.recievedMessage = client.recv(1024).decode('utf-8')
        print(self.recievedMessage)
        client.send("Succeed".encode('utf-8'))
        queue.enque(self.recievedMessage)
        return self.recievedMessage

    def extractIP(self):
        extracted = json.loads(self.recievedMessage[7:-1])
        print("Port is ", extracted['port'])
        print("IP address is ", extracted['ipaddress'])
        print("Public Key is ", extracted['publickey'])
        connectionDetails = (extracted['ipaddress'], int(extracted['port']) ,extracted['publickey'])
        print(connectionDetails)
        return connectionDetails

    def sendNewNode(self, connectionDetails, message):
        for connection in connectionDetails:
            try:
              print(connection)
              client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
              client.settimeout(1)
              client.connect(connection)
              client.settimeout(None)
              client.send(message.encode())
              response = client.recv(1024).decode('utf-8')
              print("response from the server",response)
              print(connection,response)
            except:
              print( "failed",connection)
              continue

    def liveness(self, connectionDetails, message):
        li = []
        for connection in connectionDetails:
            try:
                print(connection)
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(1)
                client.connect(connection)
                client.settimeout(None)
                client.send(message.encode())
                response = client.recv(1024).decode('utf-8')
                print("response from the server", response)
                print("succed",connection, response)
            except:
                print("failed", connection)
                peerTable = PeerDetailsTable()
                peerTable.deletePeerData(connection)
                li.append(connection)
                continue
        return tuple(li)

    def livenessTest(self):
        pass