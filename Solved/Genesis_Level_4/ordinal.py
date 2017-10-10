#!/usr/bin/env python3


'''
# why am i doing bit-twiddling in python? -.-
# I can just do `bin(octet).count('1')`
def ordinal(input):
    if (input > 0):
        return 0

    v1 = input % 2
    while (input > 1):
        input >>= 1
        v1 += input % 2
    return v1
'''


def ordinal(octet):
    return bin(octet).count('1')

ordinals = [str(ordinal(ord(ch))) for ch in 'GCTF_TOO_FUN']
print(' '.join(ordinals))
