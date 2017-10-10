# FILECEPTION
Forensics - 20 points

## Challenge 
> Someone sent me this telling me there were important documents in there.. I think they sent me the wrong file?

Creator - @paux

[BESTESTMODEL_8d615d0598d4eaad913d6ba4ae829dbe.jfif](BESTESTMODEL_8d615d0598d4eaad913d6ba4ae829dbe.jfif)


## Solution

Checking the last few lines in strings of the file we see there is a ZIP file hidden inside (`PK`)

	$ strings BESTESTMODEL_8d615d0598d4eaad913d6ba4ae829dbe.jfif | tail -n 5
	#password is "long_pa55w0rd_y0u_c4nt_cr4ck"PK
	IMPORTANT DOCUMENTS/PK
	IMPORTANT DOCUMENTS/hi
	IMPORTANT DOCUMENTS/
	IMPORTANT DOCUMENTS/hi

We can extract it using `foremost`

	$ sudo apt-get foremost
	$ foremost BESTESTMODEL_8d615d0598d4eaad913d6ba4ae829dbe.jfif 

Now, extracted ZIP is at `./output/zip/00000014.zip`
Open it and type in the password `long_pa55w0rd_y0u_c4nt_cr4ck`

Finally, the flag is found

	$ cat output/zip/IMPORTANT\ DOCUMENTS/hi 
	GCTF{4_fi13_1n_4_f1l3_1n_4_f11e}

## Flag
`GCTF{4_fi13_1n_4_f1l3_1n_4_f11e}`