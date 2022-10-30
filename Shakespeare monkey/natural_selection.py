def select(population, scores):
    # mating pool where elements are in accordance to their probablities
    mating_pool = []
    int_scores = [int(score*100) for score in scores]

    for i in range(len(population)):
        score = int_scores[i]
        for _ in range(score):
          mating_pool.append(population[i])
          
    return mating_pool