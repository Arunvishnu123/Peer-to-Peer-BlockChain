class block:
    def __init__(self,version,previousHash,merkleRoot,timestamp,difficultyTarget,nonce,transactionList):
       self.version  = version
       self.previousHash = previousHash
       self.merkleRoot = merkleRoot
       self.timestamp = timestamp
       self.difficultyTarget = difficultyTarget
       self.nonce = nonce 
       self.transactionList = transactionList

    def createHeader(self):
       header = {
       }
       header["Version"] = self.version
       header["PreviousHash"] = self.previousHash
       header["MerkleRoot"] =self.merkleRoot
       header["Timestamp"] = self.timestamp
       header["DifficultyTarget"] = self.difficultyTarget
       header["Nonce"] =self.nonce
       return header

    def createTransactionList(self):
       transactions ={
       }
       transactions["Transactions"] = self.transactionList
       return transactions

    def transactionCounter(self):
       return len(self.transactionList)

    def createBlocks(self):
      block = {
      }
      block["Header"] = self.createHeader()
      block["TransactionCounter"] = self.transactionCounter()
      block["TransactionList"] = self.createTransactionList()
      return block


