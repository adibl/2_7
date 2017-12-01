"""
author - adi bleyer
date   - 29/11/17
socket client
"""
import socket
import struct
import protocol

SERVER_IP = '127.0.0.1'
SERVER_PORT = 20003
MESSAGE = 'hi'




def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((SERVER_IP, SERVER_PORT))
        # send the message
        protocol.send(client_socket, MESSAGE)

        packet = protocol.recev(client_socket)
        print packet
    except socket.error as msg:
        print 'error in communication with server - ' + str(msg)
    finally:
        client_socket.close()


if __name__ == '__main__':
    main()