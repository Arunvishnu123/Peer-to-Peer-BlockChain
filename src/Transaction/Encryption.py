import json
import rsa

class encryption:
    def __init__(self,sprivateKey,respublicKey,data):
        self.sprivateKey = sprivateKey
        self.respublicKey = respublicKey
        self.data = data

    ## for authentication of the sender
    def encryptedMessage1(self):                    
        message = json.dumps(self.data)
        encodedMessage = message.encode('utf8')
        digitalSign = rsa.encrypt(encodedMessage,self.respublicKey)
        return digitalSign

   ## maintain confidentiality for sender and receiver
    def encryptedMessage2(self):
        encriptedMessage = rsa.encrypt(self.encryptedMessage1,self.respublicKey)
        return encriptedMessage