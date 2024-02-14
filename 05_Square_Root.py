a = float(input("Pick a number to take the square root of: "))

epsilon = float(input("Pick the margin: "))

b = a/2

while b*b > a + epsilon or b*b < a - epsilon:
    delta = abs((b*b - a)/100)
    if b*b > a:
        b = b - delta
    if b*b < a:
        b = b + delta
    print(b)

print("The square root of ",a," is equal to ",b," +- ",epsilon,".")
