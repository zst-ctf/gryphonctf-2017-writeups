# Crypto Hotdogs
Crypto - 45 points

## Challenge 
> Our team, the Crypto Hotdogs seek for your help. We have encrypted our flag with the public key. However, some idiot told one of my team members that the command 'rm' meant 'remake'. Basically, he deleted our private key. Maybe you can help us.

>Creator - @Platy

[Crypto_Hotdogs_7c153234ded94f19ce764c1d18aca339.zip](Crypto_Hotdogs_7c153234ded94f19ce764c1d18aca339.zip)

## Hint
> Attack the sausages!

## Solution

This is similar to the solution for smallRSA in picoCTF 2017.

Use the Wiener attack as implicitly hinted in the title and the hint.

	python3 solve.py 
	Hacked!
	b'\x026\xf8\x8f\xa5\xe0\xf8d\xc7\xec\xd9\x1d1\tw<\x082\xc8\x98\xabL\x1b\x84\x16m\xfa\x8b\x15I\xfb\xb1\xd2xm\xf8^\xc9\x8d\x1f\x0e\t~jRF\xe9\xf8?9\xcd\x82=\xc0\xa5\xb8\xfd\xea\xe7\xc1\xad\x1a\xd8\xe2m\x9e\x96\x08\xb9J\xbf\xc1\x06\xf3i\xc0\xd3^\x8eF\xe8{\xab\xef\xa5\x0f)\xee\x9a\xadc\xf2\xa3\xb3\x0f\xc1G\x9du\x17+\xa4y\xb8\xd1\x92\x00GCTF{w0w_h0770_d06u}\n'

## Flag
`GCTF{w0w_h0770_d06u}`