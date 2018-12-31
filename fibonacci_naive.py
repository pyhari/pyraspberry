import time
#Fibonacci series without recursion
def fib_naive(n):
    fib_prev=1;
    fib_prev_before=1;
    for i in range(1,n+1):
        if(i==1 or i==2):
            print(1)
        else:
            fib=fib_prev+fib_prev_before
            fib_prev_before=fib_prev
            fib_prev=fib
            print(fib)
        i=i+1
 


start = time.time()
       
input_length=1500
fib_naive(input_length)
end = time.time()
print("Elapsed time",end - start) 
    
