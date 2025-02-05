# Rubik's Cube Solver

This project is a senior honors thesis that implements a reinforcement learning-based Rubik's Cube solver using Q-learning. The project includes several components:

- `qLearn.py`: Performs Q-learning and prints the results to `q_table.txt`.
- `rubik_solver.py`: Uses the Q-table to attempt to solve various scrambles.
- `testing_solves.py`: Compares the Q-learning solutions to the Kociemba and human methods.

## Q Learning

In order to improve training, the qLearn script was ran on my universities super computer cluster.  Training covered about 30 million different Rubik's cube scrambles which took around 24 hours to complete.

### How to Run

#### Train the Q-learning model:
```bash
python qLearn.py
```

#### Use the Q-table to solve scrambles:
```bash
python rubik_solver.py
```

#### Compare solutions:
```bash
python testing_solves.py
```

## Requirements

- Python 3.11.7
- NumPy
- TensorFlow
- Keras
- Rubik's Cube library

## Conclusion

This project demonstrates the application of reinforcement learning to solve the Rubik's Cube. The Q-learning algorithm is trained to find optimal solutions, and the results are compared with traditional solving methods.  Feel free to reach out with any questions or if you are curious in reading the paper to learn more about my findings.