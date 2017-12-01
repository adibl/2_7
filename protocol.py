# -*- coding: utf-8 -*-
"""
author - adi bleyer
date   - 29/11/17
handling the protocol pack and unpack.
valid checks for arguments.
"""
import struct
import socket

LEN_SIGN_BIG = 'L' # 4 bytes, number between 0 to 4Mkb
LEN_SIGN_SMALL = 'H' # 2 bytes, number between 0 to 64kb
HEADER_LEN_SMALL = 2
HEADER_LEN_BIG = 4



def send(my_socket, massage):
    """
    send massage
    :param:my_socket: the communication socket.
    :param:massage: the massage that hte program send.
    :return: return None if the action seceded.
    if not return the error string.
    """
    packet_len = socket.htons(len(massage[0]))
    err = my_socket.sendall(struct.pack(LEN_SIGN_SMALL, packet_len))
    if not err is None:
        print err
        return False
    err = my_socket.sendall(massage[0])
    if not err is None:
        print err
        return False

    packet_len = socket.htons(len(massage[1]))
    err = my_socket.sendall(struct.pack(LEN_SIGN_BIG, packet_len))
    if not err is None:
        print err
        return False
    err = my_socket.sendall(massage[1])
    if not err is None:
        print err
        return False
    return True




def recv(my_socket):
    var =[]
    net_len = ''
    while len(net_len) < HEADER_LEN_SMALL:
        net_packet = my_socket.recv(HEADER_LEN_SMALL - len(net_len))
        if net_packet == '':
            net_len = ''
            break
        net_len += net_packet
    if net_len != '':
        packet_len = socket.ntohs(struct.unpack(LEN_SIGN_SMALL, net_len)[0])

        packet = ''
        while len(packet) < packet_len:
            buf = my_socket.recv(packet_len - len(packet))
            if buf == '':
                break
            packet += buf
        var.append(packet)

    net_len = ''
    while len(net_len) < HEADER_LEN_BIG:
        net_packet = my_socket.recv(HEADER_LEN_BIG - len(net_len))
        if net_packet == '':
            net_len = ''
            break
        net_len += net_packet
    if net_len != '':
        packet_len = socket.ntohs(struct.unpack(LEN_SIGN_BIG, net_len)[0])

        packet = ''
        while len(packet) < packet_len:
            buf = my_socket.recv(packet_len - len(packet))
            if buf == '':
                break
            packet += buf
        var.append(packet)
        return var


if __name__ == '__main__':
    pass