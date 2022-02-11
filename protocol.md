## Implementation a blockchain peer-to-peer system inspired by Bitcoin ##

The Block Chain peer to peer system consists of two types of members - 

## 1. Tracker - The server which maintain the updated list which conatin the details of IP address,Port Number,Id of the individual nodes.Also the tracker will send this infomation to nodes when the demands comes.Moreover,the tracker will monitor the communication status of each nodes in the connected network.

## 2. Nodes - In a Block Chain, all the nodes are synchronized with each other for sending and receiving information.Make money transactions with the indvidual nodes,Sending the transaction details to all other nodes,validation of transaction , creating the blocks etc are the certain features of each nodes.

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

# 1. Transaction 
# 2. Ping
# 3. Join
# 4. KeepAlive
# 5. Win
# 6. History
# 7. LastHash
# 8. FetchConnected

3. Data/Arguments - The data/argument is the content which need to be send or receive by the nodes.Here the message is of simple json format.Here Data or argument which deppends on the type of request method([get or post]).

## Example of a  json data - 

- {
    "nodeid":1,
    "ipaddress:"192.168.1.1",
    "portnumber:"502"
 }


## Repsonse -

## Response message fomat  - [StatusCode][Data]

1. Code - 



