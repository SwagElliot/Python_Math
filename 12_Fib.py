

def fib_rec(n):
    if n == 1 or n == 0:
        return n
    else:
        return fib_rec(n-2) + fib_rec(n-1)
    

x = fib_rec(18)
print(x)