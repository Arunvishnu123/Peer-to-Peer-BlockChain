######################################################################################
# Blockchain working without networking Purpose of this to test the logic make sure it is working or not 

from Transaction.TransactionData import TransactionData
from Transaction.CreateTransactionData import Transactions
from Transaction.GeneratePublicPrivateKey import generatePublicPrivateKey
from Transaction.Encryption import encryption
from Transaction.CreateTransactionLedger import TransactionsLedger
import threading

if __name__ == "__main__":
    ###################################################################
    # Private key and Public key generation
    senderGenerate = generatePublicPrivateKey
    receiverGenerate = generatePublicPrivateKey
    senderPublicPrivateKey = senderGenerate.generatePubPriKeyPair()
    recieverPublicPrivateKey = receiverGenerate.generatePubPriKeyPair()
    senderPublicKey = senderPublicPrivateKey[0]
    senderPrivateKey = senderPublicPrivateKey[1]
    receiverPublicKey = recieverPublicPrivateKey[0]
    receiverPrivateKey = recieverPublicPrivateKey[1]
    #########################################################################
    while True:
        ######################################################################
        # Enter the sender and reciver details 
        senderName = input("Enter the Sender Name:")
        receiverName =input("Enter the receiver name:")
        amount = input("Enter the amount:")
        message = input("Enter the message:")
        transactionMessage = TransactionData(amount,message)
        data  = transactionMessage.createMessage()
        print("message and amount to be send",data)
        ######################################################################
        # Encryption of the message
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
        #######################################################################
        # Creating the transaction details 
        transactureStructure = Transactions(senderName,receiverName,finalMessage)
        transactionFullMessage = transactureStructure.createTransaction()
        print("dsfsfdfs",transactionFullMessage)
        #######################################################################
        #Creating the transaction list
        otransactionLedgerCreation = TransactionsLedger(transactionFullMessage,"0")
        test = otransactionLedgerCreation.createtransactionlist()
        print("dfdsfdsfdfdf",test)
        