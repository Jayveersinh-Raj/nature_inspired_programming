def crossover(parent1, parent2, split_point):
    p1 = parent1
    p2 = parent2

    child = p1[:split_point] + p2[split_point:]

    return child