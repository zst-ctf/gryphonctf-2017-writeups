#!/usr/bin/env python3

import hashlib


def test_md5(ptext, hash):
    m = hashlib.md5()
    m.update(ptext.encode())
    hexdigest = m.hexdigest()
    print(hexdigest)
    print(hash)
    return hash == hexdigest
print(test_md5('goodpassword', 'a0d540a78cd61daa5fb872ac29272c00'))
print(test_md5('TOPSECRET', 'a038080bc8208c7f00837e8d2558df0f'))
