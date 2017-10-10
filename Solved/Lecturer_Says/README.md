# Lecturer Says
Programming - 20 points

## Challenge 
> Exams are coming soon! I haven't studied a thing! Luckily, the lecturers are giving out hints!

> nc prog.chal.gryphonctf.com 17451

> Creator - @Platy

## Solution

`nc` into the server

	Welcome to Lecturer Says!
	All you have to do is very simple.
	When the text is green, you say "Yes! I will study"
	If it's red, you say "No! I won't study"

Simple! Check for text color which is controlled by defined escape sequences.

	$ python3 solve.py 
	
	...

	Round: 500
	Lecturer Says: Study for Network Fundamentals!
	>
	GCTF{p4y_4773n710n_wh3n_l3c7ur3r_15_61v1n6_3x4m_h1n75}

## Flag
`GCTF{p4y_4773n710n_wh3n_l3c7ur3r_15_61v1n6_3x4m_h1n75}`