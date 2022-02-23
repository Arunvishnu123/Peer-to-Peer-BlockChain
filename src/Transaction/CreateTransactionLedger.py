class Transactions:
    def _init_(self,transaction,mineRequest):
        self.transaction=transaction
        self.mineRequest = mineRequest
        self.transactionlist = []
    
    def createtransactionlist(self):  
        self.transactionlist.append(self.transaction)
        if(self.mineRequest == 1):
          return self.transactionlist
          self.transactionlist.clear()
          
          
