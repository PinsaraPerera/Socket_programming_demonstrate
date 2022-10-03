import socket
import threading

HEADER = 64  # This represents the length of the msg coming from client(64 bit)
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())  # this will gives the local ipv4 address
ADDR = (SERVER, PORT)  # have to give as a tuple
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECTED'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET is the family of the socket which can used to use ipv4
# socket.SOCK_STREAM is the socket type which we use to stream data through this socket

# binding the server to socket
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} is connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)  # decode the msg to utf-8 format (byte --> string)
        if msg_length:
            msg_length = int(msg_length)  # convert into the integer form
            msg = conn.recv(msg_length).decode(FORMAT)  # this is the actual msg .recv(size of the msg)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            msg_back = input("enter the message...\n")
            conn.send(msg_back.encode(FORMAT))

    conn.close()


def start():  # This function will handle every connection
    server.listen()  # this will listen to a new connection
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        # this will block statement so we use threading up now
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        # Declaring one thread to one client
        thread.start()
        # These threading module is only can be used in python3
        print(f"[ACTIVE CLIENTS] {threading.active_count() - 1}")

        # To know how many clients are connected to the server.
        # Already one thread is working to catch up the connections that's why we subtract one(-1)


print("[STARTING] server is starting...")
start()
