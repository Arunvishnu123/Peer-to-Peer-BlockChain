transactionlist = []

class TransactionsLedger:
    def __init__(self,transaction,mineRequest):
        self.transaction=transaction
        self.mineRequest = mineRequest
       
    
    def createtransactionlist(self):
        transactionlist.append(self.transaction)   
        return transactionlist
        #self.transactionlist.clear()
          
          
