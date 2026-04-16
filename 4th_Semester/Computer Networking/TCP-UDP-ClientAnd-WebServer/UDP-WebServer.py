from socket import *
import datetime

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(10)
print("Server is listening...")
conn, addr = serverSocket.accept()

     
     
while True:
    msg = conn.recv(1024).decode()
    if not msg:
        break

    print(f"[{datetime.datetime.now()}] Client {addr} sent: {msg}")
    if msg == "!time":
        conn.send(str(datetime.datetime.now()).encode())
    elif msg.startswith("!echo "):
        serverSocket.send(msg[6:].encode())
    elif msg == "!quit":
        conn.send("Goodbye!".encode())
        break
    else:
        response = f"Sending Time : {str(datetime.datetime.now())} \n Hello BOSS, You are asking me : {msg}"

    conn.send(response.encode())

conn.close()
