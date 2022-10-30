from random import randint
import populate
import fitness
import crossover
import natural_selection
import mutation


generation = 0
def check_fitness(target, population, mutation_probability):
    # calculate fitness for each
    # list to store fitness values
    global generation
    generation += 1
    #print(generation)
    scores = []
    for p in population:
        scores.append(fitness.calculate_fitness(target, p))
    max_score = sorted(scores, reverse = True)[0]*100
    print(max_score)

    # list of candidates with score > 0
    candidates = []
    candidate_scores = []
    for i in range(len(scores)):
        # Line of change
        if(scores[i]>0):
            if(scores[i] == 1):
                print(f"Target achieved: {target}, on {generation} generation")
                return 
            good_candidate = population[i]
            candidate_scores.append(scores[i])
            candidates.append(good_candidate)
     
    # NaturalSelection
    mating_pool = natural_selection.select(candidates, candidate_scores)
    #print(len(population))

    # new population from mating pool
    new_population = []
    for i in range(len(population)):
        p1 = randint(0, len(mating_pool)-1)
        p2 = randint(0, len(mating_pool)-1)
        split_point = randint(0, len(target)-1)
        breed = crossover.crossover(mating_pool[p1], mating_pool[p2], split_point)
       # p1_fitness = fitness.calculate_fitness(target, mating_pool[p1])
       # p2_fitness = fitness.calculate_fitness(target, mating_pool[p2])

        ##if(fitness.calculate_fitness(target, breed) < p1_fitness):
         # if(p1_fitness < p2_fitness):
         #   new_population.append(mating_pool[p2])
         # else:
         #   new_population.append(mating_pool[p1])
        
        #else:
        new_population.append(mutation.mutate(breed, mutation_probability))

    
    # Repeat by calculating the fitness
    check_fitness(target, new_population, mutation_probability)

if __name__ == "__main__":
    population_size = 1500
    notValid = True

    # valid discontinues ascii values
    valid = [32, 46]

    # Until a valid input is achieved
    while notValid:
        target = input("Enter your to be guessed target string >")
        ascii_target = [ord(ch) for ch in target]
        
        for ascii in ascii_target:
          if(ascii<65 or ascii>122):
              if(ascii in valid):
                  notValid = False
              else:
                  print("Please enter a valid string")
          else:
              notValid = False

    # Populate
    population = populate.populate(len(target), population_size)
    mutation_per = 0.01
    check_fitness(target, population, mutation_per)
    