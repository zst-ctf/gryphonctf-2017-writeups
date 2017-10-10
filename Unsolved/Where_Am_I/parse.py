
def parse1():

    with open('serial.out') as f:
        raw = f.read()


    prev = 0
    for line in raw.splitlines():
        if ('Waiting' in line or
            '********' in line): 
           continue

        curr = int(line[2:].strip())
        delta = curr - prev
        prev = curr

        print("Delta:", delta)


def parse2():
    with open('serial2.out') as f:
        raw = f.read()

    for line in raw.splitlines():
        if ('Waiting' in line or
            '********' in line): 
           continue
        if ('G' in line): quit()


        delta = int(line.split('=')[-1])

        if delta < 300:
            print(".", end='')
        else:
            print('-', end='')

    
parse2()