# Algorithms-AI2

# AI Algorithms in Python

This repository contains Python implementations of various AI algorithms, including WalkSAT, GSAT, WalkSAT with heuristic, and GSAT with random walk.

## Table of Contents

- [Introduction](#introduction)
- [Algorithms Implemented](#algorithms-implemented)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Artificial Intelligence (AI) algorithms play a significant role in solving complex problems and decision-making processes. This repository provides Python implementations of essential AI algorithms, enabling developers and enthusiasts to understand, experiment, and utilize these algorithms in various applications.

## Algorithms Implemented

### 1. WalkSAT

WalkSAT (Walk SATisfiability) is a local search algorithm used to solve Boolean satisfiability (SAT) problems. It iteratively flips the truth values of variables to satisfy as many clauses as possible, aiming to find a satisfying assignment.

### 2. GSAT

GSAT (Greedy SATisfiability) is a variant of WalkSAT that employs a greedy strategy to choose which variable to flip. It selects the variable that maximizes the number of satisfied clauses, potentially leading to faster convergence in certain cases.

### 3. WalkSAT with Heuristic

WalkSAT with heuristic incorporates additional heuristics to guide the variable selection process, aiming to improve the efficiency of the algorithm by prioritizing variables likely to contribute to clause satisfaction.

### 4. GSAT with Random Walk

GSAT with random walk introduces a random walk component to the GSAT algorithm, allowing it to escape local optima and explore the search space more extensively. This randomness enhances the algorithm's ability to find satisfying assignments, particularly in challenging problem instances.

## Usage

To use the algorithms implemented in this repository, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/proplayer5555/Algorithms-AI2.git
    ```

2. Navigate to the directory containing the algorithms:

    ```bash
    cd ai-algorithms-python
    ```

3. Choose the algorithm you want to use and run the corresponding Python file:

    ```bash
    python walksat.py
    ```

4. Follow the prompts or customize the input parameters as needed for your specific problem.

## Contributing

Contributions to this repository are welcome! If you have suggestions for improvements, bug fixes, or new algorithms to add, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
