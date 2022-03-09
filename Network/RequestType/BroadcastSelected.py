import socket


class BroadCastSelected:
    def __init__(self,connectDetails,message):
        self.connectDetails = connectDetails
        self.message =message

    def peer(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect(self.connectDetails)
            client.send(self.connectDetails)
            status = client.recv(1024).decode('utf-8')
            print("Status of the Message :", status)
        except:
            print("Sending Failed")
