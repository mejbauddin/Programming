from socket import *
import sys  
import time  
import datetime

serverSocket = socket(AF_INET, SOCK_STREAM)

serverPort = 1200
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("Server is ready to serve on port", serverPort)

while True:
    
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  

    try:
        
        message = connectionSocket.recv(1024)  
        if not message:
            continue

        filename = message.split()[1]
        print(f"Requested file: {filename}")

        log_entry = f"{datetime.datetime.now()} - Client {addr[0]} requested {filename}\n"
        print(log_entry.strip())

        f = open(filename[1:], 'r') 
        outputdata = f.read()
        f.close()

        connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n".encode())

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:
        response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<html><body><h1>404 Not Found</h1></body></html>"
        connectionSocket.send(response.encode())

        connectionSocket.close()

serverSocket.close()
sys.exit()  

