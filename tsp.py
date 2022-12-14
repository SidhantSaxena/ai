from sys import maxsize
from itertools import permutations

def tsp(graph,s,v):
    ver = []
    for i in range(v):
        if i!=s:
            ver.append(i)
    next = permutations(ver)
    mini = maxsize  
    for i in next:
        k=s
        path_weight=0
        for j in i:
            path_weight+=graph[k][j]
            k=j
        path_weight+=graph[k][s]
        mini = min(mini,path_weight)
    return mini
graph = [[0, 10, 15, 20], [10, 0, 35, 25],[15, 35, 0, 30], [20, 25, 30, 0]]
s = 0
print(tsp(graph, s, 4))