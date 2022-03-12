from threading import Thread
from BlockChain.Network.RequestType.ReceiveMessage import Receiver
from BlockChain.Queue.Queue import Queue
from BlockChain.Network.MessageType.Join import DataExtraction as joinNewPeerDetails
from BlockChain.Network.MessageType.Transaction import DataExtraction as TransactionMessageExtraction
from BlockChain.Database.PeerDetails import PeerDetailsTable
from BlockChain.Database.Transactions import TransactionsDT
from BlockChain.Database.Ledger import TransactionsLedgerDT
from BlockChain.Network.MessageType.TransactionLedger import LedgerDataExtraction
###################################################################################################
#create datables object
peerDataTable = PeerDetailsTable()
transactionDataTable  = TransactionsDT()
ledgerDataTable = TransactionsLedgerDT()

#ServerIP
reciever = Receiver(('192.168.0.13',4001))
peerList = [ ]

while True:
    # receive new Node details
    recieveNewNodeQueue =Queue()
    recieveNewNode = Thread(target = reciever.receiveMessagePost,args=(recieveNewNodeQueue ,))
    recieveNewNode.start()
    recieveNewNode.join()
    receivedMessage = recieveNewNodeQueue.dequeue()
    print(type(receivedMessage))

    #peer deatils recives
    if(receivedMessage[4] == "J"):
         extractedData = joinNewPeerDetails(receivedMessage,peerList)
         print("Data Extracted from the recieved message:",extractedData.finalDataExtraction())
         peerDataTable.addElements(extractedData.finalDataExtraction())

    #transaction message receiving logic
    if(receivedMessage[4] == "T"):
        extractedTransactionData = TransactionMessageExtraction(receivedMessage)
        print("Extracted Message of Transaction:",extractedTransactionData.finalDataExtraction())
        transactionDataTable.addElements(extractedTransactionData.finalDataExtraction())

    #transaction ledger creation
    if(receivedMessage[4] == "L"):
        extractedLedgerData = LedgerDataExtraction(receivedMessage)
        print("Extracted Message of Transactions(for ledger creation:",extractedLedgerData.finalDataExtraction())
        ledgerDataTable.addLedgerElements(extractedLedgerData.finalDataExtraction())

