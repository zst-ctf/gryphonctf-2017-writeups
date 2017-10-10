# Genesis Level 6
Reverse - 250 points

***Continuation of [Genesis Level 5](../Genesis_Level_5)***

## Solution

Looking at the `bonus()` method first.

	// Hopper Decompiler
	int bonus() {

	    printf(*banner, 0x63);

	    fgets(&var_4E, 0x20, *__TMC_END__);
	    *(int8_t *)(ebp + strcspn(&var_4E, 0x8049a27) + 0xffffffb2) = 0x0;
	    if (strcmp(&0x20643164, &var_4E) == 0x0) {
	            eax = 0x1;
	    } else {
	            eax = 0x0;
	    }
	    return eax;
	}

Using this, I can simplify the code, to just a comparison of 2 strings.

	int bonus() {
		print_level6_header();

		char string1[32];
		fgets(&string1, 32, stdin); // fgets excluding newline

		char str2 = 0x20643164; // string at address of 0x20643164
		char * string2 = &str2; // string at address of 0x20643164
    	return (string1 == string2);
	}


Like in [Level 2](../Genesis_Level_2), I extracted the string.
	
    ; Variables:
    ;    var_C: -12
    ;    var_E: -14
    ;    var_12: -18
    ;    var_16: -22
    ;    var_1A: -26
    ;    var_1E: -30
    ;    var_22: -34
    ;    var_26: -38
    ;    var_2A: -42
    ;    var_2E: -46
    ;    var_4E: -78

	080495f4         movl       $0x20643164, var_2E(%ebp)
	080495fb         movl       $0x20753079, var_2A(%ebp)
	08049602         movl       $0x6e316837, var_26(%ebp)
	08049609         movl       $0x6837206b, var_22(%ebp)
	08049610         movl       $0x77203531, var_1E(%ebp)
	08049617         movl       $0x646c7530, var_1A(%ebp)
	0804961e         movl       $0x20336220, var_16(%ebp)
	08049625         movl       $0x79353433, var_12(%ebp)
	0804962c         movw       $0x3f, var_E(%ebp)

	from pwn import *
	val = [0x20643164, 0x20753079, 0x6e316837, 0x6837206b, 0x77203531, 0x646c7530, 0x20336220, 0x79353433, 0x3f]
	val = list(map(lambda x: p32(x), val))
	print(''.join(val))
	d1d y0u 7h1nk 7h15 w0uld b3 345y?

If you key it in, it fails. This is because `d1d y0u 7h1nk 7h15 w0uld b3 345y?` is 33 bytes long, but our input buffer is only 31 bytes (excluding null byte). Hence, it will never succeed. I confirmed this by bruteforcing the input until I got `d1d y0u 7h1nk 7h15 w0uld b3 345` and then it stopped.

---

After asking for a hint from the challenge creators, he said that "something else" is in the program outside.
I decided to [decompile again using Retargetable, but changing the decompiler optimisations to low](decompile_low-optimisation.c).

Now we can see some weird functions.
Looks like there is a socket connection to a server.

	int32_t _sys_construct(void);
	int32_t _sys_hash(int32_t a1, char * a2);
	int32_t _sys_send(char * a1, char * a2);
	
	// --------------- Dynamically Linked Functions ---------------
	// struct hostent * gethostbyname(const char * name);
	// int socket(int domain, int type, int protocol);


Simplifying `_sys_hash()`, it is a simple single-key XOR function.

	int _sys_hash(int key, char * str) {
		if (strlen(str) == 0) {
			return 0;
		}
		for (int i = 0; i < strlen(str); i++) {
			a2[i] ^= key;
	    }
	}	

It is used in `_sys_construct()` on 6 strings.

    _sys_hash(63, (char *)&v_4370);
    _sys_hash(123, (char *)&v_4376);
    _sys_hash(42, (char *)&v_4361);
    _sys_hash(2, (char *)&v_4323);
    _sys_hash(127, (char *)&v_4241);
    _sys_hash(24, (char *)&v_4343);

We can take a look at the disassembly from line `08048ce3` to line `08048d50` which we can see the location of each string.


	// ssize_t send(int sockfd, const void *buf, size_t len, int flags);
	// send a message on a socket
	// The argument sockfd is the file descriptor of the sending socket.
	int32_t _sys_send(char * sockfd, char * buffer) {
	    send((int32_t) sockfd, buffer, strlen(buffer), 0);
	    return v_8048adb2;
	}

I created a script to parse the strings from the extracted disassembly. Each of the 6 strings have different XOR keys.
	
	$ python3 extract_xor.py 
	Couldn't
	Found
	chat.freenode.com
	USER GCTF_ID10T_%s GCTF_ID10T_%s GCTF_ID10T_%s :GCTF_ID10T_%s
	NICK GCTF_ID10T_%s

	JOIN #gryphonctf
	PRIVMSG #gryphonctf :I AM AN ID10T WHO RUNS BINARIES GIVEN TO ME INDISCRIMINATELY! MOCK MEEE!!!

	End of /NAMES list.

From this, we can see it is connecting to [Freenode channel](chat.freenode.com) `#gryphonctf`.
Now at the chat header we can see this! We see the input string at the end!

	#gryphonctf: GryphonCTF - 4 October 2017 - Stay tuned! - 1n73rn37 r34lly ch4rm5


For the rest of `_sys_construct()`, understanding it is not really needed. Here's what it does:

- connect chat.freenode.com
- JOIN #gryphonctf channel
- Check if "Couldn't" is in the response (Checking for "Couldn't" connect)
- If connected successful, then next generate 5 random chars appended to `GCTF_ID10T_` as the username
- send `I AM AN ID10T WHO RUNS BINARIES GIVEN TO ME INDISCRIMINATELY! MOCK MEEE!!!`

For the last time, send the payload

	$ cat final_payload | nc rev.chal.gryphonctf.com 17234
	...

	================================================================
	                            LEVEL 99                              
	================================================================
	Enter secret code: GCTF{1rc_15_p0pul4r_4m0n6_c7f_pl4y3r5_700}

## Flag
`GCTF{1rc_15_p0pul4r_4m0n6_c7f_pl4y3r5_700}`
