from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))
serverSocket.settimeout(12)

last_recv_seq = 0

while True:
    try:
        message, address = serverSocket.recvfrom(1024)
        seq = int(message.decode().split()[1])

        if seq - last_recv_seq > 1:
            for lossSeq in range(last_recv_seq+1, seq):
                print("Loss Number:", lossSeq)

        print("Recv Number:", seq)
        last_recv_seq = seq

    except:
        print("Client Application is terminated!")
        exit(0)