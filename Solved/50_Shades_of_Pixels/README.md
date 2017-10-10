# 50 Shades of Pixels
Forensics - 40 points

## Challenge 
> Bob - "I don't do plaintext."

> Bob - "My methods of communication are unconventional."

>Alice - "So show me?"

>Bob - "Okay!"

> Creator - @LFlare

[flag-e89619f149a311e9e60b7107317217b7.png](flag-e89619f149a311e9e60b7107317217b7.png)

## Solution
Since the pixels are different shades of grey, it seems the pixel color is based on the ASCII value. Read in the RGB value as an ASCII char.

	$ python3 solve.py
	GCTF{p1x3l1z3d_53cr375_4r3_h4w7}GCTF{p1x3l1z3d_53cr375_4r3_h4w7}GCTF{p1x3l1z3d_53cr375_4r3_h4w7}GCTF{p1x3l1z3d_53cr375_4r3_h4w7}

## Flag
`GCTF{p1x3l1z3d_53cr375_4r3_h4w7}`
