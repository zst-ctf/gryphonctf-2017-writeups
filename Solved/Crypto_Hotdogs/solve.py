#!/usr/bin/env python3

###############################################################
# Read in public key
###############################################################
from Crypto.PublicKey import RSA
from Crypto.Util import asn1
from base64 import b64decode

with open("distrib/flag.bin", 'rb') as f1:
    flag_enc = f1.read()

with open("distrib/public.pem", "r") as f:
    b64_key = f.read()
    b64_key = b64_key.splitlines()[1:-1]
    b64_key = ''.join(b64_key)

pub_key = RSA.importKey(b64decode(b64_key))

n = pub_key.n
e = pub_key.e
c = int.from_bytes(flag_enc, byteorder='big')

# print(pub_key.keydata)
print('n =', n)
print('e =', e)
print('c =', c)

###############################################################
# Do RSA Wiener Attack
###############################################################

'''
References:
    https://crypto.stackexchange.com/questions/777/in-rsa-do-i-calculate-d-from-e-or-e-from-d
    https://github.com/pablocelayes/rsa-wiener-attack

Formula:
    m = c^d % n
'''
import binascii

# Add git directory to path, so we can import easily
import sys
sys.path.insert(0, './rsa-wiener-attack')

# import the hack!
from RSAwienerHacker import hack_RSA
d = hack_RSA(e, n)

# decrypt
priv_key = RSA.construct((n, e, d))
m = priv_key.decrypt(c)
# pow(c, d) % n
# m = pow(c, d, n)

# https://stackoverflow.com/questions/4368676/is-there-a-way-to-pad-to-an-even-number-of-digits
def hex_pair(x):
    return ('0' * (len(x) % 2)) + x

m_hex = '{:x}'.format(m)
m_hex = hex_pair(m_hex)
msg = binascii.unhexlify(m_hex)
print(msg)

