import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
HOST1 = "192.168.0.12"
PORT = 8080
PORT1 = 80811

FORMAT = 'utf-8'
li = []
test = [(HOST,PORT),(HOST1,PORT1)]
while True:
  k = input("Enter the number:")
  for t in test:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
      t = client.connect(t)
      client.send(k.encode(FORMAT))
      print(t)
      R = client.recv(1024).decode(FORMAT)
      print(R)
    except:
      continue

