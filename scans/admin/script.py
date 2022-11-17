#!/usr/bin/env python3

import socket
from contextlib import closing

def check_socket(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f'{host} is open at {port}')
        return
    except Exception as e:
        print(f"{host} {e}")


with open("amass.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        l = line.strip()
        check_socket(l, 80)
        check_socket(l, 443)