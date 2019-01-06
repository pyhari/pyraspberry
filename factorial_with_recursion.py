import time
start_time = time.time()
def factorial(n):
    fact=1
    if(n==1):
        return fact 
    else:
        fact=fact*factorial(n)
        n=n-1
    return fact    

print("Factorial is ", factorial(3))
end_time = time.time()
print("Elapsed time:", end_time - start_time)


