# Where_Is_It
Forensics - 20 points

## Challenge 
> I realised there was suspicious traffic on my network.. It seems like someone is trying to communicate through it? Help me find out what it is?
Thanks!

> Creator - @paux

[suspicious_dcae5f9a6135df584e04b00a8109d913.pcap](suspicious_dcae5f9a6135df584e04b00a8109d913.pcap)

## Solution

After looking through all the packets in Wireshark, it appears the flag is within packets 86 to 122, one char at a time.

- `File` > `Export Specified Packets`
- Set Range: `86-122`
- Save as `flag.pcap`

Now we have a pcap of the flag data. Let's export a dump of the packets.

	$ tshark -x -r flag.pcap > flag_raw.txt

Notice that all the flag portions are at the ending of each packet.
It occurs on lines starting with `0040`. For each packet, get ending which appears after '@'.

Let's draft out a bash one-liner

	cat flag_raw.txt \
		| grep "0040"       # lines starting with 0040
		| cut -f 2 -d '@'   # get text after @ symbol
		| tr -d '\n'        # combine the lines into one
		| tr -d '.'         # delete the dots
	
Combine it and get the flag!

	$ cat flag_raw.txt | grep "0040" | cut -f 2 -d '@' | tr -d '\n' | tr -d '.'
	GCTF{4m0ng57_7h3_b175}

## Flag
`GCTF{4m0ng57_7h3_b175}`