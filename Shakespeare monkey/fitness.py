def calculate_fitness(target, individual):
    # fitness score of inidividual
    score = 0

    # for each character if they are the same and in the correct position
    for i in range(len(target)):
        if(target[i] == individual[i]):
            score+=1      
        else:
            pass
    return score/len(target)
