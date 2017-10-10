# Turducken
Forensics - 35 points

## Challenge 
> We are having Turducken for dinner, but I only want chicken, can you get it for me? Multiple tools have been used to prepare the dish though, you need to have java installed to attempt the challenge

> Recommended Reads
https://www.slideshare.net/hussainsavani/image-steganography
http://resources.infosecinstitute.com/steganography-and-tools-to-perform-steganography/
http://www.topbestalternatives.com/best-steganography-software/
https://www.geekdashboard.com/best-steganography-tools/

> Enjoy~

	[Update] 05/10/2017 10:36PM - Updated distrib
	[Update] 07/10/2017 07:00PM - Hint 1 released
	[Update] 08/10/2017 07:20PM - Hint 2 released

> Creator @ESLunarPhoenix

## Hint 1
> Check out the recommended reads and analyse the task more

## Hint 2
> The passwords are in turducken and part of turducken

## Solution

The challenge says we need Java. From the recomended reads, the only Java tools are [RSteg](https://github.com/akush/rSteg), [OpenStego](https://github.com/syvaidya/openstego/releases) and [StegoShare](stegoshare.sourceforge.net).

---

If you do a strings on the file, we can see it is using OpenStego! 

	$ strings Turducken-c247048d1c014ad3725982971a05a1f8_3F000FC8074080AA568A788896045692.png | tail -n 3
	}]_p
	IEND
	OpenStego0.7.1

[Download that software](https://github.com/syvaidya/openstego/releases) and try to extract the file.

To get the password, hint 2 says: The passwords are in turducken and "part of turducken".

What is turducken?
> Turducken is a dish consisting of a deboned chicken stuffed into a deboned duck, further stuffed into a deboned turkey

So the password is either `chicken`, `duck`, or `turkey`.
Try each password and we get a success for `turkey`! 

*Extracting takes a while.*

Extracted file: `efecf2cabdb882e968544525559e11802bcd4de0.png`

---

Do a strings on the new file. 

	$ strings ./output/efecf2cabdb882e968544525559e11802bcd4de0.png | tail -n 3
	!-?E
	IEND
	OpenStego0.7.1

It is in OpenStego again! Extract it using password `duck`.

Extracted file: `Honey Chicken(Don't forget about the coffee).png`

---

Finally, we get another PNG which is not using OpenStego. Since StegoShare does not support PNGs, we try [RSteg](https://github.com/akush/rSteg) with the password `chicken`

## Flag
`GCTF{H0n3st1y_I_pr3f3r_f1sh}`
