# IMPORTS
import socket
import threading

# Port, Server, Header, Address, Disconnection Message Format config
HEADER = 64
PORT = 5050
SERVER = "192.168.0.6"
ADDR = (SERVER, PORT) 
FORMAT = 'utf-8'
DISCONNECTION_MESSAGE = "<!Disconnect!>"

# Creating the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# Loggin function
def log(tag, value):
    print(f"[{tag}] {value}")

# Handling the client
def handle_client(conn, addr):
    log("NEW CONNECTION", f"{addr} connected")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            log(addr, f"{msg}")
            conn.send("Msg Received".encode(FORMAT))
    conn.close

# Starting the server function
def start():
    # Listening for new connection
    server.listen()
    log("LISTINGIN", f"server is listening on http://{SERVER}:{PORT}/")
    while True:
        # Getting the connection and then the address then handling the connection
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args= (conn, addr))
        thread.start()
        log("ACTIVE CONNECTIONS", (threading.activeCount() - 1))


# Starting the server
log("STARTING", "starting the server ...")
start()