## Plan of computer networking project ##

Here I will explain the sequence of operation of the system

## Creating Users For making Transactions ##

*  Here the users can be able to register 
*  Only Registered User are allowed to make transaction - that means reciever and sender of doing transaction should be registered in the network
* User can choose any of the node for registration . after the registration the user information is send to all other nodes and information is stored in a database
* At the time of registration each user will assigned a key which is nothing but the sha of the email id they used for registration
* Users can make transaction by using the userid 


## Making Transactions ##

* When user is making a transactions user will enter the amount,user id and user id of the reciever and send it .User can choose any node for making this transactions.After the transactions the information will be shared to all the connected nodes.

* After this all the connected node will add the reward transaction to this transaction and start creating the mining procedure.

* If a node is created the complete blocks, then the node send information to other nodes to stop mining and the block created by the node is broadcasted to the network

* The same procedure repeated in every transactions

* Here for the blocks contain 1 transactions and 1 reward transaction for the miners

## Mining Procedure ##

* When a transaction is happened , then all node will get information about this transaction
* Then, add the transaction details,reward for mining, and hash of previous and then started minining.Store all these data in a dictionary
* First, find the sha of the dictionary created and make the first 4 digits to zero by changing the special number
* When it is done, a message will go to all other nodes that mining completed after created block is add to chain and send to the cconnected nodes
* Chain is same like a linked list -

## Tracker ##
* Tracker job is to identify the nodes connected to the network
* When a node want to join the network  - then it will send the port number and ip address to the tracker
* Tracker will that details from the new node and assign  a unique id to that node and send back the list of connected node to the new   node and all other nodes
* Also the tracker will verify the failures in the network.If a node is desconnected then the tracker will identify that and update the list send the new list to all other nodes
