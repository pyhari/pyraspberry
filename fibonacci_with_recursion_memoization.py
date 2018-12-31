import time
#Fibonacci series with recursion
memo={}
def fib_recursion(n):
    
    if(n<2):
       return(1)
    else:
        if n in memo:
            return memo[n]
        else:
            fib= fib_recursion(n-1) + fib_recursion(n-2)
            memo[n]=fib
        return(fib)
    


start = time.time()
input_length=1500
print("Result is", fib_recursion(input_length))
end = time.time()
print("Elapsed time",end - start)        
        
 
       
