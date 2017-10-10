# COOKIE AGENT
Web - 40 points

## Challenge 
> I found this mysterious secret agency site while browsing the web, please help me find out what conspiracies lies within??!!?

> http://web.chal.gryphonctf.com:17561

> Creator - @paux

## Solution

Look at the source code of the main page. We see the background image is set to `others/cookiecookie.jfif`.

Let's take a look at the [`others/` directory](http://web.chal.gryphonctf.com:17561/others)
Immediately, we see the source code `backup.txt`.

In it, we see it reads [`check.txt`](http://web.chal.gryphonctf.com:17561/check.txt) and compares the MD5 checksum of the username and password fields.

	String loc="http://localhost:8080/CookieAgent/check.txt";
	...
	...
	if (hashtext1.equals(line1)&&hashtext.equals(line2)){

Now from the source code, every odd line of MD5 is username and every even line is the password.

	while ((line1 = br.readLine()) != null&&(line2 = br.readLine()) != null) {

---

We can use a [MD5 hash lookup website to decrypt it](https://hashkiller.co.uk/md5-decrypter.aspx)

	80b412568909831f41783af8b00a72af [Not found]
	82a7dc7e103ad1c676d5fe5a7a6d6a20 MD5 : LASTONEHERE
	80b412568909831f41783af8b00a72af [Not found]
	82a7dc7e3332399676d5fe5a7a6d6a20 [Not found]
	80b4125689098bbaa44ffbba5fba72af [Not found]
	bfacbfabe103ad1c676d5e5a7a6d6a20 [Not found]
	1734032192912334fbfd016795682550 [Not found]
	f3344fabc9f71a86bb4d8449e51b3ae8 [Not found]
	7843b2223341486466614ec79395d77f [Not found]
	223344fffbbcc443fbc49ec79395d76b [Not found]
	ea13be91ab93032f56face835720a609 MD5 : hueh
	ff0595c63cb68b7de64596f5b4b2da18 [Not found]
	80b45ff9ade7275cd774f7f8b00a72ab [Not found]
	5fb872ac29272c00fffffffa0d540a78 [Not found]
	7843b21cefc1486466614ec79998d77f [Not found]
	bb4adcf1715d30f9eb078ea82ff4d0e4 MD5 : wfedcz
	a0d540a78cd61daa5fb872ac29272c00 MD5 : goodpassword
	7843b21cefc1486466614ec79395d77f [Not found]
	bb4adcf1715d30f9eb078ea82ff4d0e4 MD5 : wfedcz
	51d7f57047d1769f9bedeabd9df06c6c [Not found]
	ce06d703bc2893d2e7a6afc82ff78566 [Not found]
	1734032192912f58b33d016795682550 [Not found]
	f5e85fcdc9f71a86bb4d8449e51b3ae8 [Not found]
	5ebe2294ecd0e0f08eab7690d2a6ee69 MD5 : secret
	3c4e04228db1f380f710afe1dc5c1a97 [Not found]
	63a9f0ea7bb98050796b649e85481845 MD5 : root
	a318e4507e5a74604aafb45e4741edd3 MD5 : roottoor
	5d41402abc4b2a76b9719d911017c592 MD5 : hello
	7843b21cefc1486466614ec79395d77f [Not found]
	09035b24bde65140a4d180244acd36c8 [Not found]
	d33f8b4f0b54d2267473bf2e0e89c0d6 [Not found]
	8f78e40af99ed65697ae9896a71c45e8 [Not found]
	1b9fd748db8ca72573133c52703f9768 [Not found]
	22df5156585cd99b492479da8284a8dd [Not found]
	c9d54183a875472f7e7025d7b37e3a07 MD5 : secret[space]user
	eade44c72812f5975c2badb120297061 [Not found]
	2034f6e32958647fdff75d265b455ebf MD5 : secretpassword
	1734032192912f58b33d016795682550 [Not found]
	f5e85fcdc9f71a86bb4d8449e51b3ae8 [Not found]
	5ebe2294ecd0e0f08eab7690d2a6ee69 MD5 : secret
	3c4e04228db1f380f710afe1dc5c1a97 [Not found]
	ea13be91ab93032f56face835720a609 MD5 : hueh
	ff0595c63cb68b7de64596f5b4b2da18 [Not found]
	80b45ff9ade7275cd774f7f8b00a72ab [Not found]
	a0d540a78cd61daa5fb872ac29272c00 MD5 : goodpassword
	a038080bc8208c7f00837e8d2558df0f MD5 : TOPSECRET
	82345778ade7275cd774f7f8b00a72ab [Not found]
	80b45ff91112432442566348b00a3332 [Not found]
	99b45ff9ade7275cd774f7f812323445 [Not found]
	8aabba12111aab11a1aa11bb243223fb [Not found]
	ffbb22300324003003469948b00a72ab [Not found]
	bb4adcf1715d30f9eb078ea82ff4d0e4 MD5 : wfedcz

With this, we found a working username/password pair 

	a0d540a78cd61daa5fb872ac29272c00 MD5 : goodpassword
	a038080bc8208c7f00837e8d2558df0f MD5 : TOPSECRET

Try the login and we get past the first stage!

---

Next, we need to get the User-Agent string.

If you scroll to bottom of `backup.txt`. We see a base64-encoded string

	$ cat backup.txt | tail -n 1 | base64 --decode
	int arrange(int i){
		i=i+3;
		i=(i/2);
	        i=i*5-9*-11;
	        i=i/2*4;
	        i=i-200;
	        i=i/2;
	        i=i+100;
	        i=i%100;
		i=i+20;
		if(i!=20){
			return i;
		}
		for(int k=0;k<4;k++){
			i=arrange(i);
	        }
		i=i+i;
		return i;
	}

Converting to a quick python script, 
	
	>>> def arrange(i):
		i=i+3;
		i=(i/2);
		i=i*5-9*-11;
		i=i/2*4;
		i=i-200;
		i=i/2;
		i=i+100;
		i=i%100;
		i=i+20;
		if(i!=20):
		    return i;
		for k in range(4):
		    i=arrange(i);
		i=i+i;
		return i;
	>>> arrange(0)
	24

It uses index 24 of the array `a` when `num=0`. Index 24 of the array `a` is `iwonderthelengthofthisarray`

---

Lastly, we need `CookieDonationBox` > 0. Set it to `CookieDonationBox=1`.

I drafted a quick Python script and we get the password!

	$ python3 solve.py | html2text

	****** WELCOME goodpassword ! ******
	Dear authorised agent,
	Sufficiently paid!
	Heres the flag "GCTF{w3_ar3_7h3_c00k13_ag3nc9}"

## Flag
`GCTF{w3_ar3_7h3_c00k13_ag3nc9}`
