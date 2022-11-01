from random import randint
from genetic_algorithm import GeneticAlgorithm as ga
import math

# to store number of generation
generation = 1
# to store the total distance (by default infinity)
sum = math.inf
# to early stop
dropout_counter = 0
# to store the best solution we have on a given generation
best_so_far = []

def ga_loop(dist, population, mutation_probability,dropout_number,n_generations):

    global generation
    global sum
    global best_so_far
    global dropout_counter

    # to stop on a particular epoch/generation
    if(generation == n_generations):
        return (sum, best_so_far)
    
    # if not getting better solution for a particular number of epochs, early stop, and return the best so far
    if(dropout_counter == dropout_number):
        print("\n dropped out")
        return (sum, best_so_far)
    
    # scores from fitting function
    scores = []
   
    # for every individual in the population find fitness, and get the (score, sum)
    for p in population:
        fitness = ga.fitness(dist, p, sum)
        scores.append(fitness[0])

        # if the found score is less than any previous best, replace it
        if(fitness[1]<sum):
          best_so_far = p
          sum = fitness[1]

          dropout_counter = 0

    dropout_counter+=1
    
    min_score = sorted(scores)[0]
    max_score = sorted(scores, reverse=True)[0]
       
    # normalizing the scores
    int_scores = [((score-min_score)/max_score) for score in scores]
    
    # getting them to double precision
    int_scores = [ '%.2f' % elem for elem in int_scores]

    # calculating them as percentage
    percnt_scores = [int(float(score)*100) for score in int_scores]
    
    # just a little fanciness for output
    bar = '█'*(int(generation/n_generations*100)) + '-' *(100 - int(generation/n_generations*100))
    print(f"\r|{bar}| {int(generation/n_generations*100)}%", end = "\r")

    max_score = max(percnt_scores)
 
    # new population from mating pool
    new_population = []
   
    # selecting the parents, crossing over, and mutation based on given mutation chance
    for _ in range(len(population)):

        # creating a mating pool of elements using their probabilities from fitting 
        mating_parents = ga.select(population, percnt_scores, max_score)       
        
         # split from random points
        split_point = randint(0, len(dist)-1)        

        # crossover of those parents to yield a breed
        breed = ga.crossover(mating_parents[0], mating_parents[1], split_point)        # mutating the produced breed and adding it to the population
        new_population.append(ga.mutate(breed, mutation_probability))  

    generation += 1

        # Repeat by calculating the fitness
    return ga_loop(dist, new_population, mutation_probability, dropout_number, n_generations)