#Linear Search 
def linearsearch(data,element):
    found=False
    for i in range(len(data)):
        if data[i] == element:
            found=True
    return found

#Binary Search  - test data [10,20,30,40,50,1]
def binarysearch(data,element):
    found=False
    mid=len(data)/2
    print(mid)
    for i in range(len(data)):
        if data[i] == element:
            found=True
    return found

        
        
