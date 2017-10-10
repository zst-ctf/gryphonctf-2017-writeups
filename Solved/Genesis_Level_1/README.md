# Genesis Level 1
Reverse - 20 points

## Challenge 
> In the beginning, there was nothing.

> nc rev.chal.gryphonctf.com 17234

> Creator - @LFlare

[genesis-redacted-9681a9ecd51523ccdd7b9c0b2dd17dba](genesis-redacted-9681a9ecd51523ccdd7b9c0b2dd17dba)

## Solution

Decompile using [Retargetable Decompiler](https://retdec.com/decompilation/).

	int32_t result = strcmp("7h15 15 4 h1dd3n 57r1n6", (char *)&str) == 0;

Our input is compared to `7h15 15 4 h1dd3n 57r1n6`. Enter it to get the flag

	$ nc rev.chal.gryphonctf.com 17234
	================================================================
	                            LEVEL 01                              
	================================================================
	Enter secret code: 7h15 15 4 h1dd3n 57r1n6
	GCTF{w3lc0m3_70_r3v3r53_3n61n33r1n6}

## Flag
`GCTF{w3lc0m3_70_r3v3r53_3n61n33r1n6}`