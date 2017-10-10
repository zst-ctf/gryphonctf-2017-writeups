#!/usr/bin/env python3

import socket
import re
import sys
sys.path.insert(0, './python-pathfinding')

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

class Maze:

    def __init__(self, maze_array):
        self.maze = maze_array
        self.start_position = self.get_coord_of_char('@')
        self.end_position = self.get_coord_of_char('$')

    def get_char_from_coord(self, x, y):
        # Return character at the given (x, y) coordinates
        return self.maze[y][x]

    def get_coord_of_char(self, ch):
        # Return first (x, y) coordinates of the given
        # character closest to (0, 0) in the top left.
        y = [i for i, row in enumerate(self.maze) if (ch in row)][0]
        x = self.maze[y].index(ch)
        return (x, y)

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

    def verify_path(self, instructions):
        pos = self.start_position
        for step in instructions.strip():
            pos = self.get_position_from_direction(*pos, step)
            if self.get_char_from_coord(*pos) == '-':
                return False
        if self.get_char_from_coord(*pos) != '$':
            return False

        return True

    def path_coord_to_moves(self, path):
        current = path.pop(0)
        moves = ''
        while len(path) > 0:
            next = path.pop(0)

            # check x, move right
            if next[0] > current[0]:
                moves += 'd'
            # check x, move left
            elif next[0] < current[0]:
                moves += 'a'
            # check y, move down
            elif next[1] > current[1]:
                moves += 's'
            # check y, move up
            elif next[1] < current[1]:
                moves += 'w'
            else:
                raise Exception(f'Unknown move {current} to {next}')

            current = next
        return moves

    def get_instructions(self):
        matrix = list(
            map(lambda line: list(map(lambda ch: ch == '-', line)),
                self.maze)
        )
        grid = Grid(matrix=matrix)

        start = grid.node(*self.start_position)
        end = grid.node(*self.end_position)

        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, grid)
        path_len = len(path)

        print('>> runs:', runs)
        print('>> path length:', path_len)
        print('>> path array:', path)
        print(grid.grid_str(path=path, start=start, end=end))


        instructions = self.path_coord_to_moves(path)
        assert (path_len - 1) == len(instructions), len(instructions)


        return instructions




ansi_escape = re.compile(r'\x1b[^m]*m')




def split_every_n(line, n):
    return [line[i:i+n] for i in range(0, len(line), n)]


def create_maze(data):
    # Remove console color codes
    # https://stackoverflow.com/a/14693789
    data = ansi_escape.sub('', data)

    # Remove non-maze strings
    data = data.replace('PATH 2 TAEK >', '')
    data = data.replace(' ', '')
    data = data.splitlines()[1:]

    # https://stackoverflow.com/questions/16099694/how-to-remove-empty-string-in-a-list
    data = list(filter(lambda x: '+' in x or '-' in x, data))

    # if maze lines has accidently merged,
    # split them up properly
    if len(data) != len(data[0]):
        print(">> Fixing garbled line")
        data = split_every_n(''.join(data), len(data[0]))

    print('Raw maze:', data)

    return Maze(data)



if __name__ == '__main__':
    s = socket.socket()
    s.connect(('prog.chal.gryphonctf.com', 17454))
    s.settimeout(5)

    while True:
        data = s.recv(4096*16).decode().strip()
        if not data:
            continue

        if 'ROUND ' in data:
            # Fix weird bug of data coming in halfway
            # wait until all of the maze is received
            while ('PATH 2 TAEK >' not in data):
                data += s.recv(4096).decode().strip()
            print("Received:", data)

            maze = create_maze(data)
            payload = maze.get_instructions() + '\n'
            maze.verify_path(payload)
            s.send(payload.encode())
            print("Computed:", payload, end='')
            continue

        if 'PRES ENTR 2 START!' in data:
            s.send(b'\n')
        
        print("Received:", data)

        if ('U R NOT ALLOWD 2 STEP THAR!' in data or
            'U ENDD IN DA WRONG PLACE!' in data or
            'U RAN OUT OV TIEM!' in data or
            'GCTF{' in data):
            quit()


