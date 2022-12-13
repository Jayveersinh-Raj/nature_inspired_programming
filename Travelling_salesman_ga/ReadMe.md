## This is the `Travelling salesman problem's` solution, using `genetic algorithm`
This is optimized solution, similar to `shakespeare monkey improved` from this repository. 

## Key approaches similar to shakespeare monkey improved `from this repository` for optimized solution
* *Fitness are the sum of total distance `normalized to .2f float multiplied by 100`*
* *Due to the above `fitness`, and problem being `minimization`, in the `accept-reject` probability in `accept` function in the class `GeneticAlgorithm` implements `1-probability` scheme which means that the lesser the distance, likely it is to be picked. `For example:` distance with 10 has 90% of chance being picked (100-10 = 90).*

## hyperparameters.yaml
It is the yaml file that contains `hyper-parameters` that one can `tweek, experiment or play with` without changing anything in the code.
