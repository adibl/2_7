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
LEN_SIGN = 'L' # 4 bytes, number between 0 to 4Mkb
ANSWER = 'have a nice day'


def send(my_socket, massage):
    """
    send massage
    :param:my_socket: the communication socket.
    :param:massage: the massage that hte program send.
    :return: return None if the action seceded.
    if not return the error string.
    """
    packet_len = socket.htons(len(massage))
    err = my_socket.sendall(struct.pack(LEN_SIGN, packet_len))
    if not err is None:
        return err
    err = my_socket.sendall(massage)
    if not err is None:
        return err


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind((IP, PORT))
        server_socket.listen(QUEUE_SIZE)
        # endless loop to receive client after client
        while True:
            comm_socket, client_address = server_socket.accept()
            try:
                if comm_socket.recv(MAX_PACKET) != '':
                    # we don't care what the client sent us
                    # send the length of the message
                    send(comm_socket, ANSWER)
            except socket.error as msg:
                print 'client socket disconnected- ' + str(msg)
            finally:
                comm_socket.close()
    except socket.error as msg:
        print 'failed to open server socket - ' + str(msg)
    finally:
        server_socket.close()

if __name__ == '__main__':
    main()