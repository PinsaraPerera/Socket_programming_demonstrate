import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECTED'
SERVER = "add_the_server_ip_addr"
ADDR = (SERVER, PORT)
valid = True

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

while valid:
    def send(msg):
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        client.send(send_length)
        client.send(message)
        print(client.recv(2040).decode(FORMAT))


    send_message = input("Enter the message that you want to send.")
    send(send_message)
    if send_message == DISCONNECT_MESSAGE:
        valid = False
