from collections import defaultdict as dd
j1,j2,aim=4,3,2
visited = dd(lambda:False)
def waterjug(amt,amt2):
    if (amt==aim and amt2==0) or (amt2==aim and amt==0):
        print(amt,amt2)
        return True
    if not visited[(amt,amt2)]:
        print(amt,amt2)
        visited[(amt,amt2)]=True
        return waterjug(0,amt2) or waterjug(amt,0) or waterjug(j1,amt2)  or waterjug(amt,j2) or waterjug(amt+min(amt2,j1-amt),amt2-min(amt2,j1-amt)) or waterjug(amt-min(amt,(j2-amt2)),amt2+min(amt,(j2-amt2)))
    else:
        return False

waterjug(0,0)  