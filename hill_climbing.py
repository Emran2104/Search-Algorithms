import numpy as np

with open("Search-Algorithms/european_cities.csv", "r") as file:
    cityNames = file.readline().split(";")
    
    List = []
    for line in file:
        tempLine = line.split(";")
        for i in range(len(tempLine)):
            tempLine[i] = float(tempLine[i])
        List.append(tempLine)
    
    