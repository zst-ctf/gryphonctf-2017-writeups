# Time To Crypt
Crypto - 55 points

## Challenge 
> Alice has just learnt about encryption and OTPs in Applied Cryptography. Now she wants to put her knowledge to the test. She successfully implemented OTPs into her Java code, but the lecturer said that it is insecure.

> Creator - @Platy

[Time_to_Crypt_602b68ab5e57895dfd96ce7cb38d0bea.zip](Time_to_Crypt_602b68ab5e57895dfd96ce7cb38d0bea.zip)

## Hint
> She did not fully understand that 'OT' in 'OTP' stands for 'One-Time'

## Solution
From the source, we can see `encrypt()` is a simple XOR cipher.
Both `flag` and `text` are the same length. They are both encrypted, with `text` being always fixed. Hence, we can do XOR of the original `text` and the encrypted `text` to get the key.

	$ unzip Time_to_Crypt_602b68ab5e57895dfd96ce7cb38d0bea.zip
	$ mv "Time to Crypt" Time_to_Crypt
	$ cp Solver.java ./Time_to_Crypt/Solver.java
	$ javac ./Time_to_Crypt/*.java
	$ java Time_to_Crypt.Solver
	FLAG: GCTF{p4ds_u53d_0n3_700_m4ny_71m35}

## Flag
`GCTF{p4ds_u53d_0n3_700_m4ny_71m35}`