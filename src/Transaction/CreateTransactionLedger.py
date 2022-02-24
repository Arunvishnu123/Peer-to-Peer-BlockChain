transactionlist = []

class TransactionsLedger:
    def __init__(self,transaction):
        self.transaction=transaction
    
    def createtransactionlist(self):
        transactionlist.append(self.transaction)   
        return transactionlist
        #self.transactionlist.clear()
    def miningRequest(self):
        transactionlist.clear()
          
          
