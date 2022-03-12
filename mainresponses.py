from threading import Thread
from BlockChain.Network.RequestType.ReceiveMessage import Receiver
from BlockChain.Queue.Queue import Queue
from BlockChain.Network.MessageType.Join import DataExtraction as joinNewPeerDetails
from BlockChain.Network.MessageType.Transaction import DataExtraction as TransactionMessageExtraction
from BlockChain.Database.PeerDetails import PeerDetailsTable
from BlockChain.Database.Transactions import TransactionsDT
from BlockChain.Database.Ledger import TransactionsLedgerDT
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
    if(receivedMessage[4] == "J"):
         extractedData = joinNewPeerDetails(receivedMessage,peerList)
         print("Data Extracted from the recieved message:",extractedData.finalDataExtraction())
         peerDataTable.addElements(extractedData.finalDataExtraction())

    if(receivedMessage[4] == "T"):
        extractedTransactionData = TransactionMessageExtraction(receivedMessage)
        print("Tranasacted Message:",extractedTransactionData.finalDataExtraction())
        transactionDataTable.addElements(extractedTransactionData.finalDataExtraction()[0])

        #send the received transaction message to the all other peers
        #ledgerDataTable.addLedgerElements(extractedTransactionData.finalDataExtraction()[1])

    if(receivedMessage[4] == "L"):
        print("test")