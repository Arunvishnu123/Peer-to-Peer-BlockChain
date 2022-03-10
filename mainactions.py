from BlockChain.Network.TrackerClient.client import TrackerClient
from BlockChain.Network.TrackerClient.MessageCreationToTracker import PeerDetails
from BlockChain.CheeseCoin.Transaction.GeneratePublicPrivateKey import generatePublicPrivateKey
from BlockChain.Network.MessageType.Join import PeerNewData
import threading
import socket

####################################################################################################
if __name__ == "__main__":
    ################################################################################################
    # Private key and Public key generation
    hostGeneratePublicPrivateKey = generatePublicPrivateKey
    hostPublicPrivateKey = hostGeneratePublicPrivateKey.generatePubPriKeyPair()
    hostPublicKey = hostPublicPrivateKey[0]
    hostPrivateKey = hostPublicPrivateKey[1]
    #################################################################################################
    # create tracker client object and message creation to send the connection details to the tracker
    # Tracker network details
    trackerIP = "192.168.0.13"
    trackerPort = 7070
    trackerTriple = (trackerIP,trackerPort)

    while True:
        # select the operation need to do by the system
        print("################################################################################################################################################")
        print("Enter C or c to connect to the peer at the first time(means connect to the tracker)")
        operation = input("Select the operation need to do:")


        def test1():
            print("succes")
            # return trackerClient
        if operation == "C" or operation == "c":
            # new peer details
            ipAddress = socket.gethostbyname(socket.gethostname())
            port = input("Enter the port to run the peer:")
            # peer data converted to dictionary for sending
            peerDetails = PeerDetails(ipAddress, port, hostPublicKey)
            peerJsonData = peerDetails.createMessage()
            print("Dictionary Converted Peer Data : ",peerJsonData)
            # message creator while send the peer data to tracker
            peerMessageStructure = PeerNewData(peerJsonData)
            finalMessageStructure = peerMessageStructure.final()
            print("final message format of the new peer details to the tracker:",finalMessageStructure)
            #send the final message to the tracker
            trackerClient = TrackerClient(trackerTriple,finalMessageStructure)
            trackerClient.trackerClient()



