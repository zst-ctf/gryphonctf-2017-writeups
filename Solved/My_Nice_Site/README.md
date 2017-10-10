# My Nice Site
Web - 10 points

## Challenge 
> Void has been working hard during the holidays. He says he has a very nice website that he coded. However, I cannot seem to open it. Can you help me?

> http://web.chal.gryphonctf.com:17566

> Creator - @Platy

## Solution
We have a site which take forever to load. Seems like it is on a redirect loop.
Let's try to view the the page using curl

	$ curl -s http://web.chal.gryphonctf.com:17566/ | html2text
	HAHAHA! I LIED ABOUT HAVING A NICE SITE
	GCTF{j4v45cr1p7_15_d4n63r0u5}

## Flag
`GCTF{j4v45cr1p7_15_d4n63r0u5}`