import numpy as np
import copy

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

        #print(randomRoute)
        first = search(List, randomRoute)
        neighRoutes = swap1(randomRoute)
        routesDistance = [search(List, neighRoutes[i]) for i in range(len(neighRoutes))]
        
        min_dis = min(routesDistance)
        Best = routesDistance.index(min_dis)
        P = neighRoutes[Best]

        while min_dis < first: 
            first = min_dis 
            neighRoutes = swap1(P)
            routesDistance = [search(List, neighRoutes[i]) for i in range(len(neighRoutes))]
            
            min_dis = min(routesDistance)
            Best = routesDistance.index(min_dis)
            P = neighRoutes[Best]

    return min_dis, [cityNames[P[i]] for i in range(len(P))]

if __name__ == "__main__": 
    Distance = []
    Routes = []

    for i in range(20):
        min_dis, route = execute()
        Distance.append(min_dis)
        Routes.append(route)
    
    min_dis = min(Distance)
    T = Distance.index(min_dis)
    P = Routes[T]
    print(min_dis, P)