from BlockChain.Network.TrackerClient.client import TrackerClient
import threading
ip = "192.168.0.13"
port = 7070
connection = (ip,port)
####################################################################################################
if __name__ == "__main__":
    trackerClient = TrackerClient(connection)
    # select the operation need to do by the system
    while True:
        print("Enter C or c to connect to the peer at the first time(means connect to the tracker)")
        operation = input("Select the operation need to do:")
        if operation == "C" or operation == "c":
            trackerClient.trackerClient()
