import hashlib
import datetime
import json

class genesisBlock:
    def __init__(self,name,timestamp,version):
        self.name = name
        self.timestamp =timestamp
        self.version = version

    def transaction(self):
        transactionDict = {
        }
        transactionDict["name"] = self.name
        transactionDict["TransactionID"] = hashlib.sha1(str(self.name).encode()).hexdigest()
        transactionDict["Timestamp"] = self.timestamp
        transactionDict["TransactionType"] = "Reward Transaction"
        return transactionDict

    
    def createHeader(self):
        header = {
        }
        header["version"] =self.version
        header["PreviousHash"] = "000000000000000000000000000000000000000000000"
        hashRewardTransaction = json.dumps(self.transaction())
        header["MerkleRoot"] =  hashlib.sha1(str(hashRewardTransaction).encode()).hexdigest()
        header["Timestamp"] = self.timestamp
        header["DifficultyTarget"] = "4"
        header["nonce"]  = ""
        return header
    
    def genesisBlockCreation(self):
        block = {
        }
        block["Size"] =""
        block["Header"] = self.createHeader
        block["TransactionCounter"] = "1"
        block["Transaction"] = self.transaction
        return block





