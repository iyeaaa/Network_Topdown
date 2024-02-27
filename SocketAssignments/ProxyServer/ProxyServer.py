from socket import *
import sys
#
# if len(sys.argv) <= 1:
#     print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
#     sys.exit(2)

# Create a server socket, bind it to a port and start listening

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(("", 8558))
tcpSerSock.listen()

while 1:
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)
    message = tcpCliSock.recv(1024).decode()

    filename = message.split()[1].partition("/")[2]

    fileExist = "false"
    filetouse = "/" + filename

    try:
        f = open(filename, "r")
        outputdata = f.read()
        fileExist = "true"

        tcpCliSock.send("HTTP/1.0 200 OK\r\n".encode())
        tcpCliSock.send("Content-Type:text/html\r\n\r\n".encode())
        tcpCliSock.send(outputdata.encode())
        tcpCliSock.send("\r\n".encode())

        print('Read from cache')

    except IOError:
        if fileExist == "false":
            # Create a socket on the proxyserver
            c = socket(AF_INET, SOCK_STREAM)

            domain = filename.replace("www.", "")
            filen = domain.partition("/")[2]
            hostn = domain.partition("/")[0]

            try:
                sendmessage = "GET /" + filen + " HTTP/1.1\r\n"
                sendmessage += "Host: " + hostn + "\r\n"
                sendmessage += "\r\n"

                c.connect((hostn, 80))
                c.sendall(sendmessage.encode())
                newmessage = c.recv(1024).decode()

                print(newmessage)

                tmpfile = open(filename, "wb")
                tmpfile.write(newmessage)
                tmpfile.close()

                tcpCliSock.send(newmessage.encode())

            except:
                print("illegal")

        else:
            pass
            # HTTP response message for file not found
            # Fill in start.
            # Fill in end.

        # Close the client and the server sockets
    tcpCliSock.close()

# Fill in start.
# Fill in end.
