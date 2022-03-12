from BlockChain.Network.TrackerClient.client import TrackerClient
from BlockChain.Network.TrackerClient.MessageCreationToTracker import PeerDetails
from BlockChain.CheeseCoin.Transaction.GeneratePublicPrivateKey import generatePublicPrivateKey
from BlockChain.Network.MessageType.Join import PeerNewData
from BlockChain.CheeseCoin.Transaction.TransactionData import TransactionData
from BlockChain.CheeseCoin.Transaction.Encryption import encryption
from BlockChain.CheeseCoin.Transaction.CreateTransactionData import Transactions
from BlockChain.Network.MessageType.Transaction import RequestCreation as TransactionRequestCreation
from BlockChain.Network.RequestType.BroadcastSelected import BroadCastSelected
from BlockChain.Network.MessageType.TransactionLedger import LedgerRequestCreation
from BlockChain.Network.RequestType.BroadcastMultiple import BroadCastMulitple
from BlockChain.Database.PeerDetails import PeerDetailsTable
import time
import socket

################################################################################################################
#database for the connected peer details
connectedPeers  = PeerDetailsTable()
################################################################################################################
if __name__ == "__main__":
    ############################################################################################################
    # Private key and Public key generation
    hostGeneratePublicPrivateKey = generatePublicPrivateKey
    hostPublicPrivateKey = hostGeneratePublicPrivateKey.generatePubPriKeyPair()
    hostPublicKey = hostPublicPrivateKey[0]
    hostPrivateKey = hostPublicPrivateKey[1]
    print("type of private key", type(hostPrivateKey))
    print("type of public key", type(hostPublicKey))
    ############################################################################################################
    # create tracker client object and message creation to send the connection details to the tracker
    # Tracker network details
    trackerIP = "192.168.0.13"
    trackerPort = 7070
    trackerTriple = (trackerIP,trackerPort)
    # new peer details
    ipAddress = socket.gethostbyname(socket.gethostname())
    port = input("Enter the port to run the peer:")
    name = input("Enter your Name:")
    # peer data converted to dictionary for sending
    peerDetails = PeerDetails(ipAddress, port, hostPublicKey,name)
    while True:
        # select the operation need to do by the system
        print("################################################################################################################################################")
        print("Enter C or c to connect to the peer at the first time(means connect to the tracker)\nEnter T or t to send message and make transaction to the peers\nEnter M or m for mining the current transaction and create Block")
        operation = input("Select the operation need to do:")
#####################################################################################################################################################
        #Select C or c to connect the new peer to the newtwork
        if operation == "C" or operation == "c":
            peerJsonData = peerDetails.createMessage()
            print("Dictionary Converted Peer Data : ",peerJsonData)
            # message creator while send the peer data to tracker
            peerMessageStructure = PeerNewData(peerJsonData)
            finalMessageStructure = peerMessageStructure.final()
            print("final message format of the new peer details to the tracker:",finalMessageStructure)
            #send the final message to the tracker
            trackerClient = TrackerClient(trackerTriple,finalMessageStructure)
            trackerClient.trackerClient()
#############################################################################################################################################
        #Select t or T to do individual transactions
        if operation == "T" or operation == "t":
            print("Connected Peers Name",connectedPeers.retreievePeerName())
            receiverName = input("Select the receiver name from the list:")
            amount = input("Enter the transaction amount:")
            message = input("Enter the message to send :")
            receiverPeerDetails = connectedPeers.retrieveAllSelected(receiverName)
            print("selected peer details:", receiverPeerDetails)
            #####################################################################################################
            #convert the transmitted message to a json string
            transactionMessage = TransactionData(amount, message)
            data = transactionMessage.createMessage()
            print("message and amount to be send", data)
            ######################################################################################################
            # Encryption of the message
            oencryption = encryption(hostPrivateKey,hostPublicKey, data, name)
            digtalSignature = oencryption.digitalSignature()
            print("vcfg", digtalSignature)
            encryptedData = oencryption.encryptedMessage()
            print(encryptedData)
            print("type of " , type(encryptedData))
            finalMessage = {"Message": encryptedData, "DigitalSignature": digtalSignature}
            print("EncryptedData", finalMessage)
            ####################################################################################################
            # Creating the transaction details
            transactureStructure = Transactions(name, receiverName, finalMessage)
            transactionFullMessage = transactureStructure.createTransaction()
            print("TransactionMessage", transactionFullMessage)
            ######################################################################################################
            transaction = TransactionRequestCreation(transactionFullMessage)
            finalEncodeMessage = transaction.final()
            print("Final Encoded Message for sending :",finalEncodeMessage)
            ######################################################################################################
            #send the message to the selected peer
            sendMessage  = BroadCastSelected((receiverPeerDetails[2],receiverPeerDetails[3]),finalEncodeMessage)
            sendMessage.sPeer()
            time.sleep(2)
            #######################################################################################################
            ledgerRequestCreation = LedgerRequestCreation(transactionFullMessage)
            ledgerMessage = ledgerRequestCreation.final()
            print("Converted Transaction Message to send to other peers format:", ledgerMessage)
            connectedPeersList = connectedPeers .retrieveElements()
            broadCastTransactions = BroadCastMulitple (connectedPeersList, ledgerMessage)
            broadCastTransactions.mPeer()

        if operation == "M" or operation == "m":
            pass

