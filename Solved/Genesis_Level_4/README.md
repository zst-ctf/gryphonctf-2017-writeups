# Genesis Level 4
Reverse - 70 points

***Continuation of [Genesis Level 3](../Genesis_Level_3)***

> [UPDATE] 5/10/17 02:38PM - Updated distribs

[genesis-redacted-89d362910f1793b2d3ba15a411644c01](genesis-redacted-89d362910f1793b2d3ba15a411644c01)

## Solution

`level_four` relies on `ordinal()`. Let's look at what it is first.
This is simplified from the decompiled code.

    int32_t ordinal(int32_t input) {
        if (a1 > 0) {
            int32_t v1 = input % 2; // get the LSB
            while (input > 1) {
                input >>= 1; // bit-shifting version of `input /= 2`;
                v1 += input % 2; // get the LSB
            }
            return v1;
        }
        return 0;
    }

`ordinal()` basically counts the number of 1 bits in the binary form of the integer. eg. `ordinal(0b01011100) = 4`.

This can be done easily in Python using `bin(octet).count('1')`. Phew!

--- 

Next, the main code:

This is simplified a bit from Retargetable Decompiler.

    int32_t level_four(void) {
        int32_t v1;
        int32_t v2 = &v1; // 0x80492af_3
        int32_t str = 0x46544347; // bp-29
        int32_t v4; // eax
        int32_t v5; // bp+235


        if (ptrace(0) == -1) {
            puts("GDB IS NOT ALLOWED!");
            return 0
        }
        print_level4_header();

        int32_t v6;
        int32_t v7;
        int32_t v8;
        int32_t v9;
        int32_t v10;
        int32_t v11;
        int32_t v12;
        int32_t v13;
        int32_t v14;
        int32_t v15;
        int32_t v16;
        int32_t v17;
        scanf("%d %d %d %d %d %d %d %d %d %d %d %d", &v17, &v16, &v15, &v14, &v13, &v12, &v11, &v10, &v9, &v8, &v7, &v6);

        while (getchar() != 10); // wait for newline char

        if (strlen((char *)&str) != 0) {
            int32_t v18 = 0;
            // branch -> 0x804938d
            while (true) {
                char v19 = str[v18]
                *(int32_t *)(v2 - 16) = (int32_t)v19;
                *(int32_t *)(v2 - 20) = 0x80493a4;
                int32_t v20;
                int32_t v21 = ordinal(v20); // 0x804939f
                int32_t v22 = v18 + 1; // 0x80493bb
                if (v21 == *(int32_t *)(4 * v18 - 76 + g1)) {
                    // 0x80493bf
                    if (strlen((char *)&str) <= v22) {
                        // break -> 0x80493d7
                        break;
                    }
                    v18 = v22;
                    // continue -> 0x804938d
                    continue;
                }
                
                return 0;
            }
            
            return 1;
        }
        return 1;

    }

Basically, inside the `while(true)`, takes each octet offset from `0x46544347` (str) value and calculate the `ordinal()` and compares to our 12 input digits. 
There should be 3 DWORDs forming 12 bytes for our 12 inputted ordinal digits. But this decompiler doesn't show the values properly
    
    int32_t str = 0x46544347; // bp-29
    int32_t v4; // eax
    int32_t v5; // bp+235

We need to know what is v4 and v5, so let's use Hopper decompiler

    ; Variables:
    ;    var_C: -12
    ;    var_D: -13
    ;    var_11: -17
    ;    var_15: -21
    ;    var_19: -25
    ;    var_4C: -76
    ;    var_50: -80

    void level_four() {
        var_C = *0x14;
        eax = 0x0;
        var_19 = 0x46544347;
        var_15 = 0x4f4f545f;
        var_11 = 0x4e55465f;
        var_D = 0x0;
        esp = (esp - 0x10) + 0x10;
        ...
    }

Now we have the values. Let's reverse as it is little endian.

    $ python
    
    >>> from pwn import *
    >>> p32(0x46544347) + p32(0x4f4f545f) + p32(0x4e55465f)
    'GCTF_TOO_FUN'

Thanks for the reassurance! 
Now get the ordinal of each char and submit those numbers!

    $ python3 ordinal.py 
    4 3 3 3 6 3 5 5 6 3 4 4

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
    ================================================================
                                LEVEL 03                              
    ================================================================
    Enter secret code: r3v3r53 3n61n33r5
    GCTF{r3v3r51n6_b175_4r3_c00l}
    ================================================================
                                LEVEL 04                              
    ================================================================
    Enter secret code: 4 3 3 3 6 3 5 5 6 3 4 4
    GCTF{b17_7w1ddl1n6_f1x3d_f0r_r34lz_n0w}

## Flag
`GCTF{b17_7w1ddl1n6_f1x3d_f0r_r34lz_n0w}`

---

## Unintended solution

Somehow due to a bug, the original binary's Level 4 flag was given together with level 3. It was fixed later on in the updated distribs

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
    ================================================================
                                LEVEL 03                              
    ================================================================
    Enter secret code: r3v3r53 3n61n33r5
    GCTF{r3v3r51n6_b175_4r3_c00l}
    GDB IS NOT ALLOWED!
    GCTF{b17_c0un71n6_w17h_b17_7w1ddl1n6}
    ================================================================
                                LEVEL 05                              
    ================================================================
    Enter secret code:


Looking at the decompiled code, seems like the server was set up wrongly and detected as having GDB, hence it immediately returns 1 and shows the flag.

    int32_t level_four(void) {
        // Omitted //
        if (ptrace(0) == -1) {
            puts("GDB IS NOT ALLOWED!");
        } else {
            // Level 4 challenge code is here //
        }
        return 1;
    }
