import json
import hashlib

class Mining:
    def __init__(self,createdBlock):
       self.createdBlock = createdBlock

    def createHash(self):
       block = json.dumps(self.createdBlock)
       hashBlock = hashlib.sha256( block .encode()).hexdigest()
       return hashBlock

    def mining(self):
       fullBlock ={
       }
       for i in range(0,1000000):
         self.createdBlock["nonce"] = i
         hashBlock = hashlib.sha256(str(input).encode()).hexdigest()
         print(hashBlock)
         if hashBlock[0] == '0' and hashBlock[1] == '0' and hashBlock[2] == '0' and hashBlock[3] == '0':
           break
       
       fullBlock["hash"] = hashBlock
       fullBlock["Block"] = self.createdBlock
       return fullBlock