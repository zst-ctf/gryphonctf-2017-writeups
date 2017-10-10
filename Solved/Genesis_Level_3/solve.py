#!/usr/bin/env python3

import re
with open('extracted.txt', 'r') as f:
    hopper = f.read().splitlines()


def tumbalek(octet):
    number = int(octet, 16)
    number = (number & 0x0F) << 4 | (number & 0xF0) >> 4
    number = (number & 0x33) << 2 | (number & 0xCC) >> 2
    number = (number & 0x55) << 1 | (number & 0xAA) >> 1
    return '{:02x}'.format(number & 0xFF)


def get_hex(offset):
    line = hopper[offset]
    print(line)
    return re.match(r'.+0x(..)', line).group(1)


payload = ''
for i in range(17):
    octet = get_hex(i * 4)
    octet = tumbalek(octet)
    payload += octet

print(bytes.fromhex(payload).decode())
