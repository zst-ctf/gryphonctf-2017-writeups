# AutoEncryptSys
Programming - 30 points

## Challenge 
> I retrieved a bunch of files from the an automatic encryption system online, I found out how they encrypt is by using aes followed by base64 encoding it and finally, storing it in a text file with the name being the key of the aes encryption. However, im only looking for one file that contains the flag... and i dont have time to look through all 1002 files could you please help me?

> Creator - @paux

[AES_bde9e30d6f7277e2d1724b193d37a1d6.zip](AES_bde9e30d6f7277e2d1724b193d37a1d6.zip)


## Solution

Loop through all files in the directory and AES ECB decode it.

	$ unzip AES_bde9e30d6f7277e2d1724b193d37a1d6.zip
    $ python3 solve.py 
       GCTF{wh4ts_1n_th3_f1l355}

## Flag
`GCTF{wh4ts_1n_th3_f1l355}`