from random import randint

# class with methods of the entire genetic algorithm loop
class GeneticAlgorithm:

    def __init__(self) -> None:
        pass


    # function to populate the population
    @classmethod
    def populate(cls,target_len,n) -> list:

    # empty list to store our initial population
      population = []
       
      # Size of population is n with size equal to the target
      for _ in range(n):
        # list to store the paths as individual
        individual = []
        # each element in population is a parent for future generations
        for _ in range(target_len):
          notUnique = True
          while notUnique:
            ran_value = randint(0, 12)
            if ran_value in individual:
              ran_value = randint(0, 12)
            else:
              notUnique = False
          individual.append(ran_value)
        # once the loop ends we have a parent  
        population.append(individual)
       
      return population


    # function to calculate fitness
    def fitness(dist, individual, sum) -> tuple:
      # fitness score of inidividual
      score = 0

      # for each character if they are the same and in the correct position
      for i in range(len(individual)):
        if(i == len(individual)-1):
           score+=dist[individual[i]][individual[0]]
        else:
          score+=dist[individual[i]][individual[i+1]]
       
      if(score<sum):
            sum = score
            
      return (score,sum)


    # function to create a mating pool for cross over by populating parents according to their fitting
    @classmethod
    def select(cls, population, scores, max_score) -> list:
      parents_to_breed = []
      # scores in integer values
      p1 = cls.accept(population,scores, max_score)
      p2 = cls.accept(population, scores, max_score)
      parents_to_breed.append(p1)
      parents_to_breed.append(p2)
            
      return parents_to_breed


    # check the probabilities of generated parent meets the criteria with random number probability
    def accept(population, scores, max_score) -> list:
      while True:
        parent_index = randint(0, len(population)-1)
        rand_num = randint(0,max_score)
        if(rand_num < scores[parent_index]):
          return population[parent_index]
        else:
          pass 
  

    # function for crossover
    def crossover(parent1, parent2, split_point) -> list:
      p1 = parent1
      p2 = parent2
      child = []
      if(split_point == 0):
        child = p2
      elif(split_point == len(p1)-1):
        child = p1
      else:
        for i in p1[:split_point]:
          child.append(i)
        for j in p2:
            if j in child:
              pass
            else:
              child.append(j)
      
      return child

    
    # function for mutation
    def mutate(individual, chance) -> list:
     
      # if chance is not provided as percentage, multiply by 100
      if(chance<=1):
         chance = chance * 100
      else:
          pass
      
      # according to given mutation chance change characters/genes of an individual
      for i in range(len(individual)):
           mutation_genes = randint(0, 100)

           if (mutation_genes <= chance):
             same = True
             while same:
               ran_value = randint(0, len(individual)-1)
               if(individual[i] != individual[ran_value]):
                 individual[i], individual[ran_value] = individual[ran_value], individual[i]
                 same = False
               else:
                pass

      return individual


  