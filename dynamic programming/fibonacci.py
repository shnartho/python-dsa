# 1 1 2 3 5 8 13 21 ...
# this code is calling the same function multiple time, therefore its not optimized
def fib(n):
    if n <= 2:
        return 1
    else:
        result = fib(n-1) + fib(n-2)
    return result

print(fib(50)) # will take a lot of time for to print the result...