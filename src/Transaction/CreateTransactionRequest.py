import hashlib
import datetime


class Transactions:
    def __init__(self,senderName,recieverName,message):
        self.senderName = senderName
        self.recieverName =recieverName
        self.message=message

    def createTransaction(self):
        transaction ={
        }
        transactionIDCreation = str(self.senderName) + str(self.recieverName) + str(self.amount)
        transaction["transactionID"] = hashlib.sha1(transactionIDCreation.encode()).hexdigest()
        transaction["sendername"] = self.senderName
        transaction["receivername"] = self.recieverName
        transaction["message"] = self.message
        transaction["dateandtime"] = str(datetime.datetime.now())
        return transaction

