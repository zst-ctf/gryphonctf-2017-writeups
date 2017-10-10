# 50 Shades Darker
Forensics - 120 points

## Challenge 
> Alice - "Wow, I know I said it was too dark earlier but this is way too bright!"
Bob - "Are you serious!? Fine! Whatever suits you!"
Alice - "..."
Bob - "..."
Alice - "This seems weird."

>Creator - @LFlare

[flag-15c8d37a1d7799188d24039dd13b72a2.png](flag-15c8d37a1d7799188d24039dd13b72a2.png)

## Solution

***Continuation of [50 Shades Brighter](./50_Shades_Brighter)***

Now that we know brighter means shifted up, darker should mean shifted down

Change it to `char_val = (pix_val << 1)`
	
	$ python3 solve.py 
	ņłTFźĶhİĴŞd4rŪnĲĴĴŞİĴŞn0ĶŞ4ĴŞĲxpĲŢĶĲdŞĲhżņłTFźĶhİĴŞd4rŪnĲĴĴŞİĴŞn0ĶŞ4ĴŞĲxpĲŢĶĲdŞĲhżņłTFźĶhİĴŞd4rŪnĲĴĴŞİĴŞn0ĶŞ4ĴŞĲxpĲŢĶĲdŞĲhżņ

Hmm, that's weird. It is displaying Unicode text? Now after shifting up, we end up with 9-bits. We need to mask `char_val` to make sure it is within 8 bits 

Change it to `char_val = (pix_val << 1) & 0xFF`

	$ python3 solve.py 
	FBTFz6h04^d4rjn244^04^n06^44^2xp2b62d^2h|FBTFz6h04^d4rjn244^04^n06^44^2xp2b62d^2h|FBTFz6h04^d4rjn244^04^n06^44^2xp2b62d^2h|F

Not quite there yet. After examining closely, some of the top-most bits are not always zero. Perhaps it is necessary information.
Change it to a 8-bit rotation instead: `char_val = (pix_val << 1) & 0xFF | (pix_val >> 7)`
	
	$ python3 solve.py 
	GCTF{7h15_d4rkn355_15_n07_45_3xp3c73d_3h}GCTF{7h15_d4rkn355_15_n07_45_3xp3c73d_3h}GCTF{7h15_d4rkn355_15_n07_45_3xp3c73d_3h}G

## Flag
`GCTF{7h15_d4rkn355_15_n07_45_3xp3c73d_3h}`