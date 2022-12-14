from queue import PriorityQueue as PQ
def bestfs(graph,src,target,v):
    pq = PQ()
    pq.put((0,src))
    visted=[0 for _ in range(v)]
    visted[src]=1
    while pq.empty()==False:
        u = pq.get()[1]
        print(u,end=" ")
        if u==target:
            break
        for n,c in graph[u]:
            if visted[n]==0:
                visted[n]=1
                pq.put((c,n))
    print()

def addedge(graph,x,y,c):
    graph[x].append((y,c))
    graph[y].append((x,c))

graph=[[] for _ in range(14)]
while True:
    x,y,c = map(int,input().split())
    if c==0:
        break
    addedge(graph,x,y,c)
bestfs(graph,0,9,14)



