# Comments Down Below
Sanity - 5 points

## Challenge 
> Find the flag! It is somewhere here: http://san.chal.gryphonctf.com:17121
> 
> Creator - @exetr

## Solution

Flag is in the commented HTML code

	$ curl -s http://san.chal.gryphonctf.com:17121/ | grep "GCTF"
	<!-- GCTF{c0mm3nt_-_c0mm3nt4ry_4_dayz} -->

## Flag
`GCTF{c0mm3nt_-_c0mm3nt4ry_4_dayz}`