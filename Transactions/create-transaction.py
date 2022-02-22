import hashlib
import datetime
currentTime=datetime.datetime.now()
transactionlist = []


class Transactions:
    def __init__(self,senderName,recieverName,amount,message):
        self.senderName = senderName
        self.recieverName =recieverName
        self.amount = amount
        self.message=message
        
    def createtransaction(self):
        transaction = {
        }
        transaction["transactionID"]="tets"
        transaction["sendername"]= self.sender
        transaction["receivername"]= self.receiver
        transaction["amountname"]= self.sender
        transaction["dateandtime"]=str(currentTime)
    
print(hashlib.sha1("a".encode()).hexdigest())


