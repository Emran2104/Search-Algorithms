from timeit import default_timer as timer
import itertools as it
import numpy as np


def calculateDistance(List, route):
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
    child1 = parent1.copy()
    child2 = parent2.copy()
    c1 = parent1[start:end]
    c2 = parent2[start:end]
    for i in range(half):
        bIdx = child2.index(c1[i])
        child2 = swap(child2, i+start, bIdx)
        aIdx = child1.index(c2[i])
        child1 = swap(child1, i+start, aIdx)

    return child1, child2



def survivor(population, distanceOfPopulation, populationSize):
    score = [1-(distanceOfPopulation[i]/sum(distanceOfPopulation)) for i in range(len(distanceOfPopulation))]
    score = [score[i]/sum(score) for i in range(len(score))]

    #score = [1/distanceOfPopulation[i] for i in range(len(distanceOfPopulation))]
    #score = [score[i]/sum(score) for i in range(len(distanceOfPopulation))]

    survivor1 = np.random.choice(len(population), size=populationSize, replace=False, p=score) 
    survivor = [population[survivor1[i]] for i in range(len(survivor1))]
    return survivor



def operation(populationSize, amountOfCities, parentSize, improvementCount):
    with open("european_cities.csv", "r") as file:
        timerStart = timer()

        cityNames = file.readline().split(";")
        List = []
        for line in file:
            tempLine = line.split(";")
            for i in range(len(tempLine)):
                tempLine[i] = float(tempLine[i])
            List.append(tempLine)

        populationSize = populationSize
        generation = 0
        amountOfCities = len(List) - (len(List) - amountOfCities)
        parentSize = parentSize
        noImprovements = 0

        routeLength = amountOfCities
        randomRoute = [i for i in range(routeLength)]

        population = []
        while len(population) < populationSize:
            np.random.shuffle(randomRoute)
            if randomRoute not in population:
                population.append(randomRoute.copy())

        distanceOfPopulation = [calculateDistance(List, population[i]) for i in range(len(population))]
        score = [1-(distanceOfPopulation[i]/sum(distanceOfPopulation)) for i in range(len(distanceOfPopulation))]
        score = [score[i]/sum(score) for i in range(len(score))]

        #score = [1/distanceOfPopulation[i] for i in range(len(distanceOfPopulation))]
        #score = [score[i]/sum(score) for i in range(len(distanceOfPopulation))]

        currentBest = min(distanceOfPopulation)

        while noImprovements < improvementCount:
            generation += 1
            parent = np.random.choice(len(population), size=parentSize, replace=False, p=score) 
            parent = [population[parent[i]] for i in range(len(parent))]

            child = []
            for i in range(0, len(parent), 2):
                c1, c2 = crossover(parent[i], parent[i+1])
                child.append(c1)
                child.append(c2)

            distanceOfChild = [calculateDistance(List, child[i]) for i in range(len(child))]
            childScore = [1/distanceOfChild[i] for i in range(len(distanceOfChild))]
            childScore = [childScore[i]/sum(childScore) for i in range(len(child))]
            
            for i in range(len(child)):
                population.append(child[i])
                distanceOfPopulation.append(distanceOfChild[i])
                score.append(childScore[i])
            
            population = survivor(population, distanceOfPopulation, populationSize)
            distanceOfPopulation = [calculateDistance(List, population[i]) for i in range(len(population))]

            score = [1-(distanceOfPopulation[i]/sum(distanceOfPopulation)) for i in range(len(distanceOfPopulation))]
            score = [score[i]/sum(score) for i in range(len(score))]


            #score = [1/distanceOfPopulation[i] for i in range(len(distanceOfPopulation))]
            #score = [score[i]/sum(score) for i in range(len(score))]

            if currentBest > min(distanceOfPopulation):
                currentBest = min(distanceOfPopulation)
            else:
                noImprovements += 1

        minDistance = min(distanceOfPopulation)
        minRoute = population[distanceOfPopulation.index(minDistance)]
        maxDistance = max(distanceOfPopulation)
        maxRoute = population[distanceOfPopulation.index(maxDistance)]

        timerStop = timer()
        totalTime = timerStop - timerStart
        return minDistance, minRoute, maxDistance, maxRoute, totalTime, populationSize, parentSize, amountOfCities, generation
    


def main(n, populationSize, amountOfCities, parentSize, improvementCount):
    minDistanceList = []
    minRouteList = []
    maxDistanceList = []
    maxRouteList = []
    generationList = []
    time = 0
    for i in range(n):
        minDistance, minRoute, maxDistance, maxRoute, totalTime, populationSize, parentSize, amountOfCities, generation = operation(populationSize=populationSize, amountOfCities=amountOfCities, parentSize=parentSize, improvementCount=improvementCount)
        minDistanceList.append(minDistance)
        minRouteList.append(minRoute)
        maxDistanceList.append(maxDistance)
        maxRouteList.append(maxRoute)
        generationList.append(generation)
        time += totalTime

    minDistance = min(minDistanceList)
    minRoute = minRouteList[minDistanceList.index(minDistance)]
    generation = generationList[minDistanceList.index(minDistance)]
    maxDistance = max(minDistanceList)
    maxRoute = maxRouteList[minDistanceList.index(maxDistance)]
    

    print("Minimum Distance: ",minDistance)
    print("Maximum Distance: ",maxDistance)
    print("Best Route: ",minRoute)
    print("Worst Route: ",maxRoute)
    print("Population Size: ",populationSize)
    print("Parent Selection Size: ",parentSize)
    print("Cities: ",amountOfCities)
    print("Generations: ",generation)
    print("Time to execute: ",time)



main(n=10, populationSize=100, amountOfCities=24, parentSize=50, improvementCount=1000)