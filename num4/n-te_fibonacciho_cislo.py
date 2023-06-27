def fib(n):
    a= 1 #větší
    b=1 #menší
    for i in range(n-2):
        a, b = a+b, a
    return a
