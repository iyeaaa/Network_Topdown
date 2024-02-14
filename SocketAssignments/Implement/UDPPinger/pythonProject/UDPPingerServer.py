# UDPPingerServer.py
# randomized lost packets를 생성하기 위해 필요한 모듈 import
import random
from socket import *

# UDP 패킷을 생성하기 위한 UDP 소켓 생성
serverSocket = socket(AF_INET, SOCK_DGRAM)

# IP 주소와 포트 번호를 소켓에 할당
serverSocket.bind(('', 12000))

while True:
    # 0에서 10 사이의 랜덤한 숫자 생성
    rand = random.randint(0, 10)

    # 클라이언트로부터 패킷 수신
    message, address = serverSocket.recvfrom(1024)

    message = message.decode().upper()

    if rand < 4:
        continue
    # 랜덤한 숫자가 4보다 크거나 같은 경우, 클라이언트에게 응답 전송
    # 즉 4 ~ 10 사이의 숫자가 나오면 응답을 전송하므로, 70%의 확률로 응답을 전송한다.
    serverSocket.sendto(message.encode(), address)