"""
Testing for partial mapped crossover 
NOT DONE YET
"""

def check(parent1, parent2, f, t):
    i = parent1[f:t]
    j = parent2[f:t]

    child = [None for i in range(len(parent1))]
    child[f:t] = i
    child1 = [None for i in range(len(parent1))]
    child1[f:t] = j

    for k in range(len(i)):
        A = parent2.index(i[k])
        child[A] = j[k]

        B = parent1.index(j[k])
        child1[B] = i[k]

    for l in range(len(child)):
        if child[l] == None:
            child[l] = parent2[l]
        if child1[l] == None:
            child1[l] = parent1[l]
            
    return child, child1



print(check( [1, 2, 0, 3, 5, 4], [1, 4, 2, 5, 0, 3], 2, 4 ))
#print(check( [2, 4, 6, 7, 3, 8, 5, 1], [8, 5, 3, 4, 1, 2, 7, 6], 3, 6 ))