from genetic_algorithm import GeneticAlgorithm
import main_loop_ga as main_loop
from validate_input import take_valid_input
import time

if __name__ == "__main__":
    
    t = time.time()
    # size of population
    population_size = 5000
    
    # mutation percentage
    mutation_per = 0.01

    # take valid input
    target = take_valid_input()
    print("\n")
    
    # Populate
    population = GeneticAlgorithm.populate(len(target), population_size)

    # main ga(genetic algorithm) loop to find the result
    result = main_loop.ga_loop(target, population, mutation_per)
    print(result)
    print(f"\nTime taken: {time.time()-t:.2f} seconds")
    