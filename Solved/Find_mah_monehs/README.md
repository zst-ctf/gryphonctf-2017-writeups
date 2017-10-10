# Find mah monehs
Programming - 120 points

## Challenge 
> NEEDZ HALPZ ME 2 FIND MAH MONEHS 2 BUY SUM GAMEZ. ME WANTS $100. CAN HALP PLZ? THX M8!

> Connect: `nc chal.gctf17.site 17454`

> Creator - @Platy

[monehs_ae642ad7e7fd608ac75da670090424fd.zip](monehs_ae642ad7e7fd608ac75da670090424fd.zip)

## Hint
PATH FINDIN ALGORITHM M8

## Solution
We are greeted with a maze to solve in the program.

	HALP ME EARN MONEY!

	RULEZ:
	U HAS 3 SECONDZ 2 FIND TEH PATH 2 TEH MONEY!
	DO DIS 100 TIEMS IN ROW AN U WIN!

	TEH @ IZ TEH STARTIN POINT
	TEH $ IZ TEH ENDIN POINT
	TEH +'S R TEH PATHS DAT U CAN TAEK
	TEH -'S R PATHS DAT U CANT TAEK

	2 SPECIFY UP U TYPE 'w'
	2 SPECIFY LEFT U TYPE 'a'
	2 SPECIFY DOWN U TYPE 's'
	2 SPECIFY RITE U TYPE 'd'

	For example:
	 -  -  -  -  -  -  -  -  -  - 
	 -  -  -  -  -  -  -  -  -  - 
	 $  +  -  -  -  -  -  -  -  - 
	 -  +  +  +  -  +  +  +  -  - 
	 -  +  +  -  +  +  +  +  -  - 
	 -  +  +  +  +  @  +  +  +  - 
	 +  +  +  +  +  +  +  -  -  - 
	 +  +  +  +  +  +  -  -  -  - 
	 +  +  -  -  +  -  -  -  -  - 
	 +  +  -  -  -  -  -  -  -  -

	TEH ANZWR WILL BE: aaaawwwa

	PRES ENTR 2 START!

Initially, I implemented a random algorithm which, although manages to solve the maze, after about round 40, the solution becomes thousands of characters long and the server can't handle the input.
> [random_algorithm.py](random_algorithm.py)

---

As the hint suggests, we need a path finding algorithm which will output a shorter path.
[A famous shortest path algorithm is the A-star algorithm](https://en.wikipedia.org/wiki/Maze_solving_algorithm#Shortest_path_algorithm).

I used [this library](https://github.com/brean/python-pathfinding) which implements the A-star algorithm.
> [a-star_algorithm.py](a-star_algorithm.py)
	
	$ git clone https://github.com/brean/python-pathfinding
	$ python3 a-star_algorithm.py

	...

	Received: U GOT $100
	HER IZ TEH FLAG!
	GCTF{1_w45_br0k3_bu7_n0_m0r3}

## Flag
`GCTF{1_w45_br0k3_bu7_n0_m0r3}`