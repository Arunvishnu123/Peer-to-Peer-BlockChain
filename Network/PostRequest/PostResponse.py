import socket
import threading

Host = socket.gethostbyname(socket.gethostname())
Port = 8080
Format = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((Host, Port))
server.listen()

def acceptClient():
   while True:
    client,address =server.accept()
    R = client.recv(1024).decode(Format)
    print(R)
    client.send("Succeed".encode(Format))


test = threading.Thread(target = acceptClient)

test.start()
