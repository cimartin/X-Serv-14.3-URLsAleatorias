#!/usr/bin/python3


import socket
import random



mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1235))
mySocket.listen(5)


try:
    while True:
        num_al = random.randrange(100000) 
        print ('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print ('Request received:')
        print (recvSocket.recv(2048))
        print ('Answering back...')
        recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                        "<html><body><h1>Hello World!</h1>" +
                        "<a href='"  + str(num_al)  +"'>Dame otra url</a>"  +
                        "</body></html>" +
                        "\r\n",'utf-8'))
        recvSocket.close()
except KeyboardInterrupt:
    print ("Closing binded socket")
mySocket.close()