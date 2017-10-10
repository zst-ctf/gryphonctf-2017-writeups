#!/usr/bin/env python3

import socket
import re
import random

class Maze:

    direction = 'w'
    instructions = ''

    def __init__(self, maze_array):
        self.maze = maze_array
        self.start_position = self.get_coord_of_char('@')
        self.current_position = self.start_position
        self.end_position = self.get_coord_of_char('$')

    def get_char_from_coord(self, x, y):
        """
        Return character at the given (x, y) coordinates
        """
        return self.maze[y][x]

    def get_coord_of_char(self, ch):
        """
        Return first (x, y) coordinates of the given
        character closest to (0, 0) in the top left.
        """
        y = [i for i, row in enumerate(self.maze) if (ch in row)]
        y = y[0]
        # print(y)
        x = self.maze[y].index(ch)
        return (x, y)

    def change_direction(self):
        if not random.getrandbits(1):
            return
        next_direction = random.choice('wasd')
        #next_direction = 'dsaw'[('dsaw'.index(self.direction) + 1) % 4]
        self.direction = next_direction


    def get_position_from_direction(self, x, y, direc):
        if direc == 'w':  # UP
            new_position = (x, y - 1)
        elif direc == 's':  # DOWN
            new_position = (x, y + 1)
        elif direc == 'a':  # LEFT
            new_position = (x - 1, y)
        elif direc == 'd':  # RIGHT
            new_position = (x + 1, y)
        else:
            raise Exception('Unknown direction', direc)
        return new_position

    def try_move(self, iteration=0):
        x = self.current_position[0]
        y = self.current_position[1]
        new_position = self.get_position_from_direction(x, y, self.direction)

        # not valid move, negative coordinates = out of grid
        if new_position[0] < 0 or new_position[1] < 0:
            return False

        # not valid move, y is more than number of rows
        if new_position[1] >= len(self.maze):
            return False

        # not valid move, x is more than number of cols
        if new_position[0] >= len(self.maze[0]):
            return False

        coord_char = self.get_char_from_coord(*new_position)

        # not valid move, position not allowed
        if coord_char == '-':
            return False

        # allowed position
        if coord_char == '+' or coord_char == '$' or coord_char == '@':
            self.current_position = new_position
            #print('\rMove to ', new_position, self.direction, end='')
            return True

        raise Exception('Unknown value after trying move',
                        new_position, self.current_position,
                        self.direction, coord_char)

    def restart(self):
        self.current_position = self.start_position
        self.instructions = ''
        #print('\rRestarting', end='')

    def calculate(self):
        while self.current_position != self.end_position:
            if self.try_move() is True:
                self.instructions += self.direction
            self.change_direction()

            # if i went back to original position, discard the useless steps
            if self.current_position == self.start_position:
                self.restart()

            if len(self.instructions) > (1024):
                self.restart()

        # remove duplicated steps
        self.instructions = (self.instructions
                                 .replace('ws', '')
                                 .replace('sw', '')
                                 .replace('da', '')
                                 .replace('ad', ''))
        return self.instructions

    def verify(self, instructions):
        pos = self.start_position
        for step in instructions:
            pos = self.get_position_from_direction(*pos, step)
            if self.get_char_from_coord(*pos) == '-':
                return False
        if self.get_char_from_coord(*pos) != '$':
            return False

        return True


ansi_escape = re.compile(r'\x1b[^m]*m')


def plaintext(sometext):
    # Remove console color codes
    # https://stackoverflow.com/a/14693789
    return ansi_escape.sub('', sometext)


def split_every_n(line, n):
    return [line[i:i+n] for i in range(0, len(line), n)]


def fix_garbled_maze_lines(data):
    if len(data) == len(data[0]):
        return data
    else:
        print(">> Fixing garbled line")
        return split_every_n(''.join(data), len(data[0]))


def get_payload(data):
    data = plaintext(data)
    data = data.replace('PATH 2 TAEK >', '')
    data = data.replace(' ', '')
    data = data.splitlines()[1:]
    data = list(filter(lambda x: '+' in x or '-' in x, data))
    # https://stackoverflow.com/questions/16099694/how-to-remove-empty-string-in-a-list

    data = fix_garbled_maze_lines(data)
    print('Raw maze:', data)
    maze = Maze(data)
    reply = maze.calculate()
    #print(">> VERIFIED:", maze.verify(reply))
    return reply

if __name__ == '__main__':
    s = socket.socket()
    s.connect(('prog.chal.gryphonctf.com', 17454))
    s.settimeout(5)

    while True:
        data = s.recv(4096*16).decode().strip()
        if not data:
            continue

        if 'PRES ENTR 2 START!' in data:
            s.send(b'\n')
        elif 'ROUND ' in data:
            # Fix weird bug of data coming in halfway
            while ('PATH 2 TAEK >' not in data):
                #data += '\n'
                data += s.recv(4096).decode().strip()
            print("Received:", data)

            payload = get_payload(data) + '\n'
            s.send(payload.encode())
            print("\rComputed:", payload, end='')
            continue

        print("Received:", data)

        if ('U R NOT ALLOWD 2 STEP THAR!' in data or
            'U ENDD IN DA WRONG PLACE!' in data or
            'U RAN OUT OV TIEM!' in data):
            quit()

