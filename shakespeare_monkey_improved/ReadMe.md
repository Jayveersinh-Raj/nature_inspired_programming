## This is an improved version of previous
## Added functionalities
* Works for `ascii from 32 to 125` meaning, all the characters, numbers, letters, brackets. You can check its validity from ascii table. 
*You can also change the ascii values from the `populate function, and mutation function` from `GeneticAlgorithm class` inside `genetic_algorithm.py`
* Removed the mutation pool so it can work with large search space without an issue of space complexity
* `The method I used`: I generate the random index from population, and a random number in range of the max score. If that random number is less than the score of the individual at that index in population, I choose it for mating.
* *Got a heart from `The coding train` for coming up with this solution*

## Make sure
You should have a bigger initial population, since now we do not have space issue like before, and since the method I use does not work well if you have 0 fitness values in initial conditions, so remove the ones with 0 fitting, and thus to componsate for that, have a larger variations i.e. population
