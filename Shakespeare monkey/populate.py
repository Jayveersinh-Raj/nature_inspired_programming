from random import randint

def populate(target_len,n):
    # empty list to store our initial population
    population = []
     
    # Size of population is n with size equal to the target
    for _ in range(n):
      # each element in population is a parent for future generations
      parent =""

      # generating parents randomly using the ascii values of characters
      for _ in range(target_len):
        ran_value = randint(63, 122)

        # for characters and space that we want, but their ASCII is not within 63, 122, so this technique
        if(ran_value == 63):
            ran_value = 32
        elif(ran_value == 64):
            ran_value = 46
        
        parent = parent + str(chr(ran_value))

      # once the loop ends we have a parent  
      population.append(parent)
    return population