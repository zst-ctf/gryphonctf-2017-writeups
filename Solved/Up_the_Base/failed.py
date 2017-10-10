#!/usr/bin/env python3

'''
def bin2ascii(i):
    pad = '0' * (8 - (len(i) - (len(i) // 8 * 8)))
    i += pad
    n = int(i, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
'''


def bin2ascii(inputs):
    return ''.join(map(lambda x: chr(int(x, 2)),
                    split_every_n(inputs, 8)))


def split_every_n(line, n):
    return [line[i:i+n] for i in range(0, len(line), n)]


def solve(base_len=18):
    final_binary = ''
    for ch in text:
        unicode_point = ord(ch) & ((1 << base_len) - 1)
        binary = ('{:0'+str(base_len)+'b}').format(unicode_point)#[-base_len:]
        #print(binary, hex(unicode_point), )
        final_binary += binary

    #print(final_binary)
    ascii = bin2ascii(final_binary + '0' * 8)
    print(ascii)


with open('output_128d62817031d5fe21821f918fb08fed.bin', 'rb') as f:
    text = f.read().decode('utf-8')


solve()
quit()
for base_len in range(10, 50):
    solve(base_len)
    

#ascii = 
#print(ascii)

'''
print(final_binary)
print(bin2ascii(final_binary))
print('Success')
quit()
'''
