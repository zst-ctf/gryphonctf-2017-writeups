#!/usr/bin/env python

import string
from pwn import *
context(terminal = ['bash'])

def get_strcmp_result(payload):
	genesis = process(['gdb', './gen'])
	log.info(' ')

	#log.info('Set Breakpoint 1')
	genesis.recvuntil('(gdb)')
	genesis.sendline('break *0x80496bd')

	#log.info('Set Breakpoint 2')
	genesis.recvuntil('(gdb)')
	genesis.sendline('break *0x08049688')

	genesis.sendline('run')
	log.info('Running: ' + payload)

	genesis.recvuntil('hit Breakpoint 1, 0x080496bd')
	#log.info('At Breakpoint 1')
	genesis.recvuntil('(gdb)')
	genesis.sendline('call bonus()')

	genesis.recvuntil("LEVEL 99")
	#log.info('At LEVEL 99')
	genesis.sendline(payload)

	genesis.recvuntil("hit Breakpoint 2, 0x08049688")
	#log.info('At Breakpoint 2')
	genesis.recvuntil('(gdb)')
	genesis.sendline('p $eax')

	eax_info = genesis.recvline()
	strcmp_result = eax_info.split(' = ')[1]
	log.info('Result: ' + strcmp_result)

	genesis.kill()

	return int(strcmp_result) > 0


ASCII = ''.join(chr(x) for x in range(128))
#SEARCH_LIST = ASCII
SEARCH_LIST = string.printable

def find_letter(prefix=''):
	prev_result = None
	prev_letter = '0'
	for letter in SEARCH_LIST: 
		curr_result = get_strcmp_result(prefix + letter)
		if (prev_result != curr_result) and (prev_result is not None):
			print 'Found', prev_letter, letter
			return (prev_letter, letter)
			quit()
		prev_result = curr_result
		prev_letter = letter
	return None

def try_pair(prefix, a, b):
	result = find_letter(prefix + a)
	if result is not None:
		return (result, a)

	result = find_letter(prefix + b)
	return (result, b)



if __name__ == '__main__':
	prefix = ''#'d1d y0u 7h1nk 7h15 w0uld b3 34'
	a, b = find_letter(prefix)
	for i in xrange(30):
		print ">> Trying %d: %s" % (i, prefix)
		pair, success = try_pair(prefix, a, b)

		if pair is None:
			print 'ERROR:', i, pair
			print 'ERROR:', prefix + a 
			print 'ERROR:', prefix + b

		a, b = pair
		prefix += success

if __name__ == '__main__1':
	get_strcmp_result('d1d y0u 7h1nk 7h15 w0uld b3 34'+ '\xb6\xcc')

		


"""

# Start a process
genesis = gdb.debug("./gen",  '''
# inside main()
break *0x80496bd

# after bonus() user-input
break *0x08049688
run
call bonus()
''')
"""



# process('./gen')

# Attach the debugger
#gdb.attach(genesis,)


#run
#call bonus()

#set logging on

# Interact with the process
#genesis.sendline('f')

#gdb.send('p $eax')

'''
f
f
set logging on
p $eax
'''