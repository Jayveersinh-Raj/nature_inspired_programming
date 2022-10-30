from random import randint
def mutate(individual, chance):
    if(chance<=1):
       chance = chance * 100
    else:
        pass
    genes = []
    for i in individual:
        genes.append(i)

    for i in range(len(genes)):
         mutation_genes = randint(0, 100)
         if (mutation_genes <= chance):
            
           # ran_value = randint(63, 122)
           # # for characters and space that we want, but their ASCII is not within 63, 122, so this technique
           # if(ran_value == 63):
           #     ran_value = 32
           # elif(ran_value == 64):
           #     ran_value = 46

            genes[i] = genes[randint(0, len(genes)-1)]

    individual = ''.join(genes)
   
    return individual

