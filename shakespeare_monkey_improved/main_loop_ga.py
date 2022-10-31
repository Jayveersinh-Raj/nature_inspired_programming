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
    bar = '█'*int(max_score) + '-' * (100 - int(max_score))
    print(f"\r|{bar}| {max_score:.2f}%", end = "\r")

    # list of candidates with score > 0
    candidates = []
    candidate_scores = []
    for i in range(len(scores)):
        # all those with atleast 1 correct order of letter would be allowed to mate
        if(scores[i]>0):

            # if target is achieved
            if(scores[i] == 1):
                return f"\n\nTarget achieved: '{target}' on {generation} generation \n"

            good_candidate = population[i]
            candidate_scores.append(scores[i])
            candidates.append(good_candidate)
     
    # new population from mating pool
    new_population = []
    
    # making them as integers between 0 to 100, and getting their max
    int_scores = [int(score*100) for score in candidate_scores]
    max_score = max(int_scores)
 
    if(generation == 900):
        return population[int_scores.index(max_score)]
        
    for i in range(len(population)):
        # creating a mating pool of elements using their probabilities from fitting 
        mating_parents = ga.select(candidates, int_scores, max_score)

        # split from random points
        split_point = randint(0, len(target)-1)

        # crossover of those parents to yield a breed
        breed = ga.crossover(mating_parents[0], mating_parents[1], split_point)

        # mutating the produced breed and adding it to the population
        new_population.append(ga.mutate(breed, mutation_probability))

    # Repeat by calculating the fitness
    return ga_loop(target, new_population, mutation_probability)