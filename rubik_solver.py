import random
import time
from rubik.cube import Cube
from rubik.solve import Solver
from rubik.optimize import optimize_moves

SOLVED_CUBE_STR = "OOOOOOOOOYYYWWWGGGBBBYYYWWWGGGBBBYYYWWWGGGBBBRRRRRRRRR"
MOVES = ["L", "R", "U", "D", "F", "B", "M", "E", "S"]

original_cube = Cube("OOOOOOOOOYYYWWWGGGBBBYYYWWWGGGBBBYYYWWWGGGBBBRRRRRRRRR")
def random_cube():
    scramble_moves = " ".join(random.choices(MOVES, k=1))
    print(scramble_moves)
    rand_cube = original_cube
    rand_cube.sequence(scramble_moves)
    return rand_cube


def run():
    i = 0
    
    # amount of cubes solved correctly vs incorrectly
    successes = 0
    failures = 0

    # storing number of moves used for optimal vs non-optimal solutions as well as time
    avg_opt_moves = 0.0
    avg_moves = 0.0
    avg_time = 0.0
    while i < 5:
        # generate random cube and solve for the cube
        C = random_cube()
        print(C.flat_str())
        solver = Solver(C)

        start = time.time()
        solver.solve()
        print(solver.moves)
        duration = time.time() - start

        if C.is_solved():
            opt_moves = optimize_moves(solver.moves)
            successes += 1
            avg_moves = (avg_moves * (successes - 1) + len(solver.moves)) / float(successes)
            avg_time = (avg_time * (successes - 1) + duration) / float(successes)
            avg_opt_moves = (avg_opt_moves * (successes - 1) + len(opt_moves)) / float(successes)
        else:
            failures += 1
            print(f"Failed ({successes + failures}): {C.flat_str()}")

        total = successes + failures
        if total == 1 or total % 100 == 0:
            # print out benchmarks every 100 solves
            pass_percentage = 100 * successes / total
            print(f"{total}: {successes} successes ({pass_percentage:0.3f}% passing)"
                  f" avg_moves={avg_moves:0.3f} avg_opt_moves={avg_opt_moves:0.3f}"
                  f" avg_time={avg_time:0.3f}s")
        
        i += 1


if __name__ == '__main__':
    run()