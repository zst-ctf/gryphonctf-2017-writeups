#!/usr/bin/env python3

from hashlib import sha512
from uuid import uuid4
import socket

payloads = []
while len(payloads) < 20:
    string = str(uuid4()).encode()
    hash_object = sha512(string)
    hex_dig = hash_object.hexdigest()
    if hex_dig.startswith('00'):
        payloads.append(string)


s = socket.socket()
s.connect(('prog.chal.gryphonctf.com', 17452))

while True:
    data = s.recv(4096).decode().strip()
    if not data:
        continue

    print("Received:", data)

    if 'Press enter to start!' in data:
        s.send(b'\n')

    if '>' in data:
        payload = payloads.pop(0)
        print('Sending:', payload)
        s.send(payload)

    if 'flag' in data:
        quit()
