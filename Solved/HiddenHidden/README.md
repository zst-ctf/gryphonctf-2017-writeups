# HiddenHidden
Crypto - 20 points

## Challenge 
> I accidentally left my simple encryption on loop and it spit this file out... Help me decode this please! Thank you!

> Creator - @paux

> [hiddenflag_6d94c51b0be2bd4a35daf690850df2c0.zip](hiddenflag_6d94c51b0be2bd4a35daf690850df2c0.zip)

## Solution
This was similar to the [practice question, Insanity](../Insanity) except including binary decode.

However, when I tried using my Python script, it was too slow. The string is too big for Python to handle.

I decided to manually create a bash script to decode it using [`perl` codes for the binary portion](https://unix.stackexchange.com/a/98949) and `base64 --decode`. This was much faster indeed.

	$ bash decode.sh 
	Archive:  hiddenflag_6d94c51b0be2bd4a35daf690850df2c0.zip
	  inflating: hiddenflag              
	GCTF{100p1n65_5_4ev44a44rz}

## Flag
`GCTF{100p1n65_5_4ev44a44rz}`


