## Implementation a blockchain peer-to-peer system inspired by Bitcoin ##

The Block Chain peer to peer system consists of two types of members - 

* 1. Tracker - The server which maintain the updated list which conatin the details of IP address,Port Number,Id of the individual nodes.Also the tracker will send this infomation to nodes when the demands comes.Moreover,the tracker will monitor the communication status of each nodes in the connected network.

* 2. Nodes - In a Block Chain, all the nodes are synchronized with each other for sending and receiving information.Make money   transactions with the indvidual nodes,Sending the transaction details to all other nodes,validation of transaction , creating the blocks etc are the certain features of each nodes.

## Protocol Specification ##

## Message types  in the system ##

1. Request 
2. Response

## Request -  

## Message format  - [RequestMethod][DataType][Data/Arguments]

1. Request Method  - Two type request methods are here 

# 1. Get method  - To receive data from the nodes 
# 2. Post method  - To send data to the nodes

2. DataTypes  - Here Mainly 8 datatypes are defined which will be discussed more in details in the comming explanantion  - Here pascalcase format is used in defining the datatypes.

* 1. Transaction - Details the transactions or message send by the individul nodes
* 2. Join - When a node is added to the network
* 3. KeepAlive - Check the communication status of each nodes in the network
* 4. Win - Broadcast a block to all the nodes
* 5. History - get the history of blocks in the individual nodes
* 6. LastHash - get the hash of last created blocks
* 7. FetchConnected - send nodeid to the tracker to get the port number and ip address to make the transaction

3. Data/Arguments - The data/argument is the content which need to be send or receive by the nodes.Here the message is of simple json format.Here Data or argument which deppends on the type of request method([get or post]).

* Example of a  json data - 

- {
    "nodeid":1,
    "ipaddress:"192.168.1.1",
    "portnumber:"502"
 }


## Repsonse -

## Response message fomat  - [StatusCode][Data]

1. StatusCode - Here the http standard codes are used.
   For Example  - 
           1. 200 - Ok
           2. 201 - Created
           3. 400 - Bad Request
           4. 404 - Not Found


2. Data  - Here data is same as the request type and is of json format.This optional in every messages


## Explanations and Examples of differnent types requests and correpsonding reponses - 

# 1. [Post][Transaction][Data] - 
               Here the transaction information is send to the receiver node.
               sample message  - 
               {
                   "sendername":"Arun",
                   "transactionnumber":1,
                   "amount":"10",
                   "receivername":"vishnu",
                   "publickey":"SDOJDUB"
                   "timestamp":"12323209203"
                   
                }

# Reponse for this request  - 
# [StatusCode] 
              Here the sender get the code meesage deppends of the situations.For example if the reciever succesfully recived the message then the sender get the status  - 200











