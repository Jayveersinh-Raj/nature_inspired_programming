from random import randint
from genetic_algorithm import GeneticAlgorithm as ga
import math

# to store number of generation
generation = 0

def ga_loop(dist, population, mutation_probability):

    # calculate fitness for each
    # list to store fitness values
    global generation
    generation += 1
    
    # scores from fitting function
    scores = []
    sum = math.inf
    for p in population:
        scores.append(ga.fitness(dist, p, sum))
    min_score = sorted(scores)[0]
    max_score = sorted(scores, reverse=True)[0]
   
    # new population from mating pool
    new_population = []
    
    # making them as integers between 0 to 100, and getting their max
    int_scores = [((score-min_score)/max_score) for score in scores]

    int_scores = [ '%.2f' % elem for elem in int_scores]
    percnt_scores = [int(float(score)*100) for score in int_scores]

    max_per_score = max(percnt_scores)
    bar = '█'*int(max_per_score) + '-' * (100 - int(max_per_score))
    print(f"\r|{bar}| {max_per_score}%", end = "\r")

    max_score = max(percnt_scores)
 
  
    if(generation == 100):
        return (min(scores), population[percnt_scores.index(min(percnt_scores))])
   
    for _ in range(len(population)):
        # creating a mating pool of elements using their probabilities from fitting 
        mating_parents = ga.select(population, percnt_scores, max_score)       
        
        #print(f"0: {mating_parents[0]}, 1: {mating_parents[1]}, generation {generation}")
         # split from random points
        split_point = randint(0, len(dist)-1)        
        # crossover of those parents to yield a breed
        breed = ga.crossover(mating_parents[0], mating_parents[1], split_point)        # mutating the produced breed and adding it to the population
        new_population.append(ga.mutate(breed, mutation_probability))  #
        # Repeat by calculating the fitness
    return ga_loop(dist, new_population, mutation_probability)