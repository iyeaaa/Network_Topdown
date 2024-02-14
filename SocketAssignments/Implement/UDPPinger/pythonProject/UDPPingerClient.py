import socket
from socket import *
from datetime import datetime

# UDP 패킷을 생성하기 위한 UDP 소켓 생성
clientSocket = socket(AF_INET, SOCK_DGRAM)

for i in range(1, 11):
    try:
        sequence_number = str(i)
        sendTime = datetime.now()
        message = "Ping " + sequence_number + " " + str(sendTime)

        clientSocket.settimeout(1)
        clientSocket.sendto(message.encode(), ("", 12000))
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        recvTime = datetime.now()

        diffTime = recvTime - sendTime
        print(sequence_number, "\tRTT:", diffTime, "\tmessage:", modifiedMessage.decode())

    except:
        print(i, "\tRequest timed out")

clientSocket.close()