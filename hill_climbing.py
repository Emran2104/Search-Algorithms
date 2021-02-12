import numpy as np
import random
import copy


def search(List, route):
    distance = 0
    for i in range(1, len(route)):
        distance += List[route[i-1]][route[i]]
    return distance

def swap1(List, route):
    Routes = [route]
    for i in range(1, len(route)-1):
        for j in range(i+1, len(route)):
            tempRoute = copy.deepcopy(route)
            temp = tempRoute[i]
            tempRoute[i] = tempRoute[j]
            tempRoute[j] = temp
            Routes.append(tempRoute)
    return Routes

"""
def swap(route):
    indexToSwap = []
    newRoute = route
    while len(indexToSwap) < 2:
        randomIndex = np.random.randint(1, routeLength)
        if randomIndex not in indexToSwap:
            indexToSwap.append(randomIndex)
    temp = newRoute[indexToSwap[0]]
    newRoute[indexToSwap[0]] = newRoute[indexToSwap[1]]
    newRoute[indexToSwap[1]] = temp
    #print(indexToSwap) 
    return newRoute
"""

with open("Search-Algorithms/european_cities.csv", "r") as file:
    cityNames = file.readline().split(";")

    List = []
    
    for line in file:
        tempLine = line.split(";")
        for i in range(len(tempLine)):
            tempLine[i] = float(tempLine[i])
        List.append(tempLine)

    for i in List:
        print(i)
    #print([i for i in List])
    routeLength = len(List) 
    randomRoute = [i for i in range(routeLength)]
    random.shuffle(randomRoute)
    #print("First: ", randomRoute)

    neighRoutes = swap1(List, randomRoute)
    routesDistance = [search(List, neighRoutes[i]) for i in range(len(neighRoutes))]
    #print(routesDistance)
    """
    min_dis = min(distance)
    Best = distance.index(min_dis)
    P = bestRoute[Best]
    """
    #print( [cityNames[P[i]] for i in range(len(P))] )