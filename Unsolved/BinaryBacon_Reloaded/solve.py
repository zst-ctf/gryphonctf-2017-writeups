#!/usr/bin/env python3

import re

def bin2ascii(inputs):
    return ''.join(map(lambda x: chr(int(x, 2)),
                    split_every_n(inputs, 8)))


def split_every_n(line, n):
    return [line[i:i+n] for i in range(0, len(line), n)]

with open('BACON_feb70db7988779276c71f6afa705e217') as f:
    bacon = f.read()
bacon = '''
HEllO P Eople I aM HeRE TO telL yOu SOM EThiNg i aM LEA RninG T o COmMU NicaTe WITH bl inD PEO Ple!! whA T dO yOU thINK A Bout th at? ISNT That A g oOD tHI NG? i cAn taLK TO More pe opLE AB Out mY l ove for bacon now!!!
'''

# remove all non-alphabetical characters
bacon = re.sub(r'([^A-Za-z ])', '', bacon)

# change uppercase to A
bacon = re.sub(r'([A-Z])', '1', bacon)

# change lowercase to B
bacon = re.sub(r'([a-z])', '0', bacon)

braille = split_every_n(bacon.replace(' ', ''), 6)
#braille = list(map(lambda x: '{:06b}'.format(int(x, 2)), bacon.split(' ')))
print(' '.join(braille))

quit()
print(bacon)
print(len(bacon))


print(bin2ascii(bacon + "000000000000"))



