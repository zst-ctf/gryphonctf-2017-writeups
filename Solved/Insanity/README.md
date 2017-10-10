# Insanity
Are you ready? - 0 points

## Challenge 
> My bassist wrote this down on a piece of paper before he died of lack of Vitamin B, I'm going insane trying to figure out what he meant, can you help me?
> 
> Creator @LFlare

[fe3c84aa840d950f7f3d006ebc4db48f.txt](fe3c84aa840d950f7f3d006ebc4db48f.txt)

## Solution

The file has a base-32 encoded string. Upon decoding it, it gives us a base-64 string.

This is similar to [CrossCTF 2017 Go Deep](https://github.com/zst123/crossctf_quals-2017-writeups/tree/master/Go_Deep), except base-16, base-32 and base-64 is needed together.

Run [solve.py](./solve.py)

	$ python3 solve.py 
	base-32: Iteration 1
	base-64: Iteration 2
	base-32: Iteration 3
	base-16: Iteration 4
	base-64: Iteration 5
	GCTF{b4535_4r3_c0nfu51n6_m4n}

## Flag
`GCTF{b4535_4r3_c0nfu51n6_m4n}`