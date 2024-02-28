from socket import *
from datetime import datetime
import random
import time

clientSocket = socket(AF_INET, SOCK_DGRAM)
sequence_number = 1

while True:

    rand = random.randint(1, 10)

    # 클라이언트가 예기치 않게 종료되었다!
    if rand == 1:
        exit(1)

    # 패킷이 손실되었다!
    if rand == 2 or rand == 3:
        sequence_number += 1

    # 패킷이 정상적으로 전송되었다.
    else:
        send_time = datetime.now().timestamp()
        ping_message = "Ping " + str(sequence_number) + " " + str(send_time)
        clientSocket.sendto(ping_message.encode(), ('127.0.0.1', 12000))
        sequence_number += 1

    time.sleep(4)
