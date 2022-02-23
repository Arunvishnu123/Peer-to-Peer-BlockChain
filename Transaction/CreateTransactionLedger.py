class Transactions:
    def _init_(self,transaction):
        self.transaction=transaction
    
    def createtransactionlist(self):
        transactionlist = []
        transactionlist.append(self.transaction)
        return transactionlist
