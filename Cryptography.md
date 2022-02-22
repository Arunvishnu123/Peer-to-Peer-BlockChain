## Cryptography ##

# There  are two types of cryptography 

* Symmetric Key Cryptography
* Assymmetric key cryptography

Here we are using Assymmetric Key cryptographic


### Confidentiality and Authentication ###

*  Every node has a Public key and Private Key

* During Sending the message first, the message is encrypted using sender' private key and then again encrypt the message using receivers public key and then send the message

* At the reciever side, reciever decrypt the message first using recivers private key and then again decrypt the message using senders public key

# Sending procedure  - 

* Encripted message = Encrypt(message,Private key of sender)
* Final Encripted message = Encrypt(Encripted message, Public key of receiver)

# Receiving Proceduer - 

* Decrypted message = Decrypt(Final Encrypted message,Private key of Receiver)
* Final Decrypted message = Decrypt(Decrypted message,Public key of Sender)

## Task need to complete here

* Create public key generator for nodes
* Create Private key generator for nodes
* Encryption of the message using private and public key of receiver and sender simultaneously
* Decryption of the message using private and public key of sender and receiver simultaneously




