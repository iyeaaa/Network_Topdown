from socket import *
from datetime import datetime

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
rttlist = []
losscnt = 0

for sequence_number in range(1, 11):
    send_time = datetime.now().timestamp()
    ping_message = "Ping " + str(sequence_number) + " " + str(send_time)
    clientSocket.sendto(ping_message.encode(), ('127.0.0.1', 12000))

    try:
        message = clientSocket.recv(1024)
        timeDiff = datetime.now().timestamp() - send_time
        rttlist.append(timeDiff)
        print(sequence_number, "RTT:", timeDiff)

    except:
        print(sequence_number, "Request timed out")
        losscnt += 1

print()

if rttlist:
    print("minimum:", min(rttlist))
    print("maximum:", max(rttlist))
    print("average:", sum(rttlist)/len(rttlist))
    print("loss rate:", str(losscnt/10*100) + "%")

clientSocket.close()
