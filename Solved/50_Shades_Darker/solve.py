#!/usr/bin/env python3
from PIL import Image

im = Image.open('flag-15c8d37a1d7799188d24039dd13b72a2.png')
im = im.convert('RGB')

flag = ''
for x in range(im.size[0]):
    pixel = im.getpixel((x, 0))

    pix_val = pixel[0] & 0xFF
    char_val = (pix_val << 1) & 0xFF | (pix_val >> 7)
    flag += chr(char_val)

print(flag)
