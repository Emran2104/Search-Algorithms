from timeit import default_timer as timer
import itertools as it
import numpy as np


def calculate(L, A):
    sumDistance = 0
    for i in range(1, len(A)):
        sumDistance += L[A[i-1]][A[i]]
    sumDistance += L[A[-1]][A[0]]
    return sumDistance

with open("Search-Algorithms/european_cities.csv", "r") as file:
    start = timer()
    nrOfCities = 6
    cityName = file.readline()
    cityName = cityName.split(";")
    citiesByIndex = np.linspace(0, nrOfCities-1, nrOfCities, dtype=int)
    
    Line = []
    
    for line in file:
        L = line.split(";")
        for i in range(len(L)):
            L[i] = float(L[i])
        Line.append(L)
    
    A = list(it.permutations(citiesByIndex))
    best_route = A[0]
    best_score = 100000
    route = []
    for i in range(len(A)):
        score = calculate(Line, A[i]) 
        if score < best_score:
            best_score = score
            best_route = A[i]
            
    for i in range(len(best_route)):
        route.append(cityName[best_route[i]])
        
    end = timer()
    print("Time: ", end - start)
    print("Score: ", best_score)
    print("Route: ", route)
    