import numpy as np
import copy

#Given a route, finds the distance of the route
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

with open("european_cities.csv", "r") as file:
    cityNames = file.readline().split(";")

    List = []
    
    for line in file:
        tempLine = line.split(";")
        for i in range(len(tempLine)):
            tempLine[i] = float(tempLine[i])
        List.append(tempLine)

    routeLength = len(List) - 13
    randomRoute = [i for i in range(routeLength)]
    np.random.shuffle(randomRoute)

    neighRoutes = swap1(List, randomRoute)
    routesDistance = [search(List, neighRoutes[i]) for i in range(len(neighRoutes))]

    min_dis = min(routesDistance)
    Best = routesDistance.index(min_dis)
    P = neighRoutes[Best]


    for i in range(20):
        neighRoutes = swap1(List, P)
        routesDistance = [search(List, neighRoutes[i]) for i in range(len(neighRoutes))] 
        min_dis = min(routesDistance)


    #print(min_dis)

    """
    print(min_dis)
    print( [cityNames[P[i]] for i in range(len(P))] )
    """