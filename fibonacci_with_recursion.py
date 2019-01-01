import time
#Fibonacci series with recursion
def fib_recursion(n):
    if(n<2):
       return(1)
    else:
        fib= fib_recursion(n-1) + fib_recursion(n-2)
        return(fib)
    


start = time.time()
input_length=50
print("Result is", fib_recursion(input_length))
end = time.time()
print("Elapsed time",end - start)        
        
 
       