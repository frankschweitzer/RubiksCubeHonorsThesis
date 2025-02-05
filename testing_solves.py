# human method
from rubik.cube import Cube
from rubik.solve import Solver

# math method
import kociemba


print('BEGINNER METHOD SOLVER')
# declare human method scramble
human_cube = Cube('YORYWGOWGRRBYBWOOWGWBOOYGGGRRWGBYRRYGBWOOGYBBRYBWYBWRO')
print(human_cube)

# solve using human method
human_solve = Solver(human_cube)
human_solve.solve()
print(human_solve.moves)
print(f'Scramble was solved via Beginners Method using {len(human_solve.moves)} moves')


print('KOCIEMBA SOLVER')
# declare kociemba scramble
up = 'yyrwwbgrb'
left = 'rbwrowgow'
front = 'ogyogwogr'
right = 'oobgrryyy'
back = 'wbbybborr'
down = 'bogyygwwg'
math_cube = up + right + front + down + left + back
math_cube = math_cube.replace('w', 'U')
math_cube = math_cube.replace('r', 'R')
math_cube = math_cube.replace('g', 'F')
math_cube = math_cube.replace('y', 'D')
math_cube = math_cube.replace('o', 'L')
math_cube = math_cube.replace('b', 'B')
print(math_cube)

# solve using math method
kociemba_solve = kociemba.solve(math_cube)
print(f'Scramble was solved via Kociemba"\'"s method using {kociemba_solve} moves')