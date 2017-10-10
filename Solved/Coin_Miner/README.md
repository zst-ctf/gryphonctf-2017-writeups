# Coin Miner
Programming - 30 points

## Challenge 
> I'm running low on cash right now. Luckily, I found this virtual currency that uses inputs that when hashed, produces a hexdigest in which the first 2 characters are '00'. I just need 20 of them. Thanks!

> `nc prog.chal.gryphonctf.com 17452`

> Creator - @Platy

## Hint
> You can use random character generator

## Solution

I created a script to randomly generate UUIDs and store those whose hexdigest starts with `00`. After collecting 20 strings, feed it into the server.

Run the script and we get the flag

	$ python3 solve.py

	...

	Received: Good job!
	Here is the flag: GCTF{70d4y_c01n_m1n3r_70m0rr0w_b17c01n}

## Flag
`GCTF{70d4y_c01n_m1n3r_70m0rr0w_b17c01n}`