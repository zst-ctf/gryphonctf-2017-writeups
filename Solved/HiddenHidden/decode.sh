#!/bin/bash

unzip hiddenflag_6d94c51b0be2bd4a35daf690850df2c0.zip

cat hiddenflag \
	| perl -lpe '$_=pack"B*",$_' \
	| base64 --decode \
	| perl -lpe '$_=pack"B*",$_' \
	| base64 --decode \
	| perl -lpe '$_=pack"B*",$_' \
	| base64 --decode \
	| perl -lpe '$_=pack"B*",$_' \
	| base64 --decode \
	| perl -lpe '$_=pack"B*",$_' \
	| base64 --decode \
	| perl -lpe '$_=pack"B*",$_' \
	| base64 --decode \
	> flag.txt

cat flag.txt

rm hiddenflag
rm flag.txt