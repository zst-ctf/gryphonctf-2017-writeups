# Up the Base
Misc - 25 points

## Challenge 
> My friend always felt that Twitter was not able to accomodate to his grandfather story with the measly 140 character limit. He recently learnt about Base Encoding. Since Twitter accepts unicode characters, he decided to increase the base.

>Creator - @Platy

https://2017.gryphonctf.com/files/e079a3171158a3dee45546dd087d7b55/output_128d62817031d5fe21821f918fb08fed.bin

## Solution

Searching for "base encoding using unicode" on Google will lead us to [base65536 encoding](https://www.npmjs.com/package/base65536).

	$ npm install --global base65536

	$ cat output_128d62817031d5fe21821f918fb08fed.bin | base65536 --decode
	Base64 is used to encode arbitrary binary data as "plain" text using a small, extremely safe repertoire of 64 (well, 65) characters. Base64 remains highly suited to text systems where the range of characters available is very small -- i.e., anything still constrained to plain ASCII. Base64 encodes 6 bits, or 3/4 of an octet, per character.
	However, now that Unicode rules the world, the range of characters which can be considered "safe" in this way is, in many situations, significantly wider. Base65536 applies the same basic principle to a carefully-chosen repertoire of 65,536 (well, 65,792) Unicode code points, encoding 16 bits, or 2 octets, per character. This allows up to 280 octets of binary data to fit in a Tweet.

	Link to base65536: https://github.com/qntm/base65536
	Anyways thanks for reading, here is the flag: GCTF{1f_17_l00k5_57up1d_bu7_17_w0rk5_17_41n7_57up1d}

## Flag
`GCTF{1f_17_l00k5_57up1d_bu7_17_w0rk5_17_41n7_57up1d}`