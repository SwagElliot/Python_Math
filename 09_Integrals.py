import matplotlib.pyplot as plt
import numpy as np

h = 0.00001

func = input("Function: ")

b = int(input("x-Value, low: "))
a = int(input("x-Value, high: "))

f = lambda x:eval(func)

integral = 0
while b < a:
    integral = integral + f(b) * h
    b = b + h


print("The integrals value is:",integral)