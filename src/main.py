from Transaction.TransactionData import TransactionData
from Transaction.CreateTransactionData import Transactions
from Transaction.GeneratePublicPrivateKey import generatePublicPrivateKey
from Transaction.Encryption import encryption
import threading

if __name__ == "__main__":
    senderGenerate = generatePublicPrivateKey
    receiverGenerate = generatePublicPrivateKey
    senderPublicPrivateKey = senderGenerate.generatePubPriKeyPair()
    recieverPublicPrivateKey = receiverGenerate.generatePubPriKeyPair()
    senderPublicKey = senderPublicPrivateKey[0]
    senderPrivateKey = senderPublicPrivateKey[1]
    receiverPublicKey = recieverPublicPrivateKey[0]
    receiverPrivateKey = recieverPublicPrivateKey[1]
    
    while True:
        senderName = input("Enter the Sender Name:")
        receiverName =input("Enter the receiver name:")
        amount = input("Enter the amount:")
        message = input("Enter the message:")
        transactionMessage = TransactionData(amount,message)
        data  = transactionMessage.createMessage()
        print(data)
        oencryption = encryption(senderPrivateKey,receiverPublicKey,data,senderName)
        digtalSignature = oencryption.digitalSignature()
        print("vcfg",digtalSignature)
        encryptedData = oencryption.encryptedMessage()
        print(encryptedData)  
        finalMessage= {     
        }
        finalMessage["Message"] = encryptedData
        finalMessage["DigitalSignature"] = digtalSignature
        print("EncryptedData",finalMessage)
        
        transactureStructure = Transactions(senderName,receiverName,finalMessage)
        print(transactureStructure.createTransaction())
