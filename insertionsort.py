# test data = [10,1,20,3,4,6,0]
def insertionsort(ulist):
    for i in range(1,len(ulist)):
        current=ulist[i]
        while i>0 and ulist[i-1]>current:
            ulist[i]=ulist[i-1]
            ulist[i-1]=current
            i=i-1
    print(ulist)`   1       