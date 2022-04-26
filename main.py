import socket
import sys


HOST = '192.168.0.21'
PORT = 9090


def main():
    counter = 0
    while counter < 5:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pill_time(client_socket)
        counter += 1


def pill_time(client_socket):
    server_address = (HOST, PORT)
    client_socket.connect(server_address)
    data = 'Pill time'
    # Send data to server
    client_socket.send(data.encode())
    client_socket.close()


if __name__ == '__main__':
    main()
