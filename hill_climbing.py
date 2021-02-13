import numpy as np
import copy
from timeit import default_timer as timer

#Given a route, finds the distance of the route
def search(List, route):
    distance = 0
    for i in range(len(route)):
        distance += List[route[i-1]][route[i]]
    return distance

def swap1(route):
    Routes = [route]
    for i in range(1, len(route)-1):
        for j in range(i+1, len(route)):
            tempRoute = copy.deepcopy(route)
            temp = tempRoute[i]
            tempRoute[i] = tempRoute[j]
            tempRoute[j] = temp
            Routes.append(tempRoute)
    return Routes

def execute():
    with open("european_cities.csv", "r") as file:
        cityNames = file.readline().split(";")
        
        List = []
        for line in file:
            tempLine = line.split(";")
            for i in range(len(tempLine)):
                tempLine[i] = float(tempLine[i])
            List.append(tempLine)
            
        routeLength = len(List)
        randomRoute = [i for i in range(routeLength)]
        np.random.shuffle(randomRoute)

        
        distance = search(List, randomRoute)
        neighRoutes = swap1(randomRoute)
        routesDistance = [search(List, neighRoutes[i]) for i in range(len(neighRoutes))]
        
        minDis = min(routesDistance)
        tempIndex = routesDistance.index(minDis)
        minRoute = neighRoutes[tempIndex]

        while minDis < distance: 
            distance = minDis 
            neighRoutes = swap1(minRoute)
            routesDistance = [search(List, neighRoutes[i]) for i in range(len(neighRoutes))]
            
            minDis = min(routesDistance)
            tempIndex = routesDistance.index(minDis)
            minRoute = neighRoutes[tempIndex]

    #Best Outcome
    #print(search(List, [4, 9, 20, 1, 5, 22, 23, 2, 17, 15, 13, 18, 0, 12, 7, 11, 16, 3, 8, 6, 21, 19, 14, 10]))

    return minDis, [cityNames[minRoute[i]] for i in range(len(minRoute))]

if __name__ == "__main__": 
    Distance = []
    Routes = []
    start = timer()

    for i in range(20):
        minDistance, route = execute()
        Distance.append(minDistance)
        Routes.append(route)
    
    minimumDistance = min(Distance)
    tempIndexMin = Distance.index(minimumDistance)
    minRoute = Routes[tempIndexMin]

    maximumDistance = max(Distance)
    tempIndexMax = Distance.index(maximumDistance)
    maxRoute = Routes[tempIndexMax]

    end = timer()
    print("Minimum Route:", minRoute)
    print(" Min Distance:", minimumDistance)
    print("Maximum Route:", maxRoute)
    print(" Max Distance:", maximumDistance)
    print("Execute time:", end-start)

    """
    Minimum Route: ['London', 'Paris', 'Brussels', 'Hamburg', 'Copenhagen', 'Stockholm', 
                    'Saint Petersburg', 'Moscow', 'Kiev', 'Bucharest', 'Istanbul', 'Sofia', 
                    'Belgrade', 'Budapest', 'Vienna', 'Warsaw', 'Berlin', 'Prague', 
                    'Munich', 'Milan', 'Rome', 'Barcelona', 'Madrid', 'Dublin']
    Min Distance: 12287.07
    """