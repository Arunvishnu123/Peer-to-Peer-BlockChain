from BlockChain.Database.CreateDatabase import Database
from BlockChain.Database.PeerDetails import PeerDetailsTable
from pathlib import Path

if Path('./Blockchain/Database/BlockChain.db').is_file():
    print ("DataBaseAlreadyCreated")

else:
    print("File not exist")
    dataBaseCreation = Database()

createPeerTable = PeerDetailsTable()
createPeerTable.createTable()



