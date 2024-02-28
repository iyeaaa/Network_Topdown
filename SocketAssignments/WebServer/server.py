
from socket import *

# Welcome Socket 생성
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", 80))
serverSocket.listen(1)

while True:
    print("Ready to serve...")

    # connectionSocket : 핸드셰이킹동안 생성한 연결소켓이다.
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        f.close()

        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(outputdata.encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()

    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
