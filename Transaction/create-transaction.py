import hashlib
import datetime

class Transactions:
    def __init__(self,senderName,recieverName,amount,message):
        self.senderName = senderName
        self.recieverName =recieverName
        self.amount = amount
        self.message=message
        
    def createtransaction(self):
        transaction = {
        }
        transactionIDCreation = str(self.senderName) + str(self.recieverName) + str(self.amount)
        transaction["transactionID"]=hashlib.sha1(transactionIDCreation.encode()).hexdigest()
        transaction["sendername"]= self.senderName
        transaction["receivername"]= self.recieverName
        transaction["amountname"]= self.amount
        transaction["dateandtime"]=str(datetime.datetime.now())
        return transaction


tets = Transactions("arun","vishnu",34,"hi How are you")

print(tets.createtransaction())