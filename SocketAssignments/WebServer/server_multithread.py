
from socket import *
from threading import *


def sendmessage(connectionsocket: socket):
    try:
        message = connectionsocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        f.close()

        connectionsocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionsocket.send("\r\n".encode())
        connectionsocket.send(outputdata.encode())
        connectionsocket.send("\r\n".encode())

        connectionsocket.close()

    except IOError:
        connectionsocket.send("HTTP/1.1 404 Not Found".encode())
        connectionsocket.send("\r\n".encode())
        connectionsocket.close()


# Welcome Socket 생성
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", 80))
serverSocket.listen(40)

while True:
    print("Ready to serve...")

    # connectionSocket : 핸드셰이킹동안 생성한 연결소켓이다.
    connectionSocket, addr = serverSocket.accept()
    Thread(target=sendmessage, args=[connectionSocket]).start()