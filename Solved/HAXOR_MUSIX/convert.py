#!/usr/bin/env python3

with open('index.txt', 'r') as f:
    code = f.read()

# remove header
code = code.splitlines()[14:]

# join code together
code = ' '.join(code).strip()

items = code.split(' ')

bf = ''
while len(items) > 0:
    a = items.pop(0)
    b = items.pop(0)

    instruction = '{} {}'.format(a, b)

    if instruction == "Ook. Ook?":
        bf += '>'

    elif instruction == "Ook? Ook.":
        bf += '<'

    elif instruction == "Ook. Ook.":
        bf += '+'

    elif instruction == "Ook! Ook!":
        bf += '-'

    elif instruction == "Ook. Ook!":
        bf += ','

    elif instruction == "Ook! Ook.":
        bf += '.'

    elif instruction == "Ook! Ook?":
        bf += '['

    elif instruction == "Ook? Ook!":
        bf += ']'

    else:
        print('Invalid instruction:', instruction)
        quit()

print(bf)