import hashlib
import datetime


class basicTransaction:
    def __init__(self,senderName,recieverName,amount,message):
        self.senderName = senderName
        self.recieverName =recieverName
        self.amount = amount
        self.message=message

    def createMessage(self):
        data ={

        }
        data["amountname"]= self.amount
        data["message"] = self.amount
        return data

    def createTransaction(self):
        transaction ={

        }

        transactionIDCreation = str(self.senderName) + str(self.recieverName) + str(self.amount)
        transaction["transactionID"]=hashlib.sha1(transactionIDCreation.encode()).hexdigest()
        transaction["sendername"]= self.senderName
        transaction["receivername"]= self.recieverName
        transaction["data"]= self.createMessage()
        transaction["dateandtime"]=str(datetime.datetime.now())
        return transaction

