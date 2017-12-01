"""
author - cyber
date   - 29/11/17
socket server
"""
import socket
import struct
import protocol

IP = '0.0.0.0'
PORT = 20003
QUEUE_SIZE = 1
MAX_PACKET = 2
SHORT_SIZE = 2
ANSWER = ['have a nice day', "go"]


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind((IP, PORT))
        server_socket.listen(QUEUE_SIZE)
        # endless loop to receive client after client
        while True:
            comm_socket, client_address = server_socket.accept()
            while True:
                try:
                    request = protocol.recv(comm_socket)
                    if request[0] == "Exit":
                        comm_socket.close()
                        break
                    # add request to answer function call
                    is_work = protocol.send(comm_socket, request)
                    if not is_work:
                        comm_socket.close()
                        break
                except socket.error as msg:
                    print 'client socket disconnected- ' + str(msg)
                    comm_socket.close()
                    break
    except socket.error as msg:
        print 'failed to open server socket - ' + str(msg)
    finally:
        server_socket.close()

if __name__ == '__main__':
    main()