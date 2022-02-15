## Implementation a blockchain peer-to-peer system inspired by Bitcoin ##

The Block Chain peer to peer system consists of two types of members - 

*  Tracker - The server which maintains the updated list which contains the details of IP address, Port Number, Id of the individual nodes. Also, the tracker will send this information to nodes when the demands come. Moreover, the tracker will monitor the communication status of each node in the connected network.

*  Nodes - In a BlockChain, all the nodes are synchronized with each other for sending and receiving information. Making money transactions with the individual nodes, Sending the transaction details to all other nodes, validation of transaction, creating the blocks etc. are the certain features of each node.

## Protocol Specification ##

## Message types  in the system ##

1. Request 
2. Response

## Request -  

## Message format  - [RequestMethod][DataType][Data/Arguments]

# 1. Request Method  - Two type request methods are here 

  1. Get method  - To receive data from the nodes 
  2. Post method  - To send data to the nodes

# 2. DataTypes  - Here Mainly 8 datatypes are defined which will be discussed more in details in the coming explanation  - Here pascalcase format is used in defining the datatypes.

*  Transaction - Details the transactions or message send by the individul nodes
*  Join - When a node is added to the network
*  KeepAlive - Check the communication status of each nodes in the network
*  Win - Broadcast a block to all the nodes
*  History - get the history of blocks in the individual nodes
*  LastHash - get the hash of last created blocks
*  FetchConnected - send nodeid to the tracker to get the port number and ip address to make the transaction

# 3. [Data/Arguments] - The data/argument is the content which need to be send or receive by the nodes.Here the message is in simple json format. Here Data or argument which deppends on the type of request method([get or post]).

    Example of a  json data - 
       {
        "nodeid":1,
        "ipaddress:"192.168.1.1",
        "portnumber:"502"
        }


## Repsonse -

## Response message format  - [StatusCode][Data]

1. StatusCode - Here the http standard codes are used.
   For Example  - 
           1. 200 - Ok
           2. 201 - Created
           3. 400 - Bad Request
           4. 404 - Not Found


2. Data  - Here data is same as the request type and is of json format.This optional in every messages


## Explanations and Examples of different types requests and corresponding responses - 

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
# [StatusCode] -  
*  Here the sender gets the code message depending on the situations. For example, if the receiver successfully received the message then the  sender get the status  - 200

# 2. [Post][Join][Data] - 
            Here when a node was added to the existing network, then the new node will send its IP address and port number to the tracker server. Tracker will add the node details to the network list.
            sample message - 
            {
                "ipaddress" - "192.168.1.2",
                "portnumber" - "502"
            }
# Response for this request  - 
# [StatusCode][Data] - 
     Here the node will get the status and some data as response. Here, most probably the status code will be 201, which is "Created" or 408,  which is a request timed out. here the data contain the nodeid of the new node in the network
     sample message - 
     {
         "nodeid":7,
         "status":"active"
     }

# 3.[Get][KeepAlive] - 
      Here the KeepAlive is  used to check the communication status of the connected nodes in the network.

# Response of this request - 
# [StatusCode][Data] -
      This repsonse contain the status code which is 200 - Ok or 404 - not found  and Data and the code is 200 then it contain a data in json format.
      sample message - 
      {
          "nodeid":"34",
          "status":"online"
      }

# 4.[Post][Win][Data] - 
    This is used to broadcast the created blocks to all nodes in the network.
    sample message format - 
    {[{
      "transactionid:"232",
      "sender":"Arun",
      "receiver":"Vishnu,
      "timestamp":39043949230,
      "amount":20
    },------],
    "hashnumber":"000000SDSDUFEFUEFUEFIEJD",
    "specialnumber":30930490349
    }

# Response of this request -  
# [StatusCode] - 
    This contain mainly 200 - success or 400 - bad request



