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
MESSAGE = ['hi', "by"]




def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((SERVER_IP, SERVER_PORT))
        # send the message
        while True:
            massage = []
            massage.append(raw_input("enter action"))
            massage.append(raw_input("enter action"))
            protocol.send(client_socket, massage)
            if massage[0] == "Exit":
                break
            packet = []
            packet = protocol.recv(client_socket)
            print packet[0]+" "+packet[1]
    except socket.error as msg:
        print 'error in communication with server - ' + str(msg)
    finally:
        client_socket.close()


if __name__ == '__main__':
    main()