# Formatted
Sanity - 5 points

## Challenge 
> That file seems rather picturesque... I wonder why?
> Creator - @exetr

[20f41d9b6f29958326b785ce0aeef904.zip](20f41d9b6f29958326b785ce0aeef904.zip)

## Solution
Unzipping the archive gives us flag.txt

	$ unzip 20f41d9b6f29958326b785ce0aeef904.zip
	$ file flag.txt 
	flag.txt: PNG image data, 1280 x 720, 8-bit colormap, interlaced

This tells us it is a PNG. Rename to `.png` and open it to see the flag

	$ mv flag.txt flag.png
	$ open flag.png

## Flag
`GCTF{wr0ng-f0rma7z_n0t_g00d}`