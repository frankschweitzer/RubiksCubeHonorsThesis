import kociemba
import random
import time
from rubik import solve
from rubik.cube import Cube
from rubik.solve import Solver
from rubik.optimize import optimize_moves

up = 'rybbyyyyy'
left = 'goooobooo'
front = 'bbgrbbbob'
right = 'orrwrrrrg'
back = 'ygwgggrgg'
down = 'wywwwwwwy'
cube = up + right + front + down + left + back

cube = cube.replace('y', 'U')
cube = cube.replace('r', 'R')
cube = cube.replace('b', 'F')
cube = cube.replace('w', 'D')
cube = cube.replace('o', 'L')
cube = cube.replace('g', 'B')

print(cube)

solution = kociemba.solve(cube)

print(solution)
