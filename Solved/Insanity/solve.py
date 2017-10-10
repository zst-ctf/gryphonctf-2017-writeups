#!/usr/bin/env python3
from base64 import *

with open('fe3c84aa840d950f7f3d006ebc4db48f.txt') as f:
    text = f.read().strip()

iters = 0
while 'GCTF{' not in str(text):
    iters += 1
    try:
        text = b16decode(text)
        print("base-16: Iteration", iters)
        continue
    except:
        pass

    try:
        text = b32decode(text)
        print("base-32: Iteration", iters)
        continue
    except:
        pass

    try:
        text = b64decode(text)
        print("base-64: Iteration", iters)
        continue
    except:
        pass

print(text.decode())
