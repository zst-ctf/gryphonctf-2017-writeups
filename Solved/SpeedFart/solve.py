#!/usr/bin/env python3

import brainfuck
import socket
import re

s = socket.socket()
s.connect(('prog.chal.gryphonctf.com', 17455))

while True:
    data = s.recv(40960).decode().strip()
    if not data:
        continue

    print("Received:", data)
    if 'Are you ready? [y/n]' in data:
        s.send(b'y\n')

    if 'FIGHT!' in data:
        while 'What value is in the ' not in data:
            data += s.recv(4096).decode().strip()

        segments = data.split("+-+-+-+-+-+-+-+-+-+-")
        code = ''.join(segments[1].splitlines())
        print('>> Code:', code)

        registers = brainfuck.evaluate(code)
        print('>> Register:', registers)

        match = re.search(r'What value is in the (\d+).. register',
                          segments[2].strip())
        numb = int(match.group(1))

        result = registers[numb - 1]
        print('>> Result:', result)

        s.send(str(result).encode() + b'\n')

    if 'GCTF' in data:
        quit()
