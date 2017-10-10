# Documentation
Forensics - 10 points

## Challenge 
> Microsoft Word is a word processer developed by Microsoft...

> Creator - @exetr

[c6a5898985b71d00ebcdd939c2af424a.docx](c6a5898985b71d00ebcdd939c2af424a.docx)

## Solution

Upon opening the .docx, we see this

	Here is the first part: GCTF{
	Well, the rest is somewhere here, try looking harder.

`.docx` is basically a `.zip` file. Rename to `.zip` and open it.
Looking through all the files we find the fragments of the flag


#### `./word/_rels/document.xml`
	
	Part 2: 3v3rywh3r3_t0

#### `./docProps/core.xml`
	
	Part 3: _l00k_m4ny

#### `./docProps/custom.xml`
	
	Part 4: _Th1ng5_t0_f1nd}

## Flag
`GCTF{3v3rywh3r3_t0_l00k_m4ny_Th1ng5_t0_f1nd}`