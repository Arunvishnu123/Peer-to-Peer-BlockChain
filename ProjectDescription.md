# This document describes the technologies and features used in this block-chain application - 

# Blockchain 

# Structure of Block
![title](Images/Strucutre%20of%20the%20Block.png)
# Peer to Peer Network(Architecture used here)
![title](Images/p2pnetwork.png)
# Multi-Threading

# Socket Programming

# Asymmetric Cryptography 
## There are two types of cryptography
* Symmetric Key Cryptography
* Asymmetric key cryptography
Here we are using Asymmetric Key cryptography 
#### Confidentiality and Authentication
* Every node has a Public key and Private Key
* During Sending the message first, the message is encrypted using sender' private key and then again encrypt the message using receivers public key and then send the message
* At the receiver side, receiver decrypt the message first using receivers private key and then again decrypt the message using senders public key.
#### Sending procedure - 
* Encrypted message = Encrypt(message,Private key of sender)
* Final Encrypted message = Encrypt(Encrypted message, Public key of receiver)
#### Receiving Procedure -
* Decrypted message = Decrypt(Final Encrypted message,Private key of Receiver)
* Final Decrypted message = Decrypt(Decrypted message,Public key of Sender)
#### Task need to complete here - 
* Create public key generator for nodes
* Create Private key generator for nodes
* Encryption of the message using private and public key of receiver and sender simultaneously
* Decryption of the message using private and public key of sender and receiver simultaneously

### But here we couldn't able to follow the above procedure.Here we used "rsa module" which is used to encrypt the message only using the receiver public key  and decrypt the message using the reciever's private key for confidentiality and also,w e give a digital signature which is created using the senders private key and message which can be validation using the sender public key 
# Message Queue System

# Sqlite Database