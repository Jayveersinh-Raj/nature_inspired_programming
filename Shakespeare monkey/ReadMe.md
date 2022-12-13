## This is a Shakespeare monkey program using genetic algorithm
On given an input, the program guesses the input using genetic algorithm, provided the value has an ascii value in `[65,122] U {32,46}`

## To run it, type the following in the console
    python3 shakespeare_monkey.py

## Descprition of the files
* *shakespeare_monkey.py : The main driver file (entry point)*
* *validate_input.py : To validate the input by checking its ascii value, and return to main if it is valid*
* *main_loop_ga.py : The main loop that recursively calls the methods from `GeneticAlgorithms class` for generations, and returns the result if found.*
* *genetic_algorithm.py : Implements the `GeneticAlgorithm class` that contains all the methods of a genetic algorithm*

## Caution
Do not give an input with length `>30`, try it at your own risk because it implements a `mutation pool` version which increase the space complexity by storing the individuals `P` number of times where `P` is `Probability * 100`. 
* My computer if configured to end recursion after 1000 iterations, if yours is not than please consider using the `improved version` from this repository, or give a stopping iteration condition in the `main_loop_ga.py`
