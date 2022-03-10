import socket
class TrackerClient:
    # connectDetails is a tuple which contain ipaddress and port number
    def __init__(self, connectDetails,message):
        self.connectDetails = connectDetails
        self.message = message

    def trackerClient(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            print("Trying to connect to the tracker.................")
            client.connect(self.connectDetails)
            print("Connected to the Tracker Successfully")
            client.send(self.message)
            status = client.recv(1024).decode('utf-8')
            print("Status of the Message :", status)
        except:
            print("Connection to the tracker failed to some reason")
