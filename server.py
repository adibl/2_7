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
ANSWER = 'have a nice day'





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
                    if comm_socket.recv(MAX_PACKET) != '':
                        # we don't care what the client sent us
                        # send the length of the message
                        is_work = protocol.send(comm_socket, ANSWER)
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