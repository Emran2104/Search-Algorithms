
import itertools as it
import numpy as np

with open("Search-Algorithms/european_cities.csv", "r") as file:
    print("1")
    x = 6
    city_name = file.readline()
    city_name = city_name.split(";")
    cities_by_index = np.linspace(0, x-1, x, dtype=int)
    
    Line = []
    
    for line in file:
        L = line.split(";")
        for i in range(len(L)):
            L[i] = float(L[i])
        Line.append(L)
    print(Line)
    