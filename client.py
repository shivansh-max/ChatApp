# IMPORTS
import socket

# Port, Header, Disconnection Message Format, SERVER, ADDR config
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECTION_MESSAGE = "<!Disconnect!>"
SERVER = "192.168.0.6"
ADDR = (SERVER, PORT) 

# Socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_length = str(msg_len).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hello")
input()
send("Today is awesome I finnaly learned sockets")
input()
send("See it works")
input()
send(DISCONNECTION_MESSAGE)