"""
author - adi bleyer
date   - 29/11/17
socket client
"""
import socket
import struct
import protocol
from gio._gio import network_address_parse

SERVER_IP = '127.0.0.1'
SERVER_PORT = 20003
MESSAGE = 'hi'
HEADER_LEN = 4
LEN_SIGN = 'L'


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((SERVER_IP, SERVER_PORT))
        # send the message
        sent = 0
        while sent < len(MESSAGE):
            sent += client_socket.send(MESSAGE[sent:])
        # receive the message length
        net_len = ''
        while len(net_len) < HEADER_LEN:
            net_packet = client_socket.recv(HEADER_LEN - len(net_len))
            if net_packet == '':
                net_len = ''
                break
            net_len += net_packet
        if net_len != '':
            packet_len = socket.ntohs(struct.unpack(LEN_SIGN, net_len)[0])
            # receive the actual message
            packet = ''
            while len(packet) < packet_len:
                buf = client_socket.recv(packet_len - len(packet))
                if buf == '':
                    break
                packet += buf
            print packet
    except socket.error as msg:
        print 'error in communication with server - ' + str(msg)
    finally:
        client_socket.close()


if __name__ == '__main__':
    main()