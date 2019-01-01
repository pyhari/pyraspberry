import time
import sys
# Fibonacci series with recursion
memo = {}
sys.setrecursionlimit(5000)


def fib_recursion(n):
    if n < 2:
        return 1
    else:
        if n in memo:
            return memo[n]
        else:
            fib = fib_recursion(n-1) + fib_recursion(n-2)
            memo[n] = fib


start = time.time()
input_length = 1500
print(type(input_length))
print('Result is', fib_recursion(input_length))
end = time.time()
print('Elapsed time',end - start)
