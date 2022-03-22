from threading import Thread
from BlockChain.Network.RequestType.ReceiveMessage import Receiver
from BlockChain.Queue.Queue import Queue
from BlockChain.Network.MessageType.Join import DataExtraction as joinNewPeerDetails
from BlockChain.Network.MessageType.Transaction import DataExtraction as TransactionMessageExtraction
from BlockChain.Database.PeerDetails import PeerDetailsTable
from BlockChain.Database.Transactions import TransactionsDT
from BlockChain.Database.Ledger import TransactionsLedgerDT
from BlockChain.Network.MessageType.TransactionLedger import LedgerDataExtraction
from BlockChain.Network.MessageType.MineComplete import DataExtraction as MineCompleteDataExtraction
from BlockChain.Database.MineComplete import MiningCompleteStatusDT
from BlockChain.Network.MessageType.NewBlock import BlockDataExtraction
from BlockChain.Database.BlockChain import BlockChainDT
from BlockChain.Network.MessageType.UnconnectedPeer import UnconnectedDataExtraction
from BlockChain.CheeseCoin.BlockChain.GenesisBlock import genesisBlock
from BlockChain.Database.CurrentPeerData import PeerData
from BlockChain.Network.MessageType.NewBlock import BlockRequestCreation
from BlockChain.Network.RequestType.BroadcastMultiple import BroadCastMulitple
import socket

###################################################################################################
#create datables object
peerDataTable = PeerDetailsTable()
transactionDataTable  = TransactionsDT()
ledgerDataTable = TransactionsLedgerDT()
blockchainTable  =  BlockChainDT()
peerData  = PeerData()

#ServerIP
ipaddress = socket.gethostbyname(socket.gethostname())
reciever = Receiver((ipaddress,4001))
peerList = [ ]

while True:
    # receive new Node details
    recieveNewNodeQueue =Queue()
    recieveNewNode = Thread(target = reciever.receiveMessagePost,args=(recieveNewNodeQueue ,))
    recieveNewNode.start()
    recieveNewNode.join()
    receivedMessage = recieveNewNodeQueue.dequeue()
    print(type(receivedMessage))
    print(receivedMessage)

    #peer details receives
    if(receivedMessage[4] == "J"):
         extractedData = joinNewPeerDetails(receivedMessage,peerList)
         print("Data Extracted from the recieved message:",extractedData.finalDataExtraction())
         peerDataTable.addElements(extractedData.finalDataExtraction())
         # create the genesis block in the blockchain
         try:
             print("lasthash", blockchainTable.retriveLastHash()[0])
         except:
             peerData = peerData.retrivePeerData()
             print("current peer data:",peerData)
             genesisBlockCreation = genesisBlock(peerData[0][1])
             print("Genesis Block", genesisBlockCreation.mining())
             genesisBlock = genesisBlockCreation.mining()
             genesisBlockRequestCreation = BlockRequestCreation(genesisBlock)
             genesisBlockMessageFormat = genesisBlockRequestCreation.final()
             print(genesisBlockMessageFormat)
             connectedPeersList2 = peerDataTable.retrivePeerDetailsGensis(peerData[0][1])
             print("connected peer list",connectedPeersList2)
             blockExtraction1 = BlockDataExtraction(receivedMessage)
             print(blockExtraction1.genesisBlockExtraction(genesisBlock))
             blockchainTable.addBlocks(blockExtraction1.genesisBlockExtraction(genesisBlock))
             broadCastMineCompleteMessage = BroadCastMulitple(connectedPeersList2, genesisBlockMessageFormat)
             broadCastMineCompleteMessage.mPeer()

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

    #Mine Complete Request
    if(receivedMessage[4] == "M"):
        mineCompleteDataExtraction = MineCompleteDataExtraction(receivedMessage)
        statusMine = mineCompleteDataExtraction.finalDataExtraction()
        print("status",statusMine)
        print(type(statusMine))
        miningCompleteStatus = MiningCompleteStatusDT()
        print((statusMine,1))
        miningCompleteStatus.addMiningStatus((statusMine,1))

    #newBlockCreated
    if(receivedMessage[4] == "N"):
        print("last hash", blockchainTable.retriveLastHash())
        blockExtraction =  BlockDataExtraction(receivedMessage)
        print(blockExtraction.finalDataExtraction())
        blockchainTable.addBlocks(blockExtraction.finalDataExtraction())

    #sendUnconnected
    if(receivedMessage[4]=="U"):
        print("Unconnected Received")
        unconnectedDataExtraction = UnconnectedDataExtraction(receivedMessage)
        unConnectedPeers = unconnectedDataExtraction.finalDataExtraction()
        print(unconnectedDataExtraction.finalDataExtraction()[0][1])
        print(type(unconnectedDataExtraction.finalDataExtraction()[0]))
        for unconnected in unConnectedPeers:
            print("unconnected",unconnected)
            print(unconnected[0])
            peerDataTable.deletePeerData(unconnected[0])










