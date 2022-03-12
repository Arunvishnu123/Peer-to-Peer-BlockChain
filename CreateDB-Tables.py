from BlockChain.Database.CreateDatabase import Database
from BlockChain.Database.PeerDetails import PeerDetailsTable
from BlockChain.Database.Transactions import TransactionsDT
from BlockChain.Database.Ledger import TransactionsLedgerDT
from pathlib import Path


if Path('./Database/BlockChain.db').is_file():
    print ("DataBaseAlreadyCreated")

else:
    print("File not exist")
    dataBaseCreation = Database()
###################################################################################
#create peer tables
createPeerTable = PeerDetailsTable()
createPeerTable.createTable()
###################################################################################
#create transaction datatable
createTransactionTable  =  TransactionsDT()
createTransactionTable.createTable()
###################################################################################
#create transaction ledger table
createLedgerDT = TransactionsLedgerDT()
createLedgerDT.createLedgerTable()




