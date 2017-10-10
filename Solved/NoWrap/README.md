# NoWrap
Crypto - 50 points

## Challenge 
> My white candy wrapper had this weird numbers encoded in it's molecular structure, I think it might contain the full recipe of the candy, can you help me get to the bottom of it?

> Creator - @LFlare

[flag-0fd9e17d87d7a4d42327c61c2295c2c4.txt](flag-0fd9e17d87d7a4d42327c61c2295c2c4.txt)

## Solution

We are given `n`, `e`, `c`.

Since `e` is very small, `n` is very large, and there's no padding as the name implies, [we can try to crack it](https://crypto.stackexchange.com/questions/6770/cracking-an-rsa-with-no-padding-and-very-small-e)

	If there is no padding, then you can try the following:
	...
	If e = 3 and m is short, then m^3 could be an integer which is smaller than n, in which case the modulo operation is a no-operation. In that case, you can just compute the cube root of the value you have (cube root for plain integers, not modular cube root).

Hence, get the cuberoot of `c` to get `m`

Now, `c` is too large for Python to handle, so we can use the `gmpy2` library to calculate it.

	$ python3 solve.py 
	Our secret flag has to be: GCTF{7h3_m355463_15_h1l4r10u5ly_5h0r7}

## Flag
`GCTF{7h3_m355463_15_h1l4r10u5ly_5h0r7}`