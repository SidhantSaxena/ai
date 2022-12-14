# 8 puzzle
def count(s):
    c = 0
    ideal = [1,2,3,4,5,6,7,8,0]
    for i in range(9):
        if s[i]!=ideal[i] and s[i]!=0:
            c+=1
    return c

def printinnformat(mat):
    for i in range(9):
        if i%3==0 and i>0:
            print(" ")
        print(str(mat[i]),end=" ")
    print()

def move(ar,p,state):
    rh=99999
    store = state.copy()
    for i in range(len(ar)):
        dup = state.copy()
        t=dup[p]
        dup[p]=dup[ar[i]]
        dup[ar[i]]=t
        temph = count(dup)
        if temph<rh:
            rh = temph
            store = dup.copy()
    return store,rh


# 0 means empty
state   =  [1,2,3,0,5,6,4,7,8]
h = count(state)#counts misplaced 
lev=1
print("level "+str(lev))
printinnformat(state)
print("heuristic value:"+str(h))

while h>0:
    # find pos of blank tile 0
    pos = state.index(0)
    lev+=1
    if pos == 0:
        arr=[1,3]
    elif pos==1:
        arr=[0,2,4]
    elif pos==2:
        arr=[1,5]
    elif pos==3:
        arr=[0,4,6]
    elif pos==4:
        arr=[1,3,5,7]
    elif pos==5:
        arr=[2,4,8]
    elif pos==6:
        arr=[3,7]
    elif pos==7:
        arr=[4,6,8]
    elif pos==8:
        arr=[5,6]
    state,h = move(arr,pos,state)
    print("level "+str(lev))
    printinnformat(state)
    print("heuristic value:"+str(h))