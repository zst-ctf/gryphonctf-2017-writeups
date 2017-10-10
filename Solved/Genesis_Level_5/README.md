# Genesis Level 5
Reverse - 150 points

***Continuation of [Genesis Level 4](../Genesis_Level_4)***

## Solution

`fov()` is used in level 5. Let's analyse it first!

    int32_t fov(float32_t a1) {
        
        // lots of stuff i don't understand here

        return 0x5f3759df - (int32_t)a1 / 2;
    }

Immediately I see [`0x5f3759df`](https://en.wikipedia.org/wiki/Fast_inverse_square_root) which is famous for the [fast inverse square root algorithm](https://github.com/itchyny/fastinvsqrt#why-did-i-choose-this-algorithm).

Next, looking at the main function, it is pretty long and daunting (slightly shortened from decompiled version).

    int32_t g1 = 0; // ebp
    bool g2 = false; // fpu_ctrl_DM
    bool g3 = false; // fpu_ctrl_IM
    bool g4 = false; // fpu_ctrl_OM
    int2_t g5 = 0; // fpu_ctrl_PC
    bool g6 = false; // fpu_ctrl_PM
    int2_t g7 = 0; // fpu_ctrl_RC
    bool g8 = false; // fpu_ctrl_UM
    bool g9 = false; // fpu_ctrl_X
    bool g10 = false; // fpu_ctrl_ZM

    // Address range: 0x80494e0 - 0x804964a
    int32_t level_five(void) {
        int32_t v1 = *(int32_t *)20; // 0x80494e8
        
        print_level5_header();

        int32_t v2;
        int32_t v3;
        int32_t v4;
        int32_t v5;
        int32_t v6;
        scanf("%f %f %f %f %f", &v6, &v5, &v4, &v3, &v2);

        while (getchar() != 10); // WAIT FOR NEWLINE CHAR

        int32_t v7;
        int32_t v8 = &v7; // 0x8049579
        int32_t v9 = 0;
        // branch -> 0x804956f
        while (true) {
            int32_t v10 = 4 * v9; // 0x8049572
            int32_t v11 = v10 - 52; // 0x8049572
            int32_t v13 = v10 - 32; // 0x8049579
            fov(*(float32_t *)(v13 + v8));


            int16_t v14 = g2 ? 2 : 0; // 0x80495a1
            int16_t v15 = g10 ? 4 : 0; // 0x80495a1
            int16_t v16 = g4 ? 8 : 0; // 0x80495a1
            int16_t v17 = g8 ? 16 : 0; // 0x80495a1
            int16_t v18 = g6 ? 32 : 0; // 0x80495a1
            int16_t v19 = g9 ? 0x1000 : 0; // 0x80495a1
            int16_t v20;
            int16_t v21;
            uint32_t v22 = (int32_t)
                (v20 << 10 | v21 << 8 | g3 & 0xFFFF | v14 | v15 | v16 | v17 | v18 | v19 | 1<<6); // 0x80495a1_0
            
            g3 = v2 & 0x01; //v22 % 2 != 0; // check if bit 0 set
            g2 = !!(v22 & 0b10); // (v22 & 2) != 0; // check bit 1 set
            g10 = !!(v22 & 0b100); // (v22 & 4) != 0; // check if bit 2 set
            g4 = !!(v22 & 0b1000); // (v22 & 8) != 0; // check if bit 3 set
            g8 = !!(v22 & 0b10000); // (v22 & 16) != 0; // check if bit 4 set
            g6 = !!(v22 & 0b100000); // (v22 & 32) != 0; // check if bit 5 set

            //int2_t v23 = (int2_t)(v22 / 256) & -2; // 0x80495b4
            int2_t v23 = (v22 >> 8) & 0b10; // 0x80495b4
            g5 = v23;
            //int2_t v24 = (int2_t)(v22 / 1024) & -2; // 0x80495b4
            int2_t v24 = (v22 >> 10) & 0b10; // 0x80495b4
            g7 = v24;
            g9 = (v22 & 0x1000) != 0; // check 12th bit



            int32_t v12 = *(int32_t *)(v11 + v8); // 0x8049572
            printf("%d %d\n", (int32_t)round(0.0), v12);
            fov(*(float32_t *)(g1 + v13));
            round(0.0);


            int16_t v25 = g2 ? 2 : 0; // 0x80495f7
            int16_t v26 = g10 ? 4 : 0; // 0x80495f7
            int16_t v27 = g4 ? 8 : 0; // 0x80495f7
            int16_t v28 = g8 ? 16 : 0; // 0x80495f7
            int16_t v29 = g6 ? 32 : 0; // 0x80495f7
            int16_t v30 = g9 ? 0x1000 : 0; // 0x80495f7

            uint32_t v31 = (int32_t)(
                    (g3 & 0xFF) | v25 | v26 | 
                    (v23 & 0xFFFF) << 8 | 
                    (v24 & 0xFFFF) << 10 |
                    v27 | v28 | v29 | v30 | 64
                ); // 0x80495f7_0


            g3 = v31 % 2 != 0; // check bit 0 set
            g2 = (v31 & 2) != 0; // check bit 1 set
            g10 = (v31 & 4) != 0; // check bit 2 set
            g4 = (v31 & 8) != 0; // check bit 3 set
            g8 = (v31 & 16) != 0; // check bit 4 set
            g6 = (v31 & 32) != 0; // chekc bit 5 set
            

            //int2_t v32 = (int2_t)(v31 / 256) & -2; // 0x804960a
            int2_t v32 = (int2_t)(v31 >> 8) & 0b10; // 0x804960a
            g5 = v32; // check 
            int2_t v33 = (int2_t)(v31 >> 10) & 0b10; // 0x804960a
            g7 = v33;
            g9 = (v31 & 0x1000) != 0;
            int32_t v34 = g1; // 0x8049613
            if (*(int32_t *)(v34 + v11) == 0) {
                v9++;
                // 0x8049626
                if (v9 >= 5) {
                    // break -> 0x8049635
                    break;
                }
                v8 = v34;
                v20 = v33;
                v21 = v32;
                // continue -> 0x804956f
                continue;
            }
            return 0;
        }
        return 1;
    }

---
Important to say, I wasted a lot of time here before I realised that `g2` through `g10` are used for some FPU control flags. 
(They are FPU control registers as stated in the comments provided by Retargetable Decompiler: `fpu_ctrl_DM`, `fpu_ctrl_IM`, `fpu_ctrl_OM`, etc...)

Hence, we can safely *IGNORE* all the variables `g2` to `g10` and those related to it (woot! less codes!).

    int32_t g1 = 0; // ebp

    int32_t level_five(void) {
        int32_t v1 = *(int32_t *)20; // 0x80494e8
        
        print_level5_header();

        int32_t v2, v3, v4, v5, v6;
        scanf("%f %f %f %f %f", &v6, &v5, &v4, &v3, &v2);

        while (getchar() != 10); // WAIT FOR NEWLINE CHAR

        int32_t v7;
        int32_t v8 = &v7; // 0x8049579

        int32_t v9 = 0;
        while (true) {
            int32_t v11 = 4 * v9 - 52; // 0x8049572
            int32_t v13 = 4 * v9 - 32; // 0x8049579
            fov(*(float32_t *)(v13 + v8));

            // Removed the FPU control thingy

            int32_t v12 = *(int32_t *)(v11 + v8); // 0x8049572
            printf("%d %d\n", (int32_t)round(0.0), v12);
            fov(*(float32_t *)(g1 + v13));
            round(0.0);

            // Removed more FPU control thingy

            if (*(int32_t *)(g1 + v11) == 0) {
                v9++;
                if (v9 >= 5) {
                    break;
                }
                v8 = g1;
                v20 = v33;
                v21 = v32;
                continue;
            }
            return 0;
        }
        return 1;
    }

Now, it's quite easy to understand, the 5 inputted floats go through Fast inverse square root and compared to a value in memory.

    int32_t v11 = 4 * v9 - 52; // 0x8049572

    int32_t v13 = 4 * v9 - 32; // 0x8049579
    fov(*(float32_t *)(v13 + v8));
    
    int32_t v12 = *(int32_t *)(v11 + v8); // 0x8049572
    fov(*(float32_t *)(g1 + v13));


(where `v8 = g1 = $ebp`)

---

The loop runs 5 times (`if (v9 >= 5) break;`)
so the comparison is made to the following offsets (accessed in this order):

    -52, -48, -44, -40, -36

This is where we need Hopper Decompiler to check the values which Retargetable Decompiler missed out.

    ; Variables:
    ;    var_C: -12
    ;    var_20: -32
    ;    var_24: -36
    ;    var_28: -40
    ;    var_2C: -44
    ;    var_30: -48
    ;    var_34: -52
    ;    var_38: -56
    ;    var_3A: -58
    ;    var_3C: -60
    ;    var_40: -64
    ;    var_4C: -76
    ;    var_54: -84
    ;    var_58: -88

What we want are `var_34`, `var_30`, `var_2C`, `var_28`, `var_24` (in order)

    level_five:
    (...)
    080494ef         xorl       %eax, %eax
    080494f1         movl       $0x3, var_34(%ebp)
    080494f8         movl       $0x1, var_30(%ebp)
    080494ff         movl       $0x3, var_2C(%ebp)
    08049506         movl       $0x3, var_28(%ebp)
    0804950d         movl       $0x7, var_24(%ebp)
    08049514         movl       banner, %eax


Hence, the values are accessed in this order: `0x3, 0x1, 0x3, 0x3, 0x7`

---

Inverse square root is applied to our input. We need to key in the reverse of `3, 1, 1, 3, 7`.
Fast inverse square root is `1/sqrt(x) = y`. Opposite is `x = (1 / y)^2`.

    $ python3
    >>> x = [3, 1, 3, 3, 7]
    >>> list(map(lambda y: (1/y)**2, x))
    [0.1111111111111111, 1.0, 0.1111111111111111, 0.1111111111111111, 0.02040816326530612]

So now we key it in and we get the flag!

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
    ================================================================
                                LEVEL 05                              
    ================================================================
    Enter secret code: 0.1111111111111111 1.0 0.1111111111111111 0.1111111111111111 0.02040816326530612
    GCTF{1nv3r53_r0075_m4d3_1n3ff1c13n7}

## Flag
`GCTF{1nv3r53_r0075_m4d3_1n3ff1c13n7}`