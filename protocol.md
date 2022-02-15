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
The basic unit of information, encoded as a JSON object.

The main structure of cheese is the following:

| Size | Field | Description |
| ------------- | ------------- | ------------- |
| 4 bytes | Cheese size | The cheese size specified in bytes |
| 44 bytes | Cheese headers | Cheese metadata |
| 4 bytes | Transaction counter | The number of transactions included in the cheese |
| Variable | Transactions | The actual list of transactions' hashes. A peer has to validate the transactions before including them in a new cheese. Note that this list cannot be empty. |


The structure of a cheese's headers is the following:

| Size | Field | Description |
| ------------- | ------------- | ------------- |
| 32 bytes | Previous cheese smell | The smell of the previous cheese in the chain |
| 4 bytes | Timestamp | Creation time of this cheese |
| 4 bytes | Sequence number | Number of ancestors |
| 4 bytes | Nonce | Randomly-generated number to ensure proof-of-work |

```json
{
  "size" : 5425,
  "previouscheesesmell" :"0000000099f9738551d34f8899cd2ad76da627c3",
  "timestamp" : 1644683223,
  "seqnumber" : 2,
  "nonce" : 8903358604,
  "txcounter" :2,
  "tx" : [
      "257e7497fb8bc68421eb2c7b699dbab234831600e7352f0d9e6522c7cf3f6c77",
      "05cfd38f6ae6aa83674cc99e4d75a1458c165b7ab84725eda41d018a09176634"
  ]
}
```
Example of a cheese in the Cheesecoin protocol.

### RACLETTE CHEESE
This is a special kind of cheese that does not follow all of the mentioned constraints. The Raclette cheese is the **first** cheese in the cheesechain. It has a predefined content, known by all peers joining the network (it will be hard-coded for the sake of simplicity). In this cheese, we will observe some exceptions:
1. It has no parent cheese as it represents the origin of the chain.
2. Its sequence number will be 0.


## CHEESECHAIN
Every peer must maintain a local copy of the full cheesechain. This copy is constantly updated by receiving new cheeses from other peers, that obviously have to be validated before being added to the chain.

For a new cheese to be valid, it has to:
-  The cheese structure is valid.
-  The cheese header hash is less than the difficulty.
-  The first transaction (and only the first) is a reward transaction.
-  All transactions within the cheese are valid.

## MESSAGES
The format for the protocol messages will be simple: messages will consist of a message type identifier, encoded within 4 bytes (2^4 > 9) and the message payload, of variable size.

| Message type | Message name  | Description | Payload |
| ------------- | ------------- | ------------- | ------------- |
0 | ping | Sent from one peer to another to make sure that it is online before trying to establish a TCP connection | Random nonce | 
1 | pong | Response to the ping message | Random nonce received |
2 | keepalive | The tracker will send periodically this messages to the peers to check their status | Random nonce | 
3 | imalive | A peer's response to a keepalive message from the tracker | Random nonce received | 
4 | newcheese | A peer will broadcast this message when discovering a new cheese | JSON representation of the cheese | 
5 | transaction | A peer will broadcast this message when performing a transaction for the other peers to validate it and include it into the cheesechain | JSON representation of the transaction |
6 | getdata | A peer may query other peers or the tracker | The query: a peer may ask other peers about known cheeses or the tracker for a list of online peers |
7 | cheese | A peer's response to a query from a peer about cheeses | JSON representation of the cheeses |
8 | peers | The tracker's response to a query about online peers | JSON object with information about the online peers |

## TRANSACTION
The peers can send one transaction to only one other peer at a time.

<!-- Every transaction has a fixed amount of cheesecoins (to be defined later) as a reward for the miner that will include it in its block. -->

| Size | Field | Description |
| ------------- | ------------- | ------------- |
| 4 bytes | Amount | The amount of cheesecoin to send |
| 4 bytes | From | The sender identifier (ID or Public key) |
| 4 bytes | To | The receiver identifier (ID or Public key) |
| 4 bytes | Timestamp | Creation time of the transaction |
| 1 bit | Status | The status of the transaction (0=Unconfirmed, 1=Confirmed) |
| 32 bytes | Hash | The transaction's hash (using SHA-1) |
| variable | Size | The size of the transaction in bytes |
