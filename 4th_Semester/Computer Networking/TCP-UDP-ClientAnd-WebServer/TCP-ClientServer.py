from socket import *
serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

while True:
    msg = input("Enter message: ")
    clientSocket.send(msg.encode())
    if msg == "!quit":
        break
    print("Server says:", clientSocket.recv(1024).decode())

clientSocket.close()