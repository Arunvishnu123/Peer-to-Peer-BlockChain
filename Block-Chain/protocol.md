# CHEESECOIN PROTOCOL
## PEERS
Every peer is identified by:
- **Network identifier**.
  - An integer (no encryption), or
  - A public key (if encryption added).
- **IP address and Port Number**.

Every peer in the network is equal. A peer acts both as a TCP server - as it accepts other peers' connections - and as a client since it connects to the tracker for peer discovery and to other peers for broadcasting newly found cheeses.

Peers can:
- **Interact with other peers**.
  - By broadcasting new cheeses.
  - To (potentially) perform currency transactions.
  - To ask for an updated version of the cheesechain.
- **Communicate with the tracker**.
  - When a new peer joins the network, it has to first notify the tracker of its existence for the tracker to record his information (ID, IP address, port) and allow it to give it to other peers afterward.
  - After a peer has notified the tracker of its joining, it has to ask for other existing peers to actually be able to join the P2P network by connecting them.
  - A peer shall respond to keep-alive messages sent periodically (every 30 or 60 seconds) by the tracker for being able to maintain up-to-date information about the online peers.
- **Mine**.
  - This would be the main task of the peers.
  - The goal of a peer is to find the new valid cheese.
    * A cheese is valid when its smell starts by D number of zeros. 
    * D is called the difficulty and it is **fixed**.
  - The first transaction of every cheese is an special transaction, and it is a reward for mining it. The amount of this reward will be fixed. To make sure that the amount of this reward has not changed, other peers will verify it when verifying the whole block.
  - When a peer finds a new valid cheese, it will broadcast it to all other peers.

The different tasks a peer can do (explained above) shall be contained within different threads and should be run concurrently, and to handle mutual exclusion blocking queues (or a similar tool) will be used.

## TRACKER
There is only one tracker in the whole network and it will be a TCP Server that will work as a Peer-Index Network Database. The tracker might not record any information regarding the cheesechain nor take part in the mining process.

Its task is simply to maintain updated information of the online peers and help peers discover each other in the network by resolving their requests.

## CHEESE
The basic unit of information, encoded as a JSON String.

## Protocol Specification ##

## Message types  in the system ##

1. Request 
2. Response

## Request -  

## Message format  - [RequestMethod][MessageTypes][Data/Arguments]

# 1. Request Method  - Two type request methods are here 

  |Request Keyword|Request Method|Description|
  |---------------|--------------|------------|
  |G|Get|To receive data from the nodes|
  |P|Post|To Send data to the nodes|

    * here mostly "Post request" are used and rarely the get request is been used

# 2. MessageTypes  - Here Mainly 10 message types are defined which will be discussed more in details in the comming explanation  - Here firt letter of each message type is used in the Full Message Format.

| Message Type | Message Name |Request Type | Description | Payload |
| ------------- | ------------- |------------- |------------- | ------------- |
P | Ping | Post |Sent from one peer to another to make sure that it is online before trying to establish a TCP connection | Random nonce | 
K | KeepAlive | Post |The tracker will send periodically this messages to the peers to check their status | Random nonce received as response |  
N | NewBlock | Post|A peer will broadcast this message when discovering a new valid cheese | JSON String representation | 
T | Transaction | Post |A peer will broadcast this message when performing a transaction for the other peers to validate it and include it into the cheesechain | JSON string representation|
H | History | Get|Get the history of blocks in the individual nodes | JSON string representation |
L | LastHash | Post |Get the hash of last created blocks  | JSON string representation |
J | Join | Post |Broadcast the new node details to the tracker from the new node  | JSON string representation|
S | SendNodeData | Post|Broadcast the new node details to the peers  | JSON string representation |
L | TransactionLedger | Post | Full transaction message to adding it in the transaction ledger | JSON string representation |
M | MineComplete |Post |Send the Mining complete status to the other peers | JSON string representation |

* payload information and  explaination of  all types of  request and corresponding response will discussed in details in the coming section.

# 3. [Data/Arguments] - The data/argument is the content which need to be send or receive by the nodes.Here the message is of simple json format.Here Data or argument which deppends on the type of request method([get or post]).

    Example of a  json data - 
       {
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
# [StatusCode] -  
*  Here the sender get the code meesage deppends of the situations.For example if the reciever succesfully recived the message then the  sender get the status  - 200

# 2. [Post][Join][Data] - 
            Here when a node was added to the existing network ,then the new node will send it ip address and port number to the tracker server.Tracker will add the node details to the network list.
            sample message - 
            {
                "ipaddress" - "192.168.1.2",
                "portnumber" - "502"
            }
# Response for this request  - 
# [StatusCode][Data] - 
     Here the node will get the status and some data as response.Here,most probably the status code will 201, which is "Created" or 408,  which is request timed out. here the data contain the nodeid of the new node in the network
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


