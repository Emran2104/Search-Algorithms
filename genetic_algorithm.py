from timeit import default_timer as timer
import itertools as it
import numpy as np


def search(List, route):
    distance = 0
    for i in range(len(route)):
        distance += List[route[i-1]][route[i]]
    return distance


def swap(parent, p1, p2):
    neste = parent.copy()
    neste[p1] = parent[p2]
    neste[p2] = parent[p1]
    return neste


def crossover(parent1, parent2):
    half = len(parent1) // 2
    start = np.random.randint(0, len(parent1)-half)
    end = start + half

    c1 = parent1[start:end]
    c2 = parent2[start:end]
    
    for i in range(half):
        bIdx = parent2.index(c1[i])
        parent2 = swap(parent2, i+start, bIdx)
        aIdx = parent1.index(c2[i])
        parent1 = swap(parent1, i+start, aIdx)

    return parent1, parent2

def survivor(population, distanceOfPopulation):
    score = [1/distanceOfPopulation[i] for i in range(len(distanceOfPopulation))]
    score = [score[i]/sum(score) for i in range(len(distanceOfPopulation))]

    survivor = np.random.choice(len(population), size=n, replace=False, p=score) 
    survivor = [population[survivor[i]] for i in range(len(survivor))]
    return survivor

with open("european_cities.csv", "r") as file:
    cityNames = file.readline().split(";")
    
    List = []
    for line in file:
        tempLine = line.split(";")
        for i in range(len(tempLine)):
            tempLine[i] = float(tempLine[i])
        List.append(tempLine)

    routeLength = len(List) - 14
    randomRoute = [i for i in range(routeLength)]
    
    generation = 2
    n = 60
    population = []
    while len(population) < n:
        np.random.shuffle(randomRoute)
        if randomRoute not in population:
            population.append(randomRoute.copy())

    distanceOfPopulation = [search(List, population[i]) for i in range(len(population))]
    score = [1/distanceOfPopulation[i] for i in range(len(distanceOfPopulation))]
    score = [score[i]/sum(score) for i in range(len(distanceOfPopulation))]

    parent = np.random.choice(len(population), size=n//2, replace=False, p=score) 
    parent = [population[parent[i]] for i in range(len(parent))]

    child = []
    for i in range(0, len(parent), 2):
        c1, c2 = crossover(parent[i], parent[i+1])
        child.append(c1)
        child.append(c2)

    distanceOfChild = [search(List, child[i]) for i in range(len(child))]
    childScore = [1/distanceOfChild[i] for i in range(len(distanceOfChild))]
    childScore = [childScore[i]/sum(childScore) for i in range(len(child))]

    for i in range(len(child)):
        population.append(child[i])
        distanceOfPopulation.append(distanceOfChild[i])

    population = survivor(population, distanceOfPopulation)
    distanceOfPopulation = [search(List, population[i]) for i in range(len(population))]
    score = [1/distanceOfPopulation[i] for i in range(len(distanceOfPopulation))]
    score = [score[i]/sum(score) for i in range(len(distanceOfPopulation))]

    while max(score) - min(score) > 0.001:
        generation += 1
        parent = np.random.choice(len(population), size=n//2, replace=False, p=score) 
        parent = [population[parent[i]] for i in range(len(parent))]

        child = []
        for i in range(0, len(parent), 2):
            c1, c2 = crossover(parent[i], parent[i+1])
            child.append(c1)
            child.append(c2)

        distanceOfChild = [search(List, child[i]) for i in range(len(child))]
        childScore = [1/distanceOfChild[i] for i in range(len(distanceOfChild))]
        childScore = [childScore[i]/sum(childScore) for i in range(len(child))]

        for i in range(len(child)):
            population.append(child[i])
            distanceOfPopulation.append(distanceOfChild[i])

        population = survivor(population, distanceOfPopulation)
        distanceOfPopulation = [search(List, population[i]) for i in range(len(population))]
        score = [1/distanceOfPopulation[i] for i in range(len(distanceOfPopulation))]
        score = [score[i]/sum(score) for i in range(len(distanceOfPopulation))]
    print(min(distanceOfPopulation), generation)