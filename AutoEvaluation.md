# Initial Objective and plan of completing the project

* Create the structure of the Block which need to be generated
* Implement the blockchain, without networking, without currency transactions (the data can be any message with no particular semantic).
* Implement the mining aspects of the block and it in the chain.
* Testing of creating a peer to peer network with much logic (for sending some random messages)
* Create the protocol document for the BlockChain.By considering the needs of the blockchain working
* Create the tracker server for Blockchain application which help add the new node the network
* Develop socket programming for sending and receiving messages from other peers and also trackers
* Create the message format as per the protocol document  for identifying the message type when sending and receiving
* List out the modules required for the application and structure them properly for keep good programming standards

## Work Plan - 

We have multiple team  meetings to define the use cases of the blockchain system  and design the execution strategy and finally the table below shows our priorities from top to bottom

|Task defined initially|
|---------------|
|Create the protocol Document|
|Design the Structure of the Block|
|Design the modules required to develop the above block structure|
|Learn and Work with the Asymmetric Cryptography and do the testing for implementing it in the BlockChain|
|Study about Socket programming and do the required testing in it|
|Study about the Peer-Peer Networking and also, design the implementation plan using socket programming|
|Study about the concurrent programming and also, do the required testing using the python for using in it the BlockChain project|
|Select the database for storing the data and do the required testing and develop the modules for doing CRUD operations|
|Develop modules for creating the message structure for sending side and also, for destructuring the message at the receiving side as per the protocol document|
|Create the module for sending and receiving messages from other peers|
|Design the Tracker logic in the system |
|Study about the Message Queueing System and Design the logic to implement it in the project|

# Sequence of Operation - 

## Peers
* First Tracker should be in online 
* Connect new peer to the tracker one by one and send the new information which contain Public Key,IPAddress,Name,Port Number.
* Tracker will receive this information and store it in the local database and same time it will send to all other peers
* Each peer can send messages and money to any peers connected in the network
* During the transaction the local database of the peer will provide the list of connected peers
* Peer can select the name from the list and Enter the message and amount
* After this the peer will do encryption of the message based on the Asymmetric cryptography using the private and public key of the sender and receiver respectively
* After this the sender peer will convert this into the message format as per protocol document and send to the receiver
* When the peer receive the message then first convert the message into its form 
* Then decrypt the message and at the same time do the validation of the transaction and add the transaction to it local db
* If the validation is successful then, the receiver the broadcast the transaction to all other connected peers 
* Each peer will receive this message and add it the ledger table in the database 
* When any peer can give  command for mining and creating the block and add to the chain
* At first, peer will create the block as per structure defined earlier using the transactions in the ledger 
* Then do the Proof of Work as per the difficulty target and calculate the nonce 
* When the Mining is complete then the peer will check  any "MiningComplete" status from other peer
* If there is not "MiningComplete" status then send the block other peers 
* Other peer receives this block and add it to the blockchain
* Also, here Genesis Block also called "RacletteCheese" will created by the first peer connected to the network
* Also there is message queue system in the block,The working is when a the peer try to send the created block to other peers, at this time, any failure instance occur then that message and connection information will be logged into a database
constantly the peer try to send the message in the database
* Also, new peer can request the blockchain history

# Tracker
* Tracker will accept the new peer details and distribute it to all other peers
* Tracker there is one message queue system - Working is that when the tracker broadcast the new node details according the peer list in there local database to other peer, then any failed case occur when try to connect to ta peer then the message and the connection information of that peer will log into another table in the database
* Constantly the tracker will send the message in the queue according the connections
* Tracker will check the communication status of each peer in the network according to the peer list in the tracker 
* If the tracker find out any peer is offline then the tracker send this peer details(it can be one or many ) to other connected peers 
* Peers will receive this information and delete the connection details of the offline peers from the database

# What Works on the Tracker

 |Features|Status|Remarks|
 |---------------|--------------|-------------|
 |Features|Status|Remarks|

# What Works on the Peers

 |Features|Status|Remarks|
 |---------------|--------------|-------------|
 |Features|Status|Remarks|

# Time Spent for each member and their contribution

 |Member Name|Part which each member worked|Time spend in hours|
 |---------------|--------------|-------------|
|Arun Raveendran Nair Sheela|Block Chain creation,Designing,Network Programming,Tracker,Testing,Research|~80 hours|

# Good Development Practices Followed
|   Class    |   Practises followed   |
|-------|--------|
|   Class    |   Practises followed   |


    