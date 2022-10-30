from random import randint
from genetic_algorithm import GeneticAlgorithm as ga

# to store number of generation
generation = 0

def ga_loop(target, population, mutation_probability):

    # calculate fitness for each
    # list to store fitness values
    global generation
    generation += 1
    
    # scores from fitting function
    scores = []
    for p in population:
        scores.append(ga.fitness(target, p))
    max_score = sorted(scores, reverse = True)[0]*100
    print(max_score)

    # list of candidates with score > 0
    candidates = []
    candidate_scores = []
    for i in range(len(scores)):
        # all those with atleast 1 correct order of letter would be allowed to mate
        if(scores[i]>0):

            # if target is achieved
            if(scores[i] == 1):
                return f"Target achieved: '{target}' on {generation} generation"

            good_candidate = population[i]
            candidate_scores.append(scores[i])
            candidates.append(good_candidate)
     
    # creating a mating pool of elements using their probabilities from fitting 
    mating_pool = ga.select(candidates, candidate_scores)

    # new population from mating pool
    new_population = []
    for i in range(len(population)):
        # 2 random parents
        p1 = randint(0, len(mating_pool)-1)
        p2 = randint(0, len(mating_pool)-1)

        # split from random points
        split_point = randint(0, len(target)-1)

        # crossover of those parents to yield a breed
        breed = ga.crossover(mating_pool[p1], mating_pool[p2], split_point)

        # mutating the produced breed and adding it to the population
        new_population.append(ga.mutate(breed, mutation_probability))

    # Repeat by calculating the fitness
    return ga_loop(target, new_population, mutation_probability)