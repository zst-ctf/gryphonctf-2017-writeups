#!/usr/bin/env python3

import re

with open("flag_847cd8dd2bfb19a55a443d50450fb075.txt") as f:
    dirty = f.read()

# match non-hex characters
regex = re.compile(r'[^0-9a-f]')
clean = regex.sub('', dirty)

flag = bytes.fromhex(clean).decode()
print(flag)
