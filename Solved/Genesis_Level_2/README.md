# Genesis Level 2
Reverse - 50 points

***Continuation of [Genesis Level 1](../Genesis_Level_1)***

## Solution

Looking at decompiled code

    int32_t str2 = 0x6e316837; // bp-73
    printf((char *)*(int32_t *)&g11);
    int32_t str;
    fgets((char *)&str, 32, g12);
    strcspn((char *)&str, "\n");
    int32_t strcmp_rc = strcmp((char *)&str2, (char *)&str); // 0x80490cf

Our input is compared to the string at address `0x6e316837`

Looking at the disassembly

	; function: level_two

	mov dword [ ebp + 0xffffffbb ], 0x6e316837
	mov dword [ ebp + 0xffffffbf ], 0x366e316b
	mov dword [ ebp + 0xffffffc3 ], 0x37317720
	mov dword [ ebp + 0xffffffc7 ], 0x6e312068
	mov dword [ ebp + 0xffffffcb ], 0x33363337
	mov dword [ ebp + 0xffffffcf ], 0x31213572
	mov byte [ ebp + 0xffffffd3 ], 0x0
	mov eax, dword [ 0x804b07c ]

We see 6 `dwords` and 1 null `byte`. Put all these hex together and decode it to ASCII.
Little endian, so reverse it. I used `p32` from `pwntools` to reverse it for me

	from pwn import *

	p32(0x6e316837) + \
	p32(0x366e316b) + \
	p32(0x37317720) + \
	p32(0x6e312068) + \
	p32(0x33363337) + \
	p32(0x31213572)

	'7h1nk1n6 w17h 1n7363r5!1'

Enter to get the flag!

	$ nc rev.chal.gryphonctf.com 17234
	================================================================
	                            LEVEL 01                              
	================================================================
	Enter secret code: 7h15 15 4 h1dd3n 57r1n6
	GCTF{w3lc0m3_70_r3v3r53_3n61n33r1n6}
	================================================================
	                            LEVEL 02                              
	================================================================
	Enter secret code: 7h1nk1n6 w17h 1n7363r5!1
	GCTF{ch4r_p01n73r5_!=_ch4r_4rr4y}

## Flag
`GCTF{ch4r_p01n73r5_!=_ch4r_4rr4y}`
