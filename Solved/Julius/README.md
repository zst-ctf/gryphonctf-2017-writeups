# Julius
Sanity - 5 points

## Challenge 
> 13 rotations

> Creator - @exetr

> [93fd2e47a6cbe711c5bc730c96075f3d.txt](93fd2e47a6cbe711c5bc730c96075f3d.txt)

## Solution
13 rotations = ROT13 (aka. Ceaser cipher)

	$ cat 93fd2e47a6cbe711c5bc730c96075f3d.txt | python -c 'import sys; print sys.stdin.read().encode("rot13")'
	GCTF{caesar_s414d_iz_me_f4v0ur17e}

## Flag
`GCTF{caesar_s414d_iz_me_f4v0ur17e}`