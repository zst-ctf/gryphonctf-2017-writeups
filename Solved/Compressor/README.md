# Compressor
Misc - 25 points

## Challenge 
> I want to make my text file very very small! So, I did what any sane person would do and shoved it into my compressor and ran it 10 times!

Creator - @exetr

[level0_564546f2b66ff26cc3b94f352aaeead5.rar](level0_564546f2b66ff26cc3b94f352aaeead5.rar)

## Solution
For this challenge, we are faced with 10 levels of differing archive files. Some dependencies were installed along the way

For Mac: `brew install unzip unrar lzip rzip lzop p7zip`

	$ unrar e level0_564546f2b66ff26cc3b94f352aaeead5.rar
	
	$ file level1
	level1: Zip archive data, at least v1.0 to extract
	$ unzip level1

	$ file level2
	level2: gzip compressed data, was "level3", from Unix, last modified: Thu Sep 28 20:30:44 2017
	$ gzip --decompress level2 --suffix '' --name --keep

	$ file level3
	level3: POSIX tar archive (GNU)
	$ tar xfk level3

	$ file level4
	level4: bzip2 compressed data, block size = 900k
	$ bzcat -k level4 > level5

	$ file level5
	level5: lzip compressed data, version: 1
	$ lzip -d -k level5
	$ mv level5.out level6

	$ file level6
	level6: xz compressed data
	$ mv level6 level6.xz
	$ xz -d -k level6.xz
	$ mv level6 level7

	$ file level7
	level7: rzip compressed data - version 2.1 (2228 bytes)
	$ rzip -d -S '' -o level8 level7

	$ file level8
	level8: lzop compressed data - version 1.030, LZO1X-1, os: Unix
	$ mv level8 level8.lzop
	$ lzop -d level8.lzop -o level9

	$ file level9
	level9: ISO 9660 CD-ROM filesystem data 'CDROM
	$ 7z x level9

	$ file LEVEL10 
	LEVEL10: ASCII text, with very long lines, with no line terminators

From here we see `LEVEL10` is a base64 encoded file, and `level11` is a binary encoded string.
	
	$ cat LEVEL10 | base64 --decode > level11
	$ cat level11 | perl -lpe '$_=pack"B*",$_' > level12
	$ cat level12
	GCTF{m4ny_m4ny_l4y3r5_0f_c0mpr3ssi0n}

## Flag
`GCTF{m4ny_m4ny_l4y3r5_0f_c0mpr3ssi0n}`
