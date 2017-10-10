#!/usr/bin/env python3
import socket

RED = '\033[91m'
GREEN = '\033[92m'

s = socket.socket()
s.connect(('prog.chal.gryphonctf.com', 17451))

while True:
    data = s.recv(4096).decode().strip()
    print(data)

    if RED in data:
        s.send(b"No! I won't study\n")

    elif GREEN in data:
        s.send(b"Yes! I will study\n")

    if "GCTF{" in data:
        quit()