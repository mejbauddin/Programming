from socket import *
import sys  
import time  
import datetime

serverSocket = socket(AF_INET, SOCK_STREAM)

serverPort = 8080
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("Server is ready to serve on port", serverPort)

while True:
    
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  

    try:
        
        message = connectionSocket.recv(1024)  
        
        response = "Hello" 

        connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n".encode())
        for i in range(0, len(response)):
            connectionSocket.send(response[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:
        response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<html><body><h1>404 Not Found</h1></body></html>"
        connectionSocket.send(response.encode())

        connectionSocket.close()

serverSocket.close()
sys.exit()  