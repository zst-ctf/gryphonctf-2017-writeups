#!/usr/bin/env python3
from base64 import *

with open('flag.txt') as f:
    text = f.read().strip()

def bin2ascii(inputs):
    return ''.join(map(lambda x: chr(int(x, 2)),
                    split_every_n(inputs, 8)))

def split_every_n(line, n):
    return [line[i:i+n] for i in range(0, len(line), n)]

iters = 0
while 'GCTF{' not in str(text):
    iters += 1

    try:
        if (set(text[:10]) <= set('01')):
            print("base-2: Iteration", iters)
            text = bin2ascii(text)
        continue
    except e:
        print('no')
        raise e

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
    except e:
        raise e


print(text.decode())
