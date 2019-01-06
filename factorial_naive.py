import time
start_time = time.time()
def fact(n):
    fact=1
    for i in range(1,n):
        fact=fact*n
        n=n-1
    return fact    

print("Factorial is ", fact(10000))
end_time = time.time()
print("Elapsed time:", end_time - start_time)

