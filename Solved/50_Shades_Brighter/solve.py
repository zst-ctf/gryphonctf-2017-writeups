#!/usr/bin/env python3
from PIL import Image

im = Image.open('flag-55103fd3f7615102bef82539018477b2.png')
im = im.convert('RGB')

flag = ''
for x in range(im.size[0]):
    pixel = im.getpixel((x, 0))
    char_val = pixel[0] >> 1
    flag += chr(char_val)

print(flag)
