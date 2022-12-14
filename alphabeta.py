MAX,MIN=1000,-1000

def minmax(depth,index,values,maxi,alpha,beta):
    if depth==3:
        return values[index]
    if maxi:
        best = MIN
        for i in range(2):
            val = minmax(depth+1,index*2+i,values,False,alpha,beta)
            best = max(val,best)
            alpha = max(alpha,best)
            if alpha>=beta:
                break
        return best
    else:
        best = MAX
        for i in range(2):
            val = minmax(depth+1,index*2+i,values,True,alpha,beta)
            best = min(val,best)
            beta = min(best,beta)
            if alpha>=beta:
                break
        return best

if __name__ == "__main__":
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    print("The optimal value is :", minmax(0, 0, values,True, MIN, MAX))

    