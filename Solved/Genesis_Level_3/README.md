# Genesis Level 3
Reverse - 70 points

***Continuation of [Genesis Level 2](../Genesis_Level_2)***

## Solution

First, let's look at `tumbalek()` which is used in `level_three()`
Here's a cleaned up version of the decompiled `tumbalek()`

    int32_t tumbalek(uint32_t a1) {
        uint32_t v1 = a1 / 16 % 16 | 16 * a1;
        uint32_t v2 = v1 / 4 & 51 | 4 * v1 & 204;
        return 0x1000000 * (v2 / 2 & 85 | 2 * v2 & 170) / 0x1000000;
    }

We can simplify it by changing all the numbers to hex, and bitshifts and removing useless calculations

    int32_t tumbalek(uint32_t a1) {
        uint32_t v1 = a1 >> 4 & 0x0F | a1 << 4;
        uint32_t v2 = (v1 & 0x33) >> 2 | (v1 & 0xCC) << 2;
        return (v2 & 0x55 >> 1 | v2 & 0xAA << 1);
    }

Now it is much more familiar. We can see it is just a algorithm to [reverse a 8-bit integer using bit-manipulation.](https://stackoverflow.com/a/2602885)

---
Next, look at the main function

    int32_t g1 = 0; // ebp

    // Address range: 0x804917a - 0x8049263
    int32_t level_three(void) {
        int32_t v1;
        g1 = &v1;
        int32_t v3;
        memcpy((char *)&v3, "N", 17);
        printf((char *)*(int32_t *)&g11);
        int32_t str;
        fgets((char *)&str, 32, g12);
        strcspn((char *)&str, "\n");
        int32_t v4 = 0; // bp-140
        int32_t v5 = 0; // 0x804920d
        // branch -> 0x80491fc
        while (true) {
            char v6 = *(char *)(v5 + (int32_t)&str); // 0x8049207
            int32_t v7 = *(int32_t *)(4 * v5 - 128 + g1); // 0x8049213
            if ((int32_t)v6 == tumbalek(v7)) {
                int32_t v8 = v4 + 1; // 0x8049231
                v4 = v8;
                if (v8 >= 17) {
                    break;
                }
                v5 = v8;
                continue;
            }
            
            return 0;
        }
        return 1;
    }


Simplifying it...

    int32_t g1 = 0; // ebp
    int32_t level_three(void) {
        int32_t v1;
        g1 = &v1;

        int32_t v3;
        memcpy((char *)&v3, "N", 17); // LINE 1

        print_level3_header();

        int32_t str;
        get_user_input_until_newline_and_store_in_str()

        int32_t v4 = 0;

        while (true) {
            char v6 = str[v5]; // *(char *)(v5 + (int32_t)&str);
            int32_t v7 = *(int32_t *)(4 * v4 - 128 + g1); // LINE 2
            if ((int32_t)v6 == tumbalek(v7)) {
                v4++;
                if (v4 >= 17) {
                    break;
                }
                continue;
            }
            
            return 0;
        }
        
        return 1;
    }

From LINE 1, 'N' is in the memory and looking at the disassembly, it is at address `0x8049aa0`

    0x804918e:   8d 45 80                           lea eax, dword [ ebp + 0xffffff80 ]
    0x8049191:   bb a0 9a 04 08                     mov ebx, 0x8049aa0
    0x8049196:   ba 11 00 00 00                     mov edx, 0x11

From LINE 2, we know that every 4 other bytes from memory are used for 17 iterations.
It is compared to the user input.

I opened the binary in Hopper Disassembler to see the chars byte by byte. This is the extracted portion from `level_three` to `level_four` address: [`extracted.txt`](extracted.txt)

Writing a python script to parse the bytes and apply `tumbalek()`, we get the payload:

    r3v3r53 3n61n33r5

Feed it to the server


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

## Flag
`GCTF{r3v3r51n6_b175_4r3_c00l}`
