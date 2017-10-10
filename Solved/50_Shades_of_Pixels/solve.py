#!/usr/bin/env python3
from PIL import Image

im = Image.open('flag-e89619f149a311e9e60b7107317217b7.png')
im = im.convert('RGB')

flag = ''
for x in range(im.size[0]):
	pixel = im.getpixel((x, 0))
	flag += chr(pixel[0])

print(flag)