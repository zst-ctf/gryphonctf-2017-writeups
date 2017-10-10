# SpeedFart
Programming - 100 points

## Challenge 
> This was originally written on a stone slab somewhere in a forest. I took it, tweaked it and served it.

> nc prog.chal.gryphonctf.com 17455

> Creator - @LFlare

## Solution

	
This challenge presents you with Brainfuck code and asks you to reply with the value in the register.

	Hello there! I am the new automated testing machine!
	Unfortunately, I am also slightly stupid.

	I will ask you a series of questions.
	All you have to do, is send me your replies.
	The catch? You have to do it within 10 seconds.

	This may or may not help you:
	- 16 8-bit registers
	- 50.0 rounds

	Are you ready? [y/n]
	ROUND 1, FIGHT!
	+-+-+-+-+-+-+-+-+-+-

	><>++-<>>>><<->>>[>+>+>+>>>+>>>+++-<>][--<-+[<<+>+->+>[-+><>-<+-
	]]]

	+-+-+-+-+-+-+-+-+-+-
	What value is in the 2nd register?

Thankfully, a [there is a Python 2 library (Brainfuck interpreter)](https://github.com/pocmo/Python-Brainfuck).

I modified `evaluate()` by adding a `return cells` so I can access the registers.
I also made it work with Python3.

	$ python3 solve.py 
	...
	Received: Correct!
	Flag is: GCTF{1_h0p3_y0u_d1d_n07_7ry_7h15_m4nu4lly}

## Flag
`GCTF{1_h0p3_y0u_d1d_n07_7ry_7h15_m4nu4lly}`