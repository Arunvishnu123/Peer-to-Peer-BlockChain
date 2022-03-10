
class PeerDetails:
    def __init__(self, ipAddress, port,publicKey):
        self.ipAddress = ipAddress
        self.port = port
        self.publicKey = publicKey

    def createMessage(self):
        message = {
        }
        message["port"] = self.port
        message["ipaddress"] = self.ipAddress
        message["publickey"] = str(self.publicKey)



        return message

