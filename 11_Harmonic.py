

def harm_rec(n):
    if n ==1:
        return n
    else:
        return (1/n) + harm_rec(n-1)
    

x = harm_rec(7)

print(x)