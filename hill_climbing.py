import numpy as np
import copy
from timeit import default_timer as timer

def search(List, route):
    """
    Given a route, calculates the distance of the route with given List. Where List is all the distance values from each city.
    """
    distance = 0
    for i in range(len(route)):
        distance += List[route[i-1]][route[i]]
    return distance


def swap1(route):
    """
    Here, with given route, we can swap some of indexes with each other, and return all the routes that has been swapped. 
    We swap some of the indexes (cities), except for the starting. (neighbours)
    """
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
    """
    This is where all the functions gets run.
    1. We start with a random route (or previous route), and checks its distance.
    2. We then give the best route to "swap" function, and checks its distance.
    We then have a while loop that does 1. and 2. over and over until it can not find any better distance (local or global opimum).

    Return the best route and its distance
    """
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

    return minDis, [cityNames[minRoute[i]] for i in range(len(minRoute))]


if __name__ == "__main__": 
    """
    Here we run the "execute" function 20 times and save all the minimum distance and print out the best route and distance from the 20 runs.
    Also calculates the time it took to execute.
    """
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