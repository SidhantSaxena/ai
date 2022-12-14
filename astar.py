def f(g,h,n):
    return g[n]+h[n]

def update(to_remove,to_add,m):
    to_remove.remove(m)
    to_add.append(m)


def a_star(cost,h,st,g):
    pathset=[]#all possible path from st to goal

    open=[st]#unvisited
    closed=[]#visited

    path_len={}#total path cost length
    path_len[st]=0

    parent={}
    parent[st]=st #helps us retrack 
    while len(open)>0:
        node=None
        for n in open:
            if node == None or f(path_len,h,n)<f(path_len,h,node):
                node=n
        if node==None:
                # no path exist 
            break
        if node == g:
            f_n = f(path_len,h,node)
            recon = []
            # used for reconstructing the path from node to start
            aux = node
            while parent[aux]!=aux:
                recon.append(aux)
                aux = parent[aux]
            recon.append(aux)
            recon=recon[::-1]
            pathset=[recon,f_n]
            break
        else:
            path_cost = cost[node]
            for index in range(len(path_cost)):
                weight = path_cost[index]
                if weight>0:
                    if index not in open and index not in closed:
                        open.append(index)
                        parent[index]=node
                        path_len[index] = path_len[node] + weight
                    else:
                        if path_len[index]>path_len[node]+weight:
                            path_len[index] = path_len[node]+weight
                            parent[index] = node
                            if index in closed:
                                update(closed,open,index)
            update(open,closed,node)
            # pathset generated
    print(pathset[0])

cost=[[0,2,-1,2],[1,0,1,1],[1,2,0,1],[1,1,1,0]]
g=2
h = [0,2,2,1]
a_star(cost,h,0,g)        