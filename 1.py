import socket
import threading
from time import sleep

PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.2.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
connected = True

def handle_rev(client):
    global connected
    while connected:
        msg = client.recv(1024).decode(FORMAT)
        print(msg)
        print(len(msg))

def handle_send(client):
    global connected
    while connected:
        msg = input('C01>')
        send("[Client 01] " + msg)
        if msg == DISCONNECT_MESSAGE:
            connected = False

def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)

thread = threading.Thread(target=handle_rev, args=(client,))
thread.start()

thread = threading.Thread(target=handle_send, args=(client,))
thread.start()

while connected:
    #Xử lý chính
    sleep(2)

