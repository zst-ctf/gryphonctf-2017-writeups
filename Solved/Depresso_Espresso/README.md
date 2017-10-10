# Depresso Espresso
Reverse - 60 points

## Challenge 
> I've intercepted a couple of files. I've been trying to work out how to use the program but it constantly gives me an error. I've drank countless cups of java, but I'm still stuck. Help me please!

> Creator - @Platy

[Depresso_Espresso_046eb2455d042de7b8af0556e160cbed.zip](Depresso_Espresso_046eb2455d042de7b8af0556e160cbed.zip)

## Hint
Feistel. Just Feistel.

## Solution

*(Hint is completely irrelevant, this is not Feistel cipher `>.>`)*

The entire object including the key, cipher and flag data objects are serialised and saved in `output.bin`. 
I simply wrote a Java class `GetKey.java` to read it back in.

	$ unzip Depresso_Espresso_046eb2455d042de7b8af0556e160cbed.zip 
	$ javac GetKey.java
	$ java GetKey
	This is the flag:
	GCTF{d35_l0v35_4_6r347_c1ph3r}

## Flag
`GCTF{d35_l0v35_4_6r347_c1ph3r}`