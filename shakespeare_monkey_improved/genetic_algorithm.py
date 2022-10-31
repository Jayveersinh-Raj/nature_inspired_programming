from random import randint
import string

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
        # each element in population is a parent for future generations
        parent =""
  
        # generating parents randomly using the ascii values of characters
        for _ in range(target_len):
          ran_value = randint(32, 125)
  
          # for characters and space that we want, but their ASCII is not within 63, 122, so this technique
         # if(ran_value == 63):
         #     ran_value = 32
         # elif(ran_value == 64):
         #     ran_value = 46
          
          parent = parent + str(chr(ran_value))
  
        # once the loop ends we have a parent  
        population.append(parent)

      return population


    # function to calculate fitness
    def fitness(target, individual) -> float:

      # fitness score of inidividual
      score = 0
  
      # for each character if they are the same and in the correct position
      for i in range(len(target)):
          if(target[i] == individual[i]):
              score+=1      
          else:
              pass
            
      return score/len(target)


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
    def accept(population, scores, max_score):
      while True:
        parent_index = randint(0, len(population)-1)
        rand_num = randint(0,max_score)
        if(rand_num < scores[parent_index]):
          return population[parent_index]
        else:
          pass 
  

    # function for crossover
    def crossover(parent1, parent2, split_point) -> string:
      p1 = parent1
      p2 = parent2
  
      child = p1[:split_point] + p2[split_point:]
  
      return child

    
    # function for mutation
    def mutate(individual, chance) -> string:
     
      # if chance is not provided as percentage, multiply by 100
      if(chance<=1):
         chance = chance * 100
      else:
          pass

      # to store genes of an individual (characters)
      genes = []
      for i in individual:
          genes.append(i)
      
      # according to given mutation chance change characters/genes of an individual
      for i in range(len(genes)):
           mutation_genes = randint(0, 100)

           if (mutation_genes <= chance):
             ran_value = randint(63, 122)
     
             # for characters and space that we want, but their ASCII is not within 63, 122, so this technique
             if(ran_value == 63):
                 ran_value = 32
             elif(ran_value == 64):
                 ran_value = 46
          
             genes[i] = chr(ran_value)
   
      individual = ''.join(genes)
      
      return individual


  