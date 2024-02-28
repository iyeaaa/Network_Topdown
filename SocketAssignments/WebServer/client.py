
import sys
from socket import *

if len(sys.argv) != 4:
    print("the number of arguments is 3")
    exit(1)

serverHost = sys.argv[1]
serverPort = int(sys.argv[2])
requestFile = sys.argv[3]

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverHost, serverPort))
clientSocket.send(("GET /" + requestFile + " HTTP/1.1").encode())

print(clientSocket.recv(1024).decode())
clientSocket.close()
